#!/usr/bin/env python3
"""Union independent extraction passes over the same sources into one act corpus.

Written for P5 (two seats over the tefa archetype outlines) and generalised for P1/P2 (two engines
over drawn statutory units), which want the same discipline and differ only in which field an act
is deduplicated within.

Taking the union rather than an intersection deliberately favours recall: over-recall is safe here
because `verify_quotes.py` drops anything whose quote cannot be reproduced from the source, so a
hallucinated act cannot survive to the corpus. An intersection would instead discard every real act
that only one pass happened to notice.

Records which passes found each act. That is not bookkeeping for its own sake — an act found by
only one pass is weaker evidence than one found by both, and later stages may want to weight or
report on it.

    python3 tools/assemble_acts.py out.jsonl pass-a.jsonl pass-b.jsonl [...]          # P5 defaults
    python3 tools/assemble_acts.py --fields text,unit_id,cite,quote --group unit_id \\
        --prefix p1 out.jsonl ex-*.jsonl

Dedupe is WITHIN the group field only. The same act appearing under three archetypes, or in three
statutory sections, is real signal and must not be collapsed.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys


def load(path: pathlib.Path, fields: list[str]) -> list[dict]:
    """Read JSONL, tolerating the markdown fences and stray prose models wrap output in."""
    out, skipped = [], 0
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("```"):
            continue
        if not line.startswith("{"):
            skipped += 1
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            skipped += 1
            continue
        if all(isinstance(rec.get(f), str) and rec[f].strip() for f in fields):
            out.append(rec)
        else:
            skipped += 1
    print(f"  {path.name}: {len(out)} records, {skipped} non-record lines skipped")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("out")
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--fields", default="text,archetype,source_file,quote")
    ap.add_argument("--group", default="archetype", help="dedupe within this field only")
    ap.add_argument("--prefix", default="p5", help="id prefix for the assembled corpus")
    ap.add_argument("--const", action="append", default=[], metavar="K=V",
                    help="stamp a constant field on every record, e.g. source_file=<path>. A "
                         "field that is the same for every act in a population is assembly's job "
                         "to add, not the extractor's to repeat on every line.")
    args = ap.parse_args()

    consts = dict(kv.split("=", 1) for kv in args.const)

    fields = [f for f in args.fields.split(",") if f]
    if args.group not in fields:
        print(f"--group {args.group} is not among --fields", file=sys.stderr)
        return 2

    merged: dict[tuple[str, str], dict] = {}
    for path in [pathlib.Path(p) for p in args.inputs]:
        tag = path.stem
        for rec in load(path, fields):
            text = re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", rec["text"].lower())).strip()
            k = (rec[args.group].strip().lower(), text)
            if k in merged:
                # Keep the first pass's quote; record that this pass agreed.
                merged[k]["found_by"].append(tag)
            else:
                clean = {f: rec[f].strip() for f in fields}
                clean.update(consts)
                clean["found_by"] = [tag]
                merged[k] = clean

    records = sorted(merged.values(), key=lambda r: (r[args.group], r["text"]))
    for i, rec in enumerate(records, 1):
        rec["id"] = f"{args.prefix}-{i:04d}"

    with open(args.out, "w") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")

    by_group: dict[str, int] = {}
    both = 0
    for rec in records:
        by_group[rec[args.group]] = by_group.get(rec[args.group], 0) + 1
        if len(rec["found_by"]) > 1:
            both += 1

    print(f"\n{len(records)} distinct acts across {len(by_group)} {args.group} values -> {args.out}")
    print(f"  found by >1 pass: {both} ({both * 100 // max(len(records), 1)}%)")
    if len(by_group) <= 30:
        for g, n in sorted(by_group.items()):
            print(f"    {g:<24} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
