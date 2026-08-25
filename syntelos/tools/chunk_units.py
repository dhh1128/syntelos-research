#!/usr/bin/env python3
"""Split a units file into batches a seat can hold in one call.

The lesson from the first clustering run, recorded in `design/STATE.md`: payload size is the
dominant variable in whether a seat returns something usable. A 150-item batch comes back in
50-150s; a 1,076-item pool times out. So the units get chunked before they go anywhere near a
model, and the chunk boundary is a unit boundary — never mid-unit, since an act must be quotable
from what the extractor actually saw.

    python3 tools/chunk_units.py eval/corpora/sources/p1-units.txt /tmp/p1-batches 60
"""
from __future__ import annotations

import pathlib
import re
import sys


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__.strip().splitlines()[-1].strip(), file=sys.stderr)
        return 2
    src, out_dir, per = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), int(sys.argv[3])

    # A unit starts at its `[id] cite — heading` marker and runs to the next marker.
    text = src.read_text()
    parts = re.split(r"(?m)^(?=\[[a-z0-9]+-\d{4}\] )", text)
    units = [p for p in parts if p.strip()]

    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("tb-*"):
        old.unlink()

    n = 0
    for i in range(0, len(units), per):
        batch = units[i:i + per]
        path = out_dir / f"tb-{i // per:02d}"
        path.write_text("".join(batch))
        print(f"  {path.name}: {len(batch)} units, {path.stat().st_size // 1024} KB")
        n += len(batch)

    print(f"{n} units -> {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
