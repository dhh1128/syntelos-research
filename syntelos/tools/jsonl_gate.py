#!/usr/bin/env python3
"""Gate an extraction output before it reaches an assembly step.

`degenerate.py` is the gate for prose, and it is the wrong gate for JSONL: the repeated field names
that every record must carry drive its trigram-repetition signal toward the ceiling, so a perfectly
good extraction can read as a token loop. What matters for JSONL is different and simpler — did the
seat emit parseable records with the required fields, or did it emit prose, an apology, a fenced
block, or nothing?

Failing an empty file is deliberate, for the same reason `degenerate.py` fails a short one: a seat
that timed out having emitted nothing is the commonest failure a gate sees, and reporting it as
"ok, nothing to complain about" is precisely the silent pass a gate exists to prevent.

    python3 tools/jsonl_gate.py --fields text,unit_id,cite,quote FILE...
    python3 tools/jsonl_gate.py --quiet --min 5 FILE          # exit code only
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys


def assess(text: str, fields: list[str]) -> tuple[int, int, bool]:
    """Return (valid records, unusable lines, truncated).

    `truncated` is the signature of a run that hit its token cap: the last non-empty line is an
    unterminated JSON object. It is worth detecting separately because such a file looks healthy —
    it is full of good records — while silently covering only part of its batch. The first run of
    this pipeline lost 48 of a 60-unit batch that way and the gate passed it.
    """
    good = junk = 0
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l and not l.startswith("```")]
    for line in lines:
        if not line.startswith("{"):
            junk += 1
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            junk += 1
            continue
        if all(isinstance(rec.get(f), str) and rec[f].strip() for f in fields):
            good += 1
        else:
            junk += 1

    truncated = False
    if lines:
        last = lines[-1]
        try:
            json.loads(last)
        except json.JSONDecodeError:
            truncated = last.startswith("{")
    return good, junk, truncated


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--fields", default="text,unit_id,cite,quote")
    ap.add_argument("--min", type=int, default=1, help="fewest valid records that counts as a run")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    fields = [f for f in args.fields.split(",") if f]
    any_bad = False
    for name in args.files:
        path = pathlib.Path(name)
        if not path.exists():
            print(f"MISSING {name}", file=sys.stderr)
            any_bad = True
            continue
        good, junk, cut = assess(path.read_text(errors="replace"), fields)
        # Junk alone does not condemn a file -- a seat that emits a stray sentence around good
        # records is recoverable, and the assembler already skips non-records. Too few records
        # condemns it, and so does a truncated tail, which means the batch was only partly covered.
        bad = good < args.min or cut
        any_bad |= bad
        if not args.quiet:
            verdict = "TRUNCATED" if cut else ("EMPTY" if bad else "ok")
            print(f"{verdict:<10} {path.name:<24} records={good} unusable={junk}")
    return 1 if any_bad else 0


if __name__ == "__main__":
    sys.exit(main())
