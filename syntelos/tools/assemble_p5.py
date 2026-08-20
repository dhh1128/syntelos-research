#!/usr/bin/env python3
"""Union two independent extraction passes over the tefa archetype outlines into P5.

Two seats extract over the same files. Taking the union rather than an intersection deliberately
favours recall: over-recall is safe here because `verify_quotes.py` drops anything whose quote
cannot be reproduced from the source, so a hallucinated act cannot survive to the corpus. An
intersection would instead discard every real act that only one pass happened to notice.

Records which passes found each act. That is not bookkeeping for its own sake — an act found by
only one pass is weaker evidence about the archetype's action surface than one found by both, and
later stages may want to weight or report on it.

    python3 tools/assemble_p5.py out.jsonl pass-a.jsonl pass-b.jsonl [...]
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

FIELDS = ("text", "archetype", "source_file", "quote")


def load(path: pathlib.Path) -> list[dict]:
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
        if all(isinstance(rec.get(f), str) and rec[f].strip() for f in FIELDS):
            out.append(rec)
        else:
            skipped += 1
    print(f"  {path.name}: {len(out)} records, {skipped} non-record lines skipped")
    return out


def key(rec: dict) -> tuple[str, str]:
    """Dedupe within an archetype only. The same act under three roles is real signal."""
    text = re.sub(r"[^\w\s]", " ", rec["text"].lower())
    return rec["archetype"].strip().lower(), re.sub(r"\s+", " ", text).strip()


def main() -> int:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    out_path, inputs = pathlib.Path(sys.argv[1]), [pathlib.Path(p) for p in sys.argv[2:]]

    merged: dict[tuple[str, str], dict] = {}
    for path in inputs:
        tag = path.stem
        for rec in load(path):
            k = key(rec)
            if k in merged:
                # Keep the first pass's quote; record that this pass agreed.
                merged[k]["found_by"].append(tag)
            else:
                rec = {f: rec[f].strip() for f in FIELDS}
                rec["found_by"] = [tag]
                merged[k] = rec

    records = sorted(merged.values(), key=lambda r: (r["archetype"], r["text"]))
    for i, rec in enumerate(records, 1):
        rec["id"] = f"p5-{i:04d}"

    with open(out_path, "w") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")

    by_arch: dict[str, int] = {}
    both = 0
    for rec in records:
        by_arch[rec["archetype"]] = by_arch.get(rec["archetype"], 0) + 1
        if len(rec["found_by"]) > 1:
            both += 1

    print(f"\n{len(records)} distinct acts across {len(by_arch)} archetypes -> {out_path}")
    print(f"  found by >1 pass: {both} ({both * 100 // max(len(records), 1)}%)")
    for arch, n in sorted(by_arch.items()):
        print(f"    {arch:<24} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
