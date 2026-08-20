# The rating protocol

Draft 2026-08-20. How the gold standard gets built, given one human rater now and possibly a second
later. Companion to `sampling-frame.md`, which fixes *what* is rated; this fixes *who* rates it,
*what they record*, and *what may be claimed* from the result.

The constraint that shapes everything here: **a second human rater is wanted but must not be a
dependency.** The design below yields a defensible result with one human, and admits a second later
as pure addition — no re-rating, no invalidated figures, no re-drawn sample.

## 1. Roles

- **Reference rater — Daniel.** One pass over the full 600-act gold subsample. These labels are the
  criterion the model raters are scored against.
- **Model raters — ≥5 models × ≥3 seeds.** Scored against the reference; also measured against each
  other.
- **Second human — deferred, unscheduled.** Rates the sealed ceiling subsample (§5) whenever they
  arrive. Nothing waits on this.

## 2. Call it concordance, not accuracy

With a single human, "accuracy" would mean "agreement with Daniel" — and Daniel is the taxonomy's
author. That measures whether a model can reproduce the author's intent, which is a real and
publishable question but is **not** the question "is this taxonomy applicable by a stranger."

So the headline metric is **concordance with the reference rater**, stated that way in every table
and every sentence, with the author-rater confound named at first use. A figure called accuracy
would be quietly claiming something the design cannot support, and a reviewer would be right to say
so.

This is the single largest thing the second human buys back, and §6 says what changes when they
land.

## 3. The substitute that does not wait: intra-rater reliability

There is a cheap measurement available now that bounds part of the problem, and it needs nobody.

**Daniel re-rates 60 items, drawn from the 600, after a gap of at least two weeks, blind to his
first labels.** Item order re-randomised; original labels not consulted.

That yields **test–retest reliability** — how stably the reference rater applies the definitions to
the same item twice. It matters because it puts a floor under the interpretation of every
model figure: if the reference rater agrees with himself at α = 0.75 on `state-kind`, then a model
scoring 0.72 against him is at the noise floor of the criterion, and reporting that as a model
deficiency would be wrong.

It does not substitute for a second human — self-agreement measures stability, not
intersubjectivity, and an author can be stably idiosyncratic. But it is the difference between a
model figure that can be interpreted and one that cannot, and it costs 60 items.

Do the re-rate **before** the model runs are analysed, so the floor is known in advance rather than
discovered when it would be convenient.

## 4. What a rater records per item

Identical instrument for humans and models, or the comparison is invalid.

| Field | Values | Notes |
|---|---|---|
| `effect` | multi-select of the 5 | An act may occupy several cells |
| `state_kind` | multi-select of the 6 | Paired with effect; neither is meaningful alone |
| `modality` | one of `may` / `must` / `must-not` | |
| `granularity` | `in-scope` / `too-fine` / `too-coarse` | Tests the rule sharpened in the frame |
| `abstain` | boolean, plus free-text reason | See below |
| `confidence` | 1–5 | Feeds the calibration work in V3 |
| `notes` | free text | Where a definition felt wrong — the raw material for V4 |

**Abstention is a first-class response, not a failure.** Custos makes refusal normatively correct —
missing vocabulary yields a refusal naming what is absent, rather than a guess — so the instrument
must offer it, and V3's risk–coverage curves depend on it. A rater who abstains on 8% of items and
is right on the other 92% is more useful than one who guesses everything at 85%.

`telos`, `channel`, and `requisite` are **not rated** in this round: telos is an unpopulated
provisional facet pending re-derivation, and channel and requisite are unpopulated pending the work
in plan §6. Adding them later is a new round, not an amendment to this one.

## 5. The sealed ceiling subsample

Draw **120 of the 600 now**, using the pre-registered seed, stratified by population, and seal them
as the ceiling subsample. Record the ids in this file when drawn.

120 because it is a realistic ask of an unpaid volunteer — an hour or two — while being enough for a
usable α with a reportable interval. A second human asked to rate 600 will not finish; one asked to
rate 120 might.

Sealing it now matters for two reasons. It fixes the item set before anyone knows which items are
hard, so the ceiling cannot be computed on a flattering subset. And it lets the second human be
briefed and run without touching anything else in the pipeline.

**Contamination rules for the second human.** They see the registry definitions and the item text.
They do **not** see Daniel's labels, any model's labels, this protocol's §6, or the plan document —
whose worked examples would prime exactly the judgments being measured. Brief them from the registry
alone.

## 6. Two-tier reporting

**Tier 1 — available with one human. Publishable on its own.**

- Concordance of each model with the reference rater, per facet.
- Krippendorff's α among model raters, per facet.
- Reference rater test–retest α (§3), reported as the interpretive floor for both.
- Risk–coverage and calibration, using abstention.
- All of it split random / hard, never pooled.

Tier 1 supports the claim the program actually needs: *at coverage C, authoring-time concordance is
X, and the abstained remainder routes to human review.* That claim does not require a second human.

**Tier 2 — when the second human arrives. Additive only.**

- Human–human α on the 120-item ceiling subsample.
- The ceiling itself: model α on a facet is read against human α on the same facet and same items,
  so a model at 0.62 where humans reach 0.64 is at ceiling, not failing.
- Every human–human disagreement becomes a V4 definition-repair candidate. These are the highest-
  value defects in the whole program — two competent people reading the same definition differently
  is a defect in the definition, with no other explanation available.

**What Tier 2 cannot retroactively fix**, and this is why §2's naming discipline is not pedantry: if
Tier 1 was published calling concordance "accuracy," Tier 2 arriving with a low human ceiling would
turn the earlier claim into an overclaim already in print. Name it correctly the first time and
Tier 2 only ever adds.

## 7. What AI raters do in the interim — and what they cannot do

Model raters are not a stopgap; they are the bulk of the design and they run from the start. With
one human they carry four of the five Tier 1 results on their own: model–model α, concordance
against the reference, the calibration and abstention data, and — most usefully — the
**disagreement clusters that drive the V4 repair loop**. A pair of definitions that models split on
at scale is a defect in those definitions, and finding it needs no human at all. That loop can run
for months before a second human appears, and the taxonomy will be materially better when they do.

What model raters cannot do is stand in for the second human, for a reason that is structural rather
than about capability. The second human's contribution is evidence that the definitions are
applicable by *someone other than the author*. Model raters cannot supply that: their errors are
correlated with each other through shared training, and — the sharper problem — they may be
correlated with the reference rater himself.

  **Prior-exposure risk, and it is not hypothetical.** `syntelos.md` and `sda.md` are published at
  `dhh1128.github.io/papers/`. A model rater may have seen them in training. If it has, its
  concordance with Daniel is partly recall of Daniel's own prose rather than application of the
  definitions as written — which inflates exactly the headline number, in the direction that
  flatters the taxonomy.

**So probe for exposure before the rating run, per seat, and record the result.** Ask each seat, with
no context supplied, what Syntelos is; what the roots of its taxonomy are; and to continue a
distinctive sentence from either paper. Score exposure as `none` / `partial` / `substantial`. Then:

- Report concordance **split by exposure tier**. If exposed and unexposed seats concord equally, the
  worry is empirically dead and can be retired with evidence. If exposed seats concord markedly
  better, the gap is the memorisation premium and the unexposed figure is the honest one.
- Prefer unexposed seats for the headline where any are available.
- Never average across tiers without showing the split.

This probe is cheap, it runs once, and it converts an unfalsifiable objection a reviewer would
certainly raise into a measured quantity. It also has a chance of returning the most useful possible
answer — that exposure makes no difference — which no amount of argument could establish.

**Pilot, 2026-08-20 — early and encouraging, not yet the probe.** Asked cold, in one sentence, what
Syntelos is, the `ds`, `gpt`, and `mistral` seats each returned exactly `NO KNOWLEDGE`. That is the
answer one wants, and it is one question rather than three: it does not test the taxonomy roots or
the continuation prompt, and a model can fail to *name* a concept while still having absorbed its
content. Run the full three-part probe per seat before the rating round and record the tiers. But
the prior is now that exposure is low, which makes the unexposed-seat headline likely to be
available rather than something to hope for.

Note that the same risk does not attach to the second human, and is a further reason they are worth
waiting for even though nothing waits on them.

## 8. Order and fatigue

Randomise item order per rater from the pre-registered seed, and interleave populations so nobody
rates 135 statutes consecutively. Record the presentation order with the labels — an order effect
that goes unrecorded is indistinguishable from a facet effect.

Rate in sittings of at most 100 items, with the sitting boundary recorded. If concordance degrades
measurably within a sitting, that is a finding about the instrument, not about the taxonomy.
