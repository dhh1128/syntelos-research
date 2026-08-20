#!/usr/bin/env python3
"""Emit the contamination disqualification list from the registry.

Every act cited in a taxonomy node as an `example`, `counter_example`, or `near_miss` was used to
WRITE the definitions. Scoring a classifier on those items measures how well it memorised the
spec's own worked cases, not whether the definitions are applicable by a stranger. So they are
disqualified from the evaluation corpus (sampling-frame.md §7).

The list is generated rather than maintained, because it grows every time a node gains an example.
Regenerate at draw time; never cache it.

    python3 tools/disqualified.py            # human-readable
    python3 tools/disqualified.py --json     # for the eval harness
    python3 tools/disqualified.py --check FILE.jsonl
                                             # exit 1 if any drawn act is contaminated

The --check mode reads JSONL with a `text` field per record, which is the shape the V1 draw emits.
Matching is on normalised text: lowercased, punctuation stripped, whitespace collapsed. That is
deliberately loose — a false positive costs one re-draw, a false negative silently inflates the
headline accuracy figure.
"""
from __future__ import annotations

import argparse
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
CITED_FIELDS = ("examples", "counter_examples", "near_misses")


def normalise(text: str) -> str:
    """Loose match key. Tuned to over-catch rather than under-catch; see the module docstring."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def collect() -> list[dict]:
    """Every act text cited anywhere in the registry, with where it came from."""
    out: list[dict] = []
    for path in sorted(TAXONOMY.rglob("*.yaml")):
        if path.name == "facets.yaml":
            continue
        data = yaml.safe_load(path.read_text()) or {}
        node_id = data.get("id", str(path))
        for field in CITED_FIELDS:
            for item in data.get(field) or []:
                text = (item.get("text") or "").strip()
                if not text:
                    continue
                out.append(
                    {
                        "text": text,
                        "key": normalise(text),
                        "node": node_id,
                        "field": field,
                    }
                )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--check", metavar="FILE", help="JSONL of drawn acts to screen")
    args = ap.parse_args()

    cited = collect()

    if args.check:
        index: dict[str, dict] = {}
        for c in cited:
            index.setdefault(c["key"], c)

        hits = []
        drawn = 0
        with open(args.check) as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                drawn += 1
                rec = json.loads(line)
                key = normalise(rec.get("text", ""))
                if key in index:
                    hits.append((lineno, rec.get("text", ""), index[key]))

        for lineno, text, src in hits:
            print(
                f"CONTAMINATED line {lineno}: {text!r} "
                f"is cited by {src['node']} as {src['field']}",
                file=sys.stderr,
            )
        print(f"screened {drawn} drawn acts against {len(index)} cited acts; {len(hits)} hit(s)")
        return 1 if hits else 0

    if args.json:
        print(json.dumps(cited, indent=2))
    else:
        by_field: dict[str, int] = {}
        for c in cited:
            by_field[c["field"]] = by_field.get(c["field"], 0) + 1
            print(f"{c['node']:<34} {c['field']:<17} {c['text']}")
        print(
            f"\n{len(cited)} disqualified acts "
            + ", ".join(f"{v} {k}" for k, v in sorted(by_field.items()))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
