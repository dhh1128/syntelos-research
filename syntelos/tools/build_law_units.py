#!/usr/bin/env python3
"""Draw the P1 and P2 sampling units, so that acts can be extracted from them.

P5, P8, P9 and P10 all ship an `acts.jsonl`; P1 (Utah Code) and P2 (Civil Code of Québec) ship
raw law. Nothing had ever been drawn from them, which is the traceable cause of the two missing
telos roots (`telos-stress-cases.md` §6.1, §7.3). This is the first half of closing that: it draws
the units, and a separate extraction pass turns units into acts.

Two commitments from `eval/sampling-frame.md` are honoured here rather than asserted:

  §4  Systematic sampling with a random start, on the population's native order, at interval
      k = ceil(N / n_draw), start = seed mod k, with the seed pre-registered at 3249626741. The
      codes are ordered by subject, so a systematic draw spreads across the whole book; simple
      random sampling would not guarantee that.

  §1  Screening happens AFTER sampling. So this script does NOT filter to act-shaped units. A
      catchline reading "Definitions" is drawn like any other and is screened out downstream by
      the extractor emitting no act for it — which makes the screen-out rate a measurable result
      (E4 estimated 35-45% of headings are act-shaped) rather than an invisible filter.

The units are written twice on purpose. The `.txt` file is the **source of record for quote
verification**: extracted acts cite it in `source_file`, and `tools/verify_quotes.py` checks each
quote against it character-for-character. The `.jsonl` is the machine index. Writing the drawn
text to a file, rather than pointing at the gzipped original, is what lets a quote be verified
against exactly the bytes the extractor saw.

    python3 tools/build_law_units.py            # writes eval/corpora/sources/p{1,2}-*.{txt,jsonl}
"""
from __future__ import annotations

import gzip
import json
import math
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

HOME = pathlib.Path.home()
ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED = 3249626741  # pre-registered; see eval/sampling-frame.md §4

UTAH_DIR = HOME / "code/bakobo/utah-id-law/corpus/utah-code"
CCQ_GZ = HOME / "code/bakobo/civil-law-acts/corpus/CCQ-1991-en.txt.gz"

# Over-draw against the ~40% act-shaped estimate. The target is ~200 P1 acts and ~150 P2 acts for
# the supplementary derivation pool; the CCQ is denser in juridical acts per unit than a statute
# book that spends much of its length on definitions and appropriations, hence the smaller draw.
P1_DRAW = 500
P2_DRAW = 300

# How much of a unit's body accompanies its heading. A catchline alone is often unextractable --
# "Penalties" names no act -- and the coercive and contractual acts this pass exists to find live
# in the body text, not the heading. Truncation keeps the payload inside a seat's comfortable
# batch size; a truncated body can still anchor a quote, since the quote must come from what was
# actually shown.
BODY_CHARS = 260


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def utah_sections() -> list[dict]:
    """Every <section> in the Utah Code, in the book's native title/chapter/part/section order."""

    def title_key(path: pathlib.Path) -> tuple:
        m = re.match(r"C(\d+)([A-Z]*)", path.name)
        return (int(m.group(1)), m.group(2)) if m else (999, path.name)

    out: list[dict] = []
    for path in sorted(UTAH_DIR.glob("*.xml.gz"), key=title_key):
        try:
            tree = ET.fromstring(gzip.open(path).read().decode("utf-8", errors="replace"))
        except ET.ParseError as exc:
            print(f"  SKIP {path.name}: {exc}", file=sys.stderr)
            continue
        for sec in tree.iter("section"):
            catchline, body = "", []
            for child in sec:
                if child.tag == "catchline":
                    catchline = squash("".join(child.itertext()))
                    if child.tail:
                        body.append(child.tail)
                elif child.tag == "histories":
                    if child.tail:
                        body.append(child.tail)
                else:
                    body.append("".join(child.itertext()))
                    if child.tail:
                        body.append(child.tail)
            out.append({
                "cite": f"Utah Code §{sec.get('number') or '?'}",
                "heading": catchline,
                "body": squash("".join(body)),
            })
    return out


def ccq_articles() -> list[dict]:
    """Every article of the CCQ, in numeric order as the code prints them.

    The corpus item is a text extraction of LégisQuébec's markup, in which each article is
    introduced by a `## Article N` line and runs to the next heading of any level.
    """
    text = gzip.open(CCQ_GZ).read().decode("utf-8", errors="replace")
    lines = text.splitlines()
    out: list[dict] = []
    cur: dict | None = None
    for line in lines:
        m = re.match(r"^##\s+Article\s+(\S+)\s*$", line)
        if m:
            if cur:
                out.append(cur)
            cur = {"cite": f"CCQ art. {m.group(1)}", "heading": "", "_buf": []}
            continue
        if cur is None:
            continue
        if line.startswith("#"):
            out.append(cur)
            cur = None
            continue
        cur["_buf"].append(line)
    if cur:
        out.append(cur)
    for r in out:
        r["body"] = squash(" ".join(r.pop("_buf")))
    return [r for r in out if r["body"]]


def systematic(rows: list[dict], n: int) -> list[dict]:
    """Take n rows at interval k with the start fixed by the pre-registered seed."""
    if len(rows) <= n:
        return rows
    k = math.ceil(len(rows) / n)
    start = SEED % k
    return [rows[i] for i in range(start, len(rows), k)][:n]


def emit(tag: str, rows: list[dict], population: int) -> None:
    src_dir = ROOT / "eval/corpora/sources"
    src_dir.mkdir(parents=True, exist_ok=True)
    txt_path = src_dir / f"{tag}-units.txt"
    rel = txt_path.relative_to(ROOT.parent)

    lines, index = [], []
    for i, r in enumerate(rows, 1):
        uid = f"{tag}-{i:04d}"
        body = r["body"][:BODY_CHARS]
        lines.append(f"[{uid}] {r['cite']} — {r['heading']}\n{body}\n")
        index.append({"unit_id": uid, "cite": r["cite"], "heading": r["heading"],
                      "body": body, "source_file": str(rel)})

    txt_path.write_text("\n".join(lines))
    with open(src_dir / f"{tag}-units.jsonl", "w") as fh:
        for rec in index:
            fh.write(json.dumps(rec) + "\n")

    k = math.ceil(population / len(rows)) if len(rows) < population else 1
    print(f"  {tag}: {len(rows)} units drawn from {population} "
          f"(k={k}, start={SEED % k if k > 1 else 0}) -> {txt_path.name}, "
          f"{txt_path.stat().st_size // 1024} KB")


def main() -> int:
    for path in (UTAH_DIR, CCQ_GZ):
        if not path.exists():
            print(f"MISSING: {path}", file=sys.stderr)
            return 2

    p1 = utah_sections()
    p2 = ccq_articles()
    print(f"populations: P1 {len(p1)} sections, P2 {len(p2)} articles")
    emit("p1", systematic(p1, P1_DRAW), len(p1))
    emit("p2", systematic(p2, P2_DRAW), len(p2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
