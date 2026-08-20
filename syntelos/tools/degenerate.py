#!/usr/bin/env python3
"""Detect degenerate model output before it reaches an analysis.

Written after a run that looked like the best of three arms on every cheap metric — fastest at 50
seconds, longest at 1,730 words — and was 1,730 words of "in? in? in?". Word count and latency are
not just weak quality proxies here; they are inverted ones, because a model collapsed into a token
loop emits faster and longer than one that is thinking.

Three signals, any of which condemns:

  vocab      unique words / total words. Healthy prose sits well above 0.25; a token loop collapses
             toward zero.
  repeat     the most frequent trigram's share of all trigrams. Loops spike this.
  runlen     longest run of consecutive identical words.

    python3 tools/degenerate.py FILE...          # report, exit 1 if any file is degenerate
    python3 tools/degenerate.py --quiet FILE     # exit code only
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

VOCAB_FLOOR = 0.18
REPEAT_CEIL = 0.04
RUNLEN_CEIL = 6
MIN_WORDS = 40


def assess(text: str) -> tuple[bool, dict]:
    words = re.findall(r"\w+", text.lower())
    if len(words) < MIN_WORDS:
        return False, {"words": len(words), "note": "too short to judge"}

    vocab = len(set(words)) / len(words)

    trigrams = collections.Counter(zip(words, words[1:], words[2:]))
    repeat = (trigrams.most_common(1)[0][1] / max(len(words) - 2, 1)) if trigrams else 0.0

    runlen = best = 1
    for a, b in zip(words, words[1:]):
        runlen = runlen + 1 if a == b else 1
        best = max(best, runlen)

    bad = vocab < VOCAB_FLOOR or repeat > REPEAT_CEIL or best > RUNLEN_CEIL
    return bad, {"words": len(words), "vocab": round(vocab, 3),
                 "repeat": round(repeat, 4), "runlen": best}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    any_bad = False
    for name in args.files:
        path = pathlib.Path(name)
        if not path.exists():
            print(f"MISSING {name}", file=sys.stderr)
            any_bad = True
            continue
        bad, m = assess(path.read_text(errors="replace"))
        any_bad |= bad
        if not args.quiet:
            verdict = "DEGENERATE" if bad else "ok"
            detail = " ".join(f"{k}={v}" for k, v in m.items())
            print(f"{verdict:<11} {path.name:<24} {detail}")
    return 1 if any_bad else 0


if __name__ == "__main__":
    sys.exit(main())
