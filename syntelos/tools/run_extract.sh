#!/usr/bin/env bash
# Run a quote-anchored extraction across batches and engines.
#
# Sibling of run_batches.sh, and it inherits every hard-won default from it: stderr captured per
# output rather than discarded, max_tokens capped explicitly because OpenRouter reserves against
# the requested figure, PANEL_TIMEOUT raised from its 600s default, effort tuned per seat, success
# judged by a gate rather than by exit status, and one retry.
#
# Two things differ. The gate is jsonl_gate.py, since degenerate.py reads repeated JSON field
# names as a token loop. And one engine is `codex`, which bills against a separate quota from
# OpenRouter -- the reason it kept working when credits ran out mid-run -- and so gives the union
# a pass whose failure modes are not correlated with the panel's.
#
# Usage:  run_extract.sh <batch-dir> <out-dir> <prompt-file> <engine> [engine...]
#         engine is one of: codex | <panel-seat>:<effort>:<max_tokens>
set -u

BATCH_DIR="${1:?batch dir}"; shift
OUT_DIR="${1:?out dir}"; shift
PROMPT="${1:?prompt file}"; shift
ENGINES=("$@")
[ "${#ENGINES[@]}" -gt 0 ] || { echo "no engines given" >&2; exit 2; }

TOOLS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PANEL_TIMEOUT="${PANEL_TIMEOUT:-900}"
mkdir -p "$OUT_DIR"

for batch in "$BATCH_DIR"/tb-*; do
  b="$(basename "$batch")"
  for engine in "${ENGINES[@]}"; do
    tag="${engine%%:*}"
    out="$OUT_DIR/ex-$tag-${b#tb-}.jsonl"
    err="${out%.jsonl}.err"

    if [ -s "$out" ] && python3 "$TOOLS/jsonl_gate.py" --quiet "$out" 2>/dev/null; then
      echo "$(date +%H:%M:%S) SKIP  $(basename "$out") (already good)"
      continue
    fi

    for attempt in 1 2; do
      if [ "$tag" = codex ]; then
        # --skip-git-repo-check is required or it refuses to run outside a repo it trusts.
        nice -n 19 bash -c \
          "cat '$batch' | codex exec --skip-git-repo-check \"\$(cat '$PROMPT')\"" \
          > "$out" 2>"$err"
      else
        IFS=: read -r seat effort maxtok <<< "$engine"
        nice -n 19 bash -c \
          "cat '$batch' | panel -m $seat -o reasoning_effort $effort -o max_tokens $maxtok \"\$(cat '$PROMPT')\"" \
          > "$out" 2>"$err"
      fi

      if python3 "$TOOLS/jsonl_gate.py" --quiet "$out" 2>/dev/null; then
        echo "$(date +%H:%M:%S) OK    $(basename "$out") $(grep -c '^{' "$out") records (attempt $attempt)"
        break
      fi

      echo "$(date +%H:%M:%S) FAIL  $(basename "$out") attempt $attempt: $(grep -oE 'Error[^,]{0,90}' "$err" | head -1)"
      [ "$attempt" = 2 ] && echo "$(date +%H:%M:%S) GIVEUP $(basename "$out") -- see $err"
    done
  done
done

echo "$(date +%H:%M:%S) ALLDONE"
python3 "$TOOLS/jsonl_gate.py" "$OUT_DIR"/ex-*.jsonl 2>&1 | sort | sed 's/^/  /'
