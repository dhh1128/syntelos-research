#!/bin/bash
# Run the chunked telos clustering across batches and seats, robustly.
#
# Every default in the naive version of this loop was wrong in a way that cost a diagnosis:
#
#   stderr        was sent to /dev/null, so eleven HTTP 402s read as timeouts. Now captured
#                 per output and echoed on failure.
#   max_tokens    defaults to 65536, and OpenRouter RESERVES against that number rather than
#                 actual usage -- so a modest request 402s on a balance that could easily afford
#                 it. Capped explicitly, with room for reasoning tokens, which count against the
#                 same budget.
#   effort        must be tuned per seat, not globally: deepseek degenerated at medium and was
#                 clean at low; kimi was clean at medium.
#   timeout       PANEL_TIMEOUT is an env var, documented in the panel wrapper. The 600s default
#                 is not a hard limit.
#   success       was inferred from exit status, which a seat can return 0 on while emitting
#                 nothing. Every output is gated by degenerate.py and retried once.
#
# Usage:  run_batches.sh <batch-dir> <out-dir> <prompt-file>
set -u

BATCH_DIR="${1:?batch dir}"
OUT_DIR="${2:?out dir}"
PROMPT="${3:?prompt file}"
TOOLS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# seat:effort:max_tokens -- max_tokens must cover reasoning AND output. 16k is comfortable for a
# ~600-word answer from a reasoning model without reserving an absurd amount against the balance.
SEATS=("ds:low:16000" "kimi:medium:16000")

export PANEL_TIMEOUT="${PANEL_TIMEOUT:-900}"
mkdir -p "$OUT_DIR"

for batch in "$BATCH_DIR"/tb-*; do
  b="$(basename "$batch")"
  for spec in "${SEATS[@]}"; do
    IFS=: read -r seat effort maxtok <<< "$spec"
    out="$OUT_DIR/cl-$seat-${b#tb-}.md"
    err="${out%.md}.err"

    # Skip work already done and already passing the gate.
    if [ -s "$out" ] && python3 "$TOOLS/degenerate.py" --quiet "$out" 2>/dev/null; then
      echo "$(date +%H:%M:%S) SKIP  $(basename "$out") (already good)"
      continue
    fi

    for attempt in 1 2; do
      nice -n 19 bash -c \
        "cat '$batch' | panel -m $seat -o reasoning_effort $effort -o max_tokens $maxtok \"\$(cat '$PROMPT')\"" \
        > "$out" 2>"$err"

      if python3 "$TOOLS/degenerate.py" --quiet "$out" 2>/dev/null; then
        echo "$(date +%H:%M:%S) OK    $(basename "$out") $(wc -w < "$out") words (attempt $attempt)"
        break
      fi

      echo "$(date +%H:%M:%S) FAIL  $(basename "$out") attempt $attempt: $(grep -oE 'Error[^,]{0,90}' "$err" | head -1)"
      [ "$attempt" = 2 ] && echo "$(date +%H:%M:%S) GIVEUP $(basename "$out") -- see $err"
    done
  done
done

echo "$(date +%H:%M:%S) ALLDONE"
python3 "$TOOLS/degenerate.py" "$OUT_DIR"/cl-*.md 2>&1 | sort | sed 's/^/  /'
