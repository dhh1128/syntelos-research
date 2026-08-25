# T-supp — the supplementary derivation pass

Run 2026-08-25. Fifteen blind clustering passes over a 670-act pool the first derivation never saw,
consolidated by three engines against the frozen partition rather than from scratch.

It returned one candidate root the frozen partition does not contain, four defects in existing
outward tests, an argument against one of the three families the stress cases said were missing,
and a measurement that says the other two were never findable this way at all.

## 1. What was run

`tools/build_law_units.py` drew 493 Utah sections and 294 CCQ articles systematically at the
pre-registered seed. Two engines extracted quote-anchored acts from them, every quote checked
against `eval/corpora/sources/p{1,2}-units.txt`, yielding **924 verified P1 acts and 683 verified
P2 acts** — the first time either corpus has produced acts at all.

`tools/build_telos_supp.py` drew the pool: 200 P1, 150 P2, 200 P9 over-weighted by SOC major group
(27 arts, 39 personal service, 21 community service, 33 protective service, plus 25 across the
other eighteen), 120 P10. **670 acts, targeted and non-probability by construction** — a coverage
probe, not a frequency estimate.

Five batches of 134 went to three engines under the unchanged T1 batch prompt, so these passes are
comparable with T1's fifteen. Raw output in `sources/telos-supp-batches/`. Consolidation used a new
prompt (`sources/prompts/telos-supp-consolidate-prompt.md`) that sorts every input group into
covered / nearly covered / not covered against the frozen ten, and deliberately withholds `coerce`,
`agree` and the experiential family so that naming them would be corroboration rather than echo.
Three consolidations in `sources/telos-supp-consolidation-{ds,kimi,codex}.md`.

## 2. The finding: `govern` is missing, and it is not one of the three we were looking for

  [ F-AC2S ]  **A root is missing whose end is the collective rule itself: issuing, amending or
  repealing a rule, office, budget, programme or binding decision for a body.** Thirteen of the
  fifteen passes emitted a group named `governance`, `govern`, `regulation` or `order`; the two that
  did not used `manage` and `stewardship` for the same acts. All three consolidations proposed it
  independently, and it is the **only** new root any of them proposed.

The outward test they converged on, in ds's wording: *does the act set, change, or repeal a rule or
standing decision for a collective, rather than only comply with, coordinate under, or resolve a
dispute under existing rules?* It is decidable at act time and appeals to no one's uptake.

The discriminating questions are sharp, which is what makes this a root rather than a stretch:

- against **conform** — conform answers to an external standard; govern **issues** it.
- against **judge** — judge resolves a claim between parties looking backward; govern sets
  forward-looking direction for a body, and no claim need exist.
- against **coordinate** — coordinate fixes times and roles among consenting parties; a statute
  binds parties who did not consent and fixes no time or place.
- against **belong** — belong changes who is inside the boundary; govern directs what the bounded
  body does.

### Why T1 could not have found it, and why the answer is not "another absent corpus"

Two causes, and the second is the more interesting.

**The pool contained no rule-making.** P5, P8, P9 and P10 are corpora of work done *under* rules —
steward duties, protocol operations, occupational tasks, social acts. A statute book is made of
rule-making. Of the 1,415 acts the fifteen passes assigned to a named group, **115 went to groups
called `governance`, `govern`, `order` or `regulation` — about 8%**, well above the density a pass
can cluster on. A keyword probe over the first pool finds 0.2%.

**And the T1 question foreclosed it.** `telos-T1-review.md:114` put C10+C11 as *"governance — one
root, two, or three?"* and the options on the table were `conform` versus `judge`: is conduct being
tested against a standard, or is a contested question being resolved? `ds` had in fact proposed
`govern` at 15/15, but its `govern` meant conformity, dispute resolution and enforcement *together*,
so resolving the question as conform-versus-judge looked like it had disposed of governance
entirely. Nobody asked who makes the standard. The distinction that survives — issuing a rule versus
answering to one — was never a candidate, and `telos-T2-discriminators.md:212` records the residual
unease without locating it: *"a regulatory enforcement action both applies a standard and issues a
binding determination, and much of what a regulator does sits exactly there."*

  [ P-GK0W ]  **A consolidation can only choose among the options its adjudicating question
  admits.** Framing C10/C11 as one-or-two collapsed a three-way distinction into a binary and lost
  the third arm silently — no pass dissented, because the question was never put to the passes. This
  is a distinct failure from the sampling faults: the corpus is not at fault, the *question* is.

That governance is missing from a taxonomy aimed at governance is the same shape of embarrassment
as [F-9BKW]'s absent coercion, and from the same neighbourhood of the model.

## 3. What did not recur, and why that is not evidence against it

Neither `coerce` [F-9BKW] nor `agree` [F-6WDN] was proposed by any pass or any consolidation.
Before reading that as disconfirmation, the density was measured.

Two instruments, because they answer different questions. For a family the passes *did* name, the
honest measure is how many acts they assigned to it. For a family no pass named, the only available
measure is a probe of the pool, and a probe over-counts: a wide regex returned 25 candidates in the
supplementary pool, of which hand review found **8 clearly coercive and 4 arguable** — "waive civil
penalties", "patrol premises", "record progress of investigation" and "force embalming fluid into
organs" are not coercion.

| family | how measured | share of pool | acts per 134-act batch |
|---|---|---|---|
| governance | assigned by the passes, 115 of 1,415 | 8% | ~11 |
| experiential | assigned by the passes, 89 of 1,415 | 6% | ~8 |
| coercive | hand review of 25 probe candidates | 1.2–1.8% | 1.6–2.4 |
| binding undertaking | hand review of probe candidates | under 1% | under 1.3 |

The smallest group any of the fifteen passes emitted held five acts. A family therefore needs
roughly **4% of a pool** to be visible at all, and coercion sits at a third of that even after the
legal corpora were drawn from at full strength. In the first pool it was at zero.

  [ F-MVTY ]  **Drawing from P1 and P2 raised coercive acts from zero to under 2%, which is still an
  order of magnitude below the density at which a clustering pass can see a family.** The §6.1
  diagnosis was right about the cause and incomplete about the remedy: drawing from the legal
  corpora was necessary and is not sufficient. There is no draw from these populations that fixes
  it, because arrest, seizure and punishment are a thin slice of a statute book — the Utah Code is
  mostly licensing, revenue, organisation and administration, and the CCQ is private law with no
  criminal procedure in it at all.

  [ F-FPHH ]  **Recurrence-across-blind-passes cannot confirm a rare-but-real act family, and this
  is a floor in the method rather than a fixable sampling error.** Every act family below ~4% of a
  pool is invisible to it, however important. `coerce` and `agree` were found by cases; `govern` was
  found by the corpus and no case had raised it. The two instruments reach different things and
  neither dominates — which is worth saying in the paper, because a derivation that reports only its
  corpus evidence is claiming a completeness it cannot have.

So the status of `coerce` and `agree` is unchanged by this pass. They were not corroborated and they
were not challenged; the experiment had no power to do either.

## 4. The experiential family: a real argument against [F-7HTQ]

Here the density *was* adequate — 6%, about eight acts per batch, from the P9 redraw — and the
passes did emit the groups: `creation`, `performance`, `recreation`, `craftsmanship`, `culture`.
All three consolidations then declined to make it a root, splitting it two ways:

- **The checkable part is `provide` with too narrow a test.** Staging a performance, holding an
  exhibition, running a funeral, operating a gaming table: these bring something into being and keep
  it available, and fail only on the word *artifact*. All three proposed the same repair
  independently — artifact **or event, service, or production**.
- **The rest is a horizon.** Where the claim is that the point is amusement, reverence or being
  moved, that lives in the audience and the act does not determine it. Killed by [D-6PVH rev.2],
  exactly as *persuade* and *build trust* were.

  [ F-MMJT ]  **The experiential family's proposed test — *no deliverable beyond the experience
  itself* — is answered by the claim that an event is a deliverable.** A staged performance, a
  ceremony and a decorated wall are all things brought into being and made available, which is
  `provide`'s extension once its test stops saying *artifact*. This is a substantive counter-argument
  to [F-7HTQ] rather than a failure to find it.

Weight it carefully. The consolidators were shown the frozen partition and asked whether an existing
node reaches each group, which biases toward absorption. But the same three consolidators proposed
`govern` as a new root when they judged one necessary, so the bias is not total, and three
independent absorptions with the same reasoning is more than nothing.

What survives untouched is the part [F-7HTQ] shares with the mourning gap: **ritual and
commemoration**. All three consolidations name it in section E as the thing this corpus cannot
decide, and the funerary acts in the pool were the most consistently unplaced items across the
passes. Whether *commemorate* is a root, a child of `belong`, or `conform` to a conventional form is
open, and it needs a corpus of weddings, funerals, religious observance and civic ceremony.

## 5. Defects in existing outward tests

Four, three of them new. Each was proposed independently by at least two of the three consolidations.

  [ F-8H3R ]  **`judge`'s "contested claim" is too narrow.** Uncontested probate, a name change, an
  adoption decree, a status declaration, a default remedy, an administrative determination: an
  authorised procedure fixes the parties' legal position and no contest exists. Proposed repair —
  *does an authorised procedure determine a claim, legal status, liability, remedy, or sanction in a
  way that binds affected parties?* All three consolidations, independently.

  [ F-5FY5 ]  **`provide`'s "artifact" is too narrow**, per §4 — events, services and continuously
  operated capabilities. All three consolidations.

  **`protect` is too narrow**, corroborating [F-7PQD] from a direction the kitten case did not
  reach: firefighting, rescue, evacuation, hazard suppression, and containment after a barrier has
  already failed. Two repairs proposed, *directly intervene to reduce exposure* (ds) and *deploy a
  countermeasure* (codex). This is the third independent arrival at the same defect and it should
  now be treated as settled.

  **`communicate`'s "identified audience" is too narrow** (codex only). Publishing, broadcasting and
  open exhibition complete transmission without any individually identified audience. Proposed
  repair — *identified or publicly delimited audience*. One consolidation is weak evidence, but the
  defect is plain on inspection and costs nothing to accept.

**[F-6CTX] is not resolved.** One pass emitted `participation` and every consolidation mapped it
into `belong`, kimi adding only that belong's test "should be read to include roles". That does not
answer the objection: attending a caucus exercises a standing without changing who may enter or act.
The corpus did not settle it and the four case-based findings stand.

## 6. What all three say this corpus still cannot tell you

Converging, and worth recording as the brief for any future acquisition:

- **ritual, worship and commemoration** — named by all three.
- **self-directed play, rest and subsistence** — acts whose point is the actor's own immediately
  realised state. Recreation appeared here only as staged entertainment.
- **destruction as an intended end** — demolition, euthanasia, decommissioning, deliberate erasure.
  Destruction appeared in this corpus only as a hazard to be prevented, never as a purpose.
- **reproduction and cultivation** — breeding, planting, childrearing as ends.
- **conflict between collectives** — war, conquest, surrender, diplomacy, which is where `coerce`
  and `agree` both live and which no corpus in the frame contains.

The last item is [R-7QSD] arriving on schedule: the held-out military corpus recommended two
sessions ago is the population that would exercise both families at a density that could support a
derivation, and it is the one that has not been acquired.

## 7. Open questions

  [ Q-CQC1 ]  **Does `govern` enter the partition?** The evidence is 13/15 with three independent
  consolidations and a clean discriminating question against all four neighbours — stronger than
  `belong` (9–10/15) or `judge` (9–10/15) carry today. The counter-argument is that it needs
  checking against the modality facet before adoption, since "issues a rule that binds members" is
  adjacent to what modality already expresses, and this project's recurring failure mode is a
  distinction that belongs on another facet.

The same question carries an ordering problem. Adopting `govern`, repairing four outward tests, and
resolving `coerce` / `agree` / `commemorate` are three different kinds of change, and only the first
two are supported by evidence in hand. The third needs a corpus nobody has.

The freeze still holds structurally. Nothing in it was refuted; three of its tests are too narrow
and one root is missing from it.
