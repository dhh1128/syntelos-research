Extract a corpus of ACTS from the appended statutory units. This is a mechanical extraction task
with a strict evidence rule. Output JSONL only — no prose, no preamble, no markdown fences.

## What you are reading

Each unit is one section of a statute or one article of a code, shown as:

    [unit-id] citation — heading
    body text, truncated

A statute does not list acts. It states **norms about acts**: it permits, requires, forbids,
conditions, or attaches a consequence to something a person or a body does. Your job is to recover
the act the provision is about, stated plainly.

So `"The department may revoke or suspend the registration"` yields `revoke a registration` and
`suspend a registration`. The deontic status — may, shall, may not, is guilty of — is **not** part
of the act and must be stripped: extract the act itself, whether the provision authorises it,
compels it, or prohibits it.

Acts performed by officials, courts, agencies and public bodies count exactly as much as acts
performed by private parties. Extract both.

## What an act is

An act is a verb applied to an object, at a granularity where a principal could plausibly permit
or forbid it — the point at which someone deciding whether to delegate would want a say.

IN: "file a financing statement", "issue a licence", "record a lien", "convey property",
"appoint a director", "notify an affected owner", "post a bond".

OUT, and why:
- No verb. "Definitions", "Short title", "Scope of chapter" — a topic, not an act.
- A state of affairs rather than a doing. "Property is deemed abandoned", "the term expires" —
  nothing is done by anyone.
- A status rather than an act. "Be a licensed contractor" is a standing, not an act; if the unit
  names the act that constitutes or maintains it, emit that instead, and otherwise emit nothing.
- Too fine. "Sign the bottom of the form" — any policy about it is entirely subsumed by a policy
  about the larger act it serves.
- Too coarse. "Administer this chapter", "regulate the industry" — a whole mandate, not an act.
- A parameter variation. If two candidates differ only in a value ("file within 30 days" / "file
  within 60 days"), emit one act ("file") and not the variants.

Include acts that are REFUSALS, OMISSIONS, or ESCALATIONS — "decline an application", "withhold a
record", "refer a matter for further proceedings". These are first-class and are routinely missed.

## Many units name no act at all, and that is the expected result

A statute book spends much of its length on definitions, titles, scope clauses, findings,
appropriations, effective dates, severability, and statements of consequence. **Roughly half of
these units should yield zero acts.** Emitting nothing for such a unit is the correct behaviour and
is being measured; padding the list with an invented act so that every unit contributes is the
failure mode this instruction exists to prevent.

Where a unit does name acts, one to four is typical. A unit whose heading joins several subjects
with `--` may well carry one act per subject.

## The evidence rule — this is the point of the task

Every act you emit MUST carry a verbatim quote from the unit it came from, as that unit appears
below. The quote is checked mechanically. If the quote cannot be found character-for-character
(whitespace aside), the act is DROPPED.

So: copy the quote off the page. Do not tidy it, do not fix its grammar, do not merge two spans, do
not paraphrase, do not repair a sentence the truncation cut short. Quote at least 6 words, and
choose a span that actually contains the act.

An act you cannot quote is an act you should not emit.

## Output format

One JSON object per line, nothing else:

{"text": "revoke a pesticide registration", "unit_id": "p1-0005", "cite": "Utah Code §4-14-108", "quote": "The department may revoke or suspend the registration of a pesticide"}

Fields:
- `text` — the act, normalised to lowercase verb + object. No trailing period. No modal, no actor.
- `unit_id` — copy it exactly from the `[...]` marker of the unit.
- `cite` — copy it exactly from the same marker line.
- `quote` — verbatim span from that unit's text.

## Scope

Work through EVERY unit in the appended material, in order. Deduplicate within a unit but NOT
across units — the same act appearing in three sections is a real signal and later stages need it.

## Do NOT classify

Do not add any category, type, purpose, effect, or taxonomy label to any act, and do not group the
output. Emit only the four fields above. Classification is a separate, blinded step, and
pre-labelling this corpus would contaminate it.

=== UNITS FOLLOW ===
