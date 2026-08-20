You are doing bottom-up taxonomy derivation. Appended is a list of 1,076 real acts, each with an id, harvested from software protocols, agent tool definitions, and organisational role descriptions. They are shuffled and unlabelled by source.

## Task

Derive, **from this corpus alone**, a set of root categories that partition these acts by their **telos** — the purpose the act serves, the outcome that is its reason for existing. Not what the act mechanically does; what it is *for*.

Constraints on the partition:

- **Between 5 and 12 roots.** Fewer than 5 is uninformative; more than 12 stops being a root level.
- **Mutually exclusive.** Every act belongs to exactly one root. If you find yourself wanting two, the roots are wrong — say so and fix them rather than allowing overlap.
- **Collectively exhaustive over this corpus.** Every act must land somewhere. Acts you genuinely cannot place go in an explicit `UNPLACEABLE` bucket with a reason — do not force them.
- **Roots must be ULTIMATE purposes, not proximate ones.** This is the screen most likely to be
  missed. A purpose that is always a means to some further end is not a root, however common it is
  in the corpus. Test: strip the candidate away and ask whether an end remains. "Represent a
  client's interests" fails — the end is whatever is being represented *toward*, and representation
  is a standing relation the actor holds rather than a phase of activity with its own completion.
  "Coordinate a meeting" passes, because the coordinating phase completes on its own terms before
  whatever the meeting is for begins. Standing relations between actors are NOT purposes; if a
  candidate root describes *on whose behalf* or *in what capacity* an actor works, it belongs on a
  different axis and must be excluded here.
- **Roots must be purposes, not mechanisms.** "Read operations" is a mechanism. "Reduce informational asymmetry" is a purpose. This distinction is the whole exercise.
- Name each root with a single lowercase verb or verbal noun, kebab-case if needed.

## Method you should follow

1. Read the whole corpus before proposing anything. Do not partition the first fifty and extrapolate.
2. Group by what the act is FOR, letting the groups emerge from the acts rather than from categories you already know.
3. Where a group is very large, ask whether it is really one purpose or several that share a mechanism. Where a group is tiny, ask whether it is a genuine root or a stray.
4. State, for each root, the **discriminating question** that separates it from its nearest neighbour. If you cannot state one, the two roots should be merged.

## Output

Markdown, in this order:

**A. The partition.** For each root: name, a two-sentence definition, the discriminating question against its nearest neighbour, the count of acts assigned, and five representative act ids with their text.

**B. Unplaceable.** Any act you could not assign, with the reason.

**C. Stress points.** The ten acts that were hardest to place, each with the two roots that competed and why the corpus did not settle it. Be adversarial about your own partition here — this section is worth more than section A.

**D. What the corpus is missing.** Purposes you would expect a general taxonomy of acts to need, but which no act in this corpus exercises. This tells the reader what the corpus cannot prove.

## Critical instruction

**Derive the partition from the corpus.** Do not retrieve a taxonomy you already know and fit the acts to it. If you find yourself reaching for a standard set of categories, set it aside and work from the acts. Where your partition does end up resembling something standard, that is fine — but it must be because the acts drove it, and you should say so in section E rather than in section A.

Do NOT emit any per-act assignment table. Assignment is a separate later step; producing one here is the single most common way this task runs out of time before the partition is finished. Sections A-D are prose and should be dense.

=== THE 1,076 ACTS FOLLOW ===
