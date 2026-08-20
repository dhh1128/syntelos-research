#!/usr/bin/env python3
"""Lint the Syntelos taxonomy registry.

The registry is the source of truth; the paper is generated from it. That inversion only pays off
if the registry is mechanically checkable, which is what this does. Run with no arguments from
anywhere; paths resolve relative to this file.

Checks, in the order the plan (design/syntelos-2.0-plan.md §7) lists them:

  C1  every node carries a definition, >=2 examples, and >=1 counter-example
  C2  no duplicate ids; id matches facet and filename
  C3  every counter-example names a `correct` node that exists
  C4  discriminators cover every sibling, and name only real siblings
  C5  closed facets hold exactly their declared cardinality
  C6  every example and counter-example cites a source or gives a reason
  C7  cross-repo: bakobo/schema/gcd enums equal the registry's closed facets

C7 is skipped with a notice when the gcd repo is not present, so the suite still runs in a clean
checkout. It is NOT skipped silently: a skip is reported, because a silent skip reads as a pass.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
TAXONOMY = ROOT / "taxonomy"
GCD_SCHEMA = pathlib.Path.home() / "code/bakobo/schema/gcd/gcd.schema.json"

# Which registry facet each GCD schema enum must agree with. GCD spells state-kind values
# differently today (`info` for `information`); the mapping records the drift the check enforces
# away rather than papering over it.
GCD_SPELLING = {"information": "info"}


class Lint:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notices: list[str] = []

    def fail(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def notice(self, msg: str) -> None:
        self.notices.append(msg)


def load_facets(lint: Lint) -> dict:
    path = TAXONOMY / "facets.yaml"
    if not path.exists():
        lint.fail("taxonomy/facets.yaml", "missing")
        return {}
    return yaml.safe_load(path.read_text()) or {}


def load_nodes(lint: Lint) -> dict[str, dict]:
    nodes: dict[str, dict] = {}
    for path in sorted(TAXONOMY.rglob("*.yaml")):
        if path.name == "facets.yaml":
            continue
        rel = path.relative_to(ROOT)
        try:
            data = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError as exc:
            lint.fail(str(rel), f"unparseable: {exc}")
            continue

        node_id = data.get("id")
        if not node_id:
            lint.fail(str(rel), "no id")
            continue

        # C2: id must be unique, and must agree with the path it lives at.
        if node_id in nodes:
            lint.fail(str(rel), f"duplicate id {node_id!r}")
            continue
        expected = f"{path.parent.name}/{path.stem}"
        if node_id != expected:
            lint.fail(str(rel), f"id {node_id!r} does not match path (expected {expected!r})")
        if data.get("facet") != path.parent.name:
            lint.fail(str(rel), f"facet {data.get('facet')!r} does not match directory")

        data["_path"] = str(rel)
        nodes[node_id] = data
    return nodes


def check_completeness(lint: Lint, nodes: dict[str, dict]) -> None:
    for node_id, node in nodes.items():
        where = node["_path"]

        # C1: the three things a node needs to be applicable by someone who did not write it.
        definition = (node.get("definition") or "").strip()
        if not definition:
            lint.fail(where, "no definition")
        elif len(definition.split()) < 12:
            lint.fail(where, "definition is too short to discriminate (<12 words)")

        examples = node.get("examples") or []
        if len(examples) < 2:
            lint.fail(where, f"needs >=2 examples, has {len(examples)}")

        counters = node.get("counter_examples") or []
        if not counters:
            lint.fail(where, "needs >=1 counter-example")

        # C6: an example without a citation is an assertion; a counter-example without a reason
        # teaches nothing.
        # Presence is not substance. A `reason: bogus` satisfies a not-empty check and teaches
        # nothing; this caught real test residue that had survived a botched revert.
        def thin(value: str | None, min_words: int) -> bool:
            return len((value or "").split()) < min_words

        for i, ex in enumerate(examples):
            if not (ex.get("source") or "").strip():
                lint.fail(where, f"example[{i}] has no source")
            if thin(ex.get("text"), 3):
                lint.fail(where, f"example[{i}] text is too thin to be an act (<3 words)")
        for i, ce in enumerate(counters):
            if thin(ce.get("reason"), 6):
                lint.fail(where, f"counter_example[{i}] reason is too thin (<6 words)")
            # C3: the redirect has to land somewhere real, and somewhere ELSE. A "counter-example"
            # that resolves back to this node is not a counter-example; it is a near miss, and it
            # belongs in the field below where it will not be read as a boundary.
            correct = ce.get("correct")
            if not correct:
                lint.fail(where, f"counter_example[{i}] has no `correct` target")
            elif correct not in nodes:
                lint.fail(where, f"counter_example[{i}] points at unknown node {correct!r}")
            elif correct == node_id:
                lint.fail(
                    where,
                    f"counter_example[{i}] redirects to itself — move it to `near_misses`",
                )

        # C1b: near misses are optional, but a malformed one is worse than none. These are the
        # cases where the instinct is to reclassify and the correct answer is to stay put; they
        # carry no `correct` because the answer is this node.
        for i, nm in enumerate(node.get("near_misses") or []):
            if thin(nm.get("text"), 3):
                lint.fail(where, f"near_misses[{i}] text is too thin to be an act (<3 words)")
            if thin(nm.get("reason"), 6):
                lint.fail(where, f"near_misses[{i}] reason is too thin (<6 words)")
            if "correct" in nm:
                lint.fail(
                    where,
                    f"near_misses[{i}] must not carry `correct` — a near miss resolves to this node",
                )


def check_discriminators(lint: Lint, nodes: dict[str, dict]) -> None:
    """C4: for a flat closed facet, every node must say how it differs from every sibling.

    This is the check that would have caught the ambiguities E1 found in GCD: `create info` vs
    `create record` was unresolvable precisely because no source stated the discrimination.
    """
    by_facet: dict[str, list[str]] = {}
    for node_id, node in nodes.items():
        by_facet.setdefault(node["facet"], []).append(node_id)

    for facet, members in by_facet.items():
        for node_id in members:
            node = nodes[node_id]
            where = node["_path"]
            disc = node.get("discriminators") or {}
            siblings = {m for m in members if m != node_id}

            for named in disc:
                if named not in nodes:
                    lint.fail(where, f"discriminator names unknown node {named!r}")
                elif named not in siblings:
                    lint.fail(where, f"discriminator names {named!r}, which is not a sibling")

            for missing in sorted(siblings - set(disc)):
                lint.fail(where, f"no discriminator against sibling {missing!r}")

            for named, text in disc.items():
                if not (text or "").strip():
                    lint.fail(where, f"discriminator against {named!r} is empty")


def check_cardinality(lint: Lint, facets: dict, nodes: dict[str, dict]) -> None:
    """C5: a closed facet that has drifted from its declared size is a breaking change in disguise."""
    counts: dict[str, int] = {}
    for node in nodes.values():
        counts[node["facet"]] = counts.get(node["facet"], 0) + 1

    for facet in facets.get("facets") or []:
        fid = facet.get("id")
        declared = facet.get("cardinality")
        actual = counts.get(fid, 0)

        if facet.get("kind") == "closed" and declared is not None:
            # An EMPTY closed facet is work not yet started; a PARTIALLY populated one has drifted
            # from its declared size, which is a breaking change in disguise. Only the second is a
            # failure, so an unfinished registry does not sit red in CI and train people to ignore
            # it. The skip is reported, never silent.
            if actual == 0:
                lint.notice(
                    f"facet {fid!r} not yet populated (declares {declared} nodes) — phase 2 work"
                )
            elif actual != declared:
                lint.fail(
                    "taxonomy/facets.yaml",
                    f"facet {fid!r} declares cardinality {declared} but {actual} nodes exist",
                )
        elif actual == 0 and facet.get("status") != "provisional":
            lint.notice(f"facet {fid!r} has no nodes yet (status: {facet.get('status')})")


def gcd_act_grammar_tokens(schema: dict) -> set[str]:
    """Pull the vocabulary out of gcd's `acts` regex.

    gcd encodes the two axes asymmetrically: the five effects also appear as a JSON Schema `enum`
    on duty.effect, but the six state-kinds exist ONLY as alternation branches inside the acts
    pattern. A quoted-string search therefore reports every state-kind as missing, which is a bug in
    the checker rather than drift in either repo. Parse the alternations instead.
    """
    blob = json.dumps(schema)
    tokens: set[str] = set()
    for pattern in re.findall(r'"pattern"\s*:\s*"((?:[^"\\]|\\.)*)"', blob):
        if "observe" not in pattern:
            continue
        for group in re.findall(r"\(\?:([a-z|]+)\)", pattern):
            tokens.update(t for t in group.split("|") if t)
    return tokens


def check_gcd_alignment(lint: Lint, nodes: dict[str, dict]) -> None:
    """C7: the drift this whole registry exists to prevent, checked rather than asserted.

    Compares as SETS in both directions, so a value dropped from gcd and a value added to gcd
    without a registry node both fail. A one-way membership test would have caught neither.
    """
    if not GCD_SCHEMA.exists():
        lint.notice(f"C7 SKIPPED: {GCD_SCHEMA} not present (gcd repo not checked out)")
        return

    try:
        schema = json.loads(GCD_SCHEMA.read_text())
    except json.JSONDecodeError as exc:
        lint.fail("cross-repo/gcd", f"gcd.schema.json is unparseable: {exc}")
        return

    grammar = gcd_act_grammar_tokens(schema)
    if not grammar:
        lint.fail("cross-repo/gcd", "could not locate the acts grammar pattern in gcd.schema.json")
        return

    registry_wire: set[str] = set()
    for facet in ("effect", "state-kind"):
        members = [n["label"] for n in nodes.values() if n["facet"] == facet]
        if not members:
            lint.notice(f"C7 partial: facet {facet!r} not yet populated, so its side is unchecked")
            continue
        for label in members:
            wire = GCD_SPELLING.get(label, label)
            registry_wire.add(wire)
            if wire not in grammar:
                lint.fail(
                    "cross-repo/gcd",
                    f"registry has {facet} {label!r} (gcd spelling {wire!r}) "
                    "but gcd's acts grammar does not accept it",
                )

    # Only meaningful once both facets are populated; before that, every gcd token legitimately
    # lacks a registry node.
    both_populated = all(
        any(n["facet"] == f for n in nodes.values()) for f in ("effect", "state-kind")
    )
    if both_populated:
        for token in sorted(grammar - registry_wire):
            lint.fail(
                "cross-repo/gcd",
                f"gcd's acts grammar accepts {token!r} but the registry defines no node for it",
            )


def main() -> int:
    lint = Lint()
    facets = load_facets(lint)
    nodes = load_nodes(lint)

    if nodes:
        check_completeness(lint, nodes)
        check_discriminators(lint, nodes)
        check_gcd_alignment(lint, nodes)
    check_cardinality(lint, facets, nodes)

    for msg in lint.notices:
        print(f"notice: {msg}")

    if lint.errors:
        print(f"\n{len(lint.errors)} problem(s):", file=sys.stderr)
        for err in lint.errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    print(f"ok: {len(nodes)} nodes across {len({n['facet'] for n in nodes.values()})} facet(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
