Extract a corpus of ACTS from the appended source files. This is a mechanical extraction task with a strict evidence rule. Output JSONL only — no prose, no preamble, no markdown fences.

## What an act is

An act is a verb applied to an object, at a granularity where a principal could plausibly permit or forbid it — the point at which someone deciding whether to delegate would want a say.

IN: "record a balanced journal entry", "revoke a vendor's access", "notify the supervisory authority of a breach", "hold and escalate an unmatched invoice", "decline a concession outside mandate".

OUT, and why:
- No verb. "Accounts payable", "controls and oracles" — a topic, not an act.
- Too fine. "Click the approve button", "open the file" — any policy about it is entirely subsumed by a policy about the larger act it serves.
- Too coarse. "Keep the books", "run compliance" — a whole role, not an act.
- A parameter variation. If two candidates differ only in a value ("approve a $500 invoice" / "approve a $5000 invoice"), emit one act ("approve an invoice") and not the variants.

Include acts that are REFUSALS, OMISSIONS, or ESCALATIONS — "decline an out-of-mandate concession", "hold a duplicate invoice", "refuse an unsupported conformance claim". These are first-class and are routinely missed.

## The evidence rule — this is the point of the task

Every act you emit MUST carry a verbatim quote from the source file it came from. The quote is checked mechanically against the file. If the quote cannot be found character-for-character (whitespace aside), the act is DROPPED.

So: copy the quote off the page. Do not tidy it, do not fix its grammar, do not merge two spans, do not paraphrase. Quote at least 6 words, and choose a span that actually contains the act — not a nearby heading.

An act you cannot quote is an act you should not emit. Emitting fewer, well-anchored acts is the correct behaviour; padding the list with plausible-sounding acts you cannot evidence is the failure mode this rule exists to catch.

## Output format

One JSON object per line, nothing else:

{"text": "record a balanced journal entry", "archetype": "bookkeeper", "source_file": "code/bakobo/tefa/research/archetypes/bookkeeper/raw/00-starter-outline.md", "quote": "per transaction: record the balanced journal entry with support"}

Fields:
- `text` — the act, normalised to lowercase verb + object. No trailing period.
- `archetype` — the directory name, exactly as it appears in the FILE marker.
- `source_file` — copy it exactly from the FILE marker line above the content.
- `quote` — verbatim span from that same file.

## Scope

Work through EVERY file in the appended material. Aim for 10–25 acts per archetype. Deduplicate within an archetype but NOT across archetypes — the same act appearing under three roles is a real signal and later stages need it.

## Do NOT classify

Do not add any category, type, effect, purpose, or taxonomy label to any act. Emit only the four fields above. Classification is a separate, blinded step, and pre-labelling this corpus would contaminate it.

=== SOURCE FILES FOLLOW ===
