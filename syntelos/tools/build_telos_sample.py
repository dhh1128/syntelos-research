#!/usr/bin/env python3
"""Build a domain-balanced sample for deriving the telos facet.

Attempt 1 failed because the pool answered the wrong question. Fed acts in their natural
proportions, a partition tracks FREQUENCY: 39% of that pool was read-operations, so `discovering`
swallowed 241 of 621 acts, and any domain thin on the ground would have been merged away regardless
of whether it names a distinct purpose.

Structure and frequency are different questions and want different samples. This builds the
structure sample: capped per population and stratified within, so that no domain drives the
partition by sheer mass. Frequency is then reported separately from the full pool, where it is
actually meaningful.

This is NOT a thumb on the scale for any particular root. The seats still see an unlabelled,
shuffled list and derive whatever the acts support. What balancing removes is the sampling artefact
that would decide the outcome before they look.

    python3 tools/build_telos_sample.py            # writes eval/corpora/telos-sample-2.jsonl
"""
from __future__ import annotations

import collections
import json
import pathlib
import random
import re
import sys

HOME = pathlib.Path.home()
ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED = 3249626741  # pre-registered; see eval/sampling-frame.md §4

# Per-population cap and the field to stratify on within it. Caps are set so that no population
# exceeds ~40% of the sample; P9's 19,898 would otherwise be 95% of everything.
SOURCES = [
    ("p5", ROOT / "eval/corpora/p5-steward-acts.jsonl", 176, "archetype"),
    ("p8", HOME / "code/bakobo/interaction-acts/corpus/acts.jsonl", 200, "source"),
    ("p9", HOME / "code/bakobo/work-activities/corpus/acts.jsonl", 400, "soc_major"),
    ("p10", HOME / "code/bakobo/relational-acts/corpus/acts.jsonl", 180, "source"),
    ("p10d", HOME / "code/bakobo/relational-acts/corpus/delegated-relational.jsonl", 120, "role"),
]


def stratified(rows: list[dict], n: int, key: str, rng: random.Random) -> list[dict]:
    """Take n rows spread as evenly as possible across the values of `key`.

    Round-robin over shuffled strata rather than proportional allocation: proportional would
    reproduce the imbalance this function exists to remove.
    """
    if len(rows) <= n:
        return rows
    strata: dict[str, list[dict]] = collections.defaultdict(list)
    for r in rows:
        strata[str(r.get(key, "?"))].append(r)
    for v in strata.values():
        rng.shuffle(v)

    out: list[dict] = []
    order = sorted(strata)
    while len(out) < n:
        progressed = False
        for k in order:
            if strata[k]:
                out.append(strata[k].pop())
                progressed = True
                if len(out) >= n:
                    break
        if not progressed:
            break
    return out


def main() -> int:
    rng = random.Random(SEED)
    picked: list[dict] = []
    report: list[str] = []

    for tag, path, cap, key in SOURCES:
        if not path.exists():
            print(f"MISSING: {path}", file=sys.stderr)
            return 2
        rows = [json.loads(l) for l in open(path) if l.strip()]

        # P9 carries a SOC code; derive its major group so stratification spreads across
        # occupational domains (healthcare, construction, education, sales) rather than across
        # individual job titles, of which there are 923.
        if tag == "p9":
            for r in rows:
                r["soc_major"] = (r.get("soc") or "?")[:2]
            # The DWA and task layers describe the same work twice (frame §2), so restrict to one
            # layer for structure derivation; tasks carry the occupational spread.
            rows = [r for r in rows if r.get("level") == "task"] or rows

        take = stratified(rows, cap, key, rng)
        for r in take:
            picked.append({"text": r["text"].strip().rstrip("."), "pop": tag})
        report.append(f"  {tag:<5} {len(take):>4} of {len(rows):>6} (stratified on {key})")

    rng.shuffle(picked)
    out = ROOT / "eval/corpora/telos-sample-2.jsonl"
    with open(out, "w") as fh:
        for i, r in enumerate(picked, 1):
            r["sample_id"] = f"S{i:04d}"
            fh.write(json.dumps(r) + "\n")

    print("\n".join(report))
    print(f"\n{len(picked)} acts -> {out}")

    # The probe that condemned attempt 1's pool, re-run so the balance is visible rather than
    # asserted. Substring artefacts are known and noted in the frame; these are raw counts.
    probes = {
        "care": r"\b(treat|diagnos|nurs|patient|medicat|therap)",
        "serve": r"\b(repair|install|clean|construct|manufactur|harvest)",
        "relate": r"\b(befriend|follow|invite|celebrat|introduc|match|block|congratulat)",
        "trade": r"\b(sell|purchase|price|negotiat)",
        "teach": r"\b(teach|tutor|lecture|instruct|coach)",
        "observe": r"\b(get|list|read|search|fetch|retriev|query|view|monitor|inspect)",
    }
    texts = [r["text"] for r in picked]
    print()
    for label, pat in probes.items():
        hits = [t for t in texts if re.search(pat, t, re.I)]
        pct = 100 * len(hits) / max(len(texts), 1)
        print(f"  {label:<8} {len(hits):>4}  {pct:4.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
