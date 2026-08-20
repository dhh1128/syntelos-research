#!/usr/bin/env python3
"""Verify that every extracted act is anchored in primary text.

The problem this solves: population P5's original inventory came from a model reading the tefa
archetype docs and reporting what it found. That is one remove from the source in a way the other
populations are not — the same contamination the sampling frame exists to prevent, sitting in its
largest population (sampling-frame.md §10).

The fix is not to trust a better model. It is to require that each extracted act carry a VERBATIM
quote from a named source file, and to check every quote mechanically. An act whose quote cannot be
reproduced is dropped, not softened — the quote-or-drop rule from `bakobo/id-law-kit`.

Input: JSONL, one act per line, with at least:
    {"text": "...", "source_file": "<path>", "quote": "<verbatim span from that file>"}

    python3 tools/verify_quotes.py acts.jsonl                  # report
    python3 tools/verify_quotes.py acts.jsonl --write-clean OUT # emit only verified acts

Matching normalises whitespace only. It does NOT normalise case, punctuation, or wording: a quote
that has been tidied is a quote that was not read off the page, which is exactly the failure being
screened for.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

REQUIRED = ("text", "source_file", "quote")


def squash(text: str) -> str:
    """Collapse whitespace, including the line wrapping that makes a quote span source lines."""
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("acts", help="JSONL of extracted acts")
    ap.add_argument("--root", default="/", help="base for relative source_file paths")
    ap.add_argument("--write-clean", metavar="OUT", help="write only verified acts here")
    ap.add_argument("--min-quote-words", type=int, default=4,
                    help="a quote too short to be distinctive is not evidence (default 4)")
    args = ap.parse_args()

    root = pathlib.Path(args.root).expanduser()
    cache: dict[str, str] = {}
    verified, failures = [], []

    with open(args.acts) as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                failures.append((lineno, "?", f"unparseable JSON: {exc}"))
                continue

            missing = [f for f in REQUIRED if not (rec.get(f) or "").strip()]
            if missing:
                failures.append((lineno, rec.get("text", "?"), f"missing field(s): {', '.join(missing)}"))
                continue

            quote = rec["quote"]
            if len(quote.split()) < args.min_quote_words:
                failures.append((lineno, rec["text"], f"quote too short (<{args.min_quote_words} words)"))
                continue

            path = root / rec["source_file"].lstrip("/")
            if str(path) not in cache:
                if not path.exists():
                    failures.append((lineno, rec["text"], f"source_file not found: {path}"))
                    cache[str(path)] = ""
                    continue
                cache[str(path)] = squash(path.read_text(errors="replace"))
            haystack = cache[str(path)]
            if not haystack:
                failures.append((lineno, rec["text"], f"source_file unreadable: {path}"))
                continue

            if squash(quote) in haystack:
                verified.append(rec)
            else:
                failures.append((lineno, rec["text"], "quote NOT FOUND in source_file"))

    for lineno, text, why in failures:
        print(f"DROP line {lineno}: {text!r} — {why}", file=sys.stderr)

    total = len(verified) + len(failures)
    print(f"verified {len(verified)}/{total} acts; {len(failures)} dropped")

    if args.write_clean:
        with open(args.write_clean, "w") as out:
            for rec in verified:
                out.write(json.dumps(rec) + "\n")
        print(f"wrote {len(verified)} verified acts to {args.write_clean}")

    # A run where everything failed almost certainly means a wrong --root, not a bad extraction.
    if total and not verified:
        print("nothing verified at all — check --root", file=sys.stderr)
        return 2
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
