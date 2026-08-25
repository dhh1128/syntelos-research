#!/usr/bin/env python3
"""Build the supplementary telos pool — the draw the first derivation should have had.

Two sampling faults produced the holes the stress cases found, and this fixes both.

The first was at the population level: `build_telos_sample.py` draws from P5, P8, P9 and P10, and
**P1 (Utah Code) and P2 (Civil Code of Québec) were never drawn from at all**. The two corpora
carrying arrest, seizure, prosecution, contract formation and settlement were acquired and then
left out, so `coerce` and `agree` could not have been found no matter how the passes behaved
(`design/telos-stress-cases.md` §6.1, §7.3).

The second was one level down, inside a population. Attempt 2 spread 400 P9 acts evenly across 23
SOC major groups, about 17 each. Even stratification is not neutral: it suppresses a domain that is
small in the population but distinct in kind, exactly as proportional sampling suppressed relational
acts in attempt 1. P9 holds 798 acts from arts and entertainment, 600 from personal care and
service, 291 from community and social service, and 521 from protective service — and effectively
none of that reached the derivation (§9).

**This draw is targeted and non-probability by construction**, and must be labelled as such
wherever it is reported. It is a coverage probe, not a frequency estimate: it asks what the corpus
contains that the twelve roots cannot express. Over-weighting a stratum cannot manufacture a
concept the corpus does not hold; it only stops even-stratification from hiding one. No frequency
claim may be computed from this pool — `telos-sample-2.jsonl` and the full pools remain the place
for that.

    python3 tools/build_telos_supp.py       # writes eval/corpora/telos-supp-sample.jsonl
"""
from __future__ import annotations

import collections
import json
import pathlib
import random
import sys

HOME = pathlib.Path.home()
ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED = 3249626741  # pre-registered; see eval/sampling-frame.md §4

P1 = ROOT / "eval/corpora/p1-utah-acts.jsonl"
P2 = ROOT / "eval/corpora/p2-ccq-acts.jsonl"
P9 = HOME / "code/bakobo/work-activities/corpus/acts.jsonl"
P10 = HOME / "code/bakobo/relational-acts/corpus/acts.jsonl"
P10D = HOME / "code/bakobo/relational-acts/corpus/delegated-relational.jsonl"

# SOC major groups over-weighted, and why each. The first three come from the back-test's brief;
# protective service is added because it is the one occupational home of applied force, and a
# second corpus with a different selection principle is the only way an act-family found in
# statute gets corroborated rather than merely repeated.
SOC_WEIGHTS = {
    "27": 55,  # arts, design, entertainment, sports, media
    "39": 45,  # personal care and service
    "21": 35,  # community and social service
    "33": 40,  # protective service
}
SOC_REST = 25  # thin cover of the remaining 18 major groups, so the batches are not all-specialist

CAPS = {"p1": 200, "p2": 150, "p10": 80, "p10d": 40}


def load(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        print(f"MISSING: {path}", file=sys.stderr)
        sys.exit(2)
    return [json.loads(l) for l in open(path) if l.strip()]


def stratified(rows: list[dict], n: int, key, rng: random.Random) -> list[dict]:
    """Take n rows round-robin across the values of `key` — proportional would reproduce the
    imbalance this exists to remove. Same routine as build_telos_sample.py, kept identical so the
    two draws differ only in what they are asked to cover."""
    if len(rows) <= n:
        return rows
    strata: dict[str, list[dict]] = collections.defaultdict(list)
    for r in rows:
        strata[str(key(r))].append(r)
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

    def take(tag: str, rows: list[dict], n: int, key) -> None:
        got = stratified(rows, n, key, rng)
        for r in got:
            picked.append({"id": r["id"], "text": r["text"].strip().rstrip("."), "pop": tag})
        report.append(f"  {tag:<6} {len(got):>4} of {len(rows):>6}")

    # P1 and P2 -- the acts that were never drawn. Stratify on the Utah title / CCQ article the act
    # came from, both source-native variables, so the draw spreads across the whole book rather
    # than clustering in whichever chapters the extractor found richest.
    take("p1", load(P1), CAPS["p1"], lambda r: r["cite"].split("§")[-1].split("-")[0])
    take("p2", load(P2), CAPS["p2"], lambda r: r["cite"].split()[-1].split(".")[0][:1])

    # P9, over-weighted by SOC major group.
    p9 = [r for r in load(P9) if r.get("level") == "task"]
    for r in p9:
        r["soc_major"] = (r.get("soc") or "?")[:2]
    for major, n in sorted(SOC_WEIGHTS.items()):
        take(f"p9-{major}", [r for r in p9 if r["soc_major"] == major], n, lambda r: r.get("soc"))
    rest = [r for r in p9 if r["soc_major"] not in SOC_WEIGHTS]
    take("p9-rest", rest, SOC_REST, lambda r: r["soc_major"])

    # P10, retained for relational coverage.
    take("p10", load(P10), CAPS["p10"], lambda r: r.get("source", "?"))
    take("p10d", load(P10D), CAPS["p10d"], lambda r: r.get("role", "?"))

    rng.shuffle(picked)
    out = ROOT / "eval/corpora/telos-supp-sample.jsonl"
    with open(out, "w") as fh:
        for i, r in enumerate(picked, 1):
            r["sample_id"] = f"X{i:04d}"
            fh.write(json.dumps(r) + "\n")

    print("\n".join(report))
    print(f"\n{len(picked)} acts -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
