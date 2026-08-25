# Syntelos 2.0 — current state and handoff

Written 2026-08-25 at the end of the first working session and updated at the end of the second,
both at phase boundaries. **Read this first.**

## If you are a new session

Do the next action in "The next action" below. Before you start:

- **Do not re-derive the telos partition from scratch.** The recurrence counts (how many of 15 blind
  passes independently found each concept) are the most expensive artifact here and cannot be
  regenerated cheaply. The supplementary pass *adds to* the frozen partition; it does not replace it.
- **Conserve Daniel's tokens.** Delegate analysis to OpenRouter seats and `codex` rather than reading
  large corpora yourself. Operational notes below — they were learned the hard way.
- **Autopush is on.** `git-autopush` runs nightly at 02:45 and this repo is **public**
  (`dhh1128/syntelos-research`). Commits publish without anyone deciding to publish them. The three
  corpus repos under `~/code/bakobo/` are local-only with no remote; keep them that way.

### Operating the seats — learned by failing

- **Chunk the work.** A 150-act batch clusters in 50–150s; a 1,076-act pool times out. Payload size
  is the dominant variable.
- **`PANEL_TIMEOUT` is an env var**, documented at the top of the `panel` wrapper. The 600s default
  is not a hard limit. Use 900.
- **Cap `max_tokens` explicitly** (16000 works). OpenRouter *reserves* against `max_tokens`, not
  actual usage, so a modest request 402s on a balance that could easily afford it. The default is
  65536.
- **Tune effort per seat, not globally.** `ds` degenerated at medium and was clean at low; `kimi` was
  clean at medium.
- **`codex exec --skip-git-repo-check`** — the flag is required or it refuses. Separate quota from
  OpenRouter, which is why it kept working when credits ran out.
- **Never `2>/dev/null` a seat call.** Eleven HTTP 402s were misread as timeouts because stderr was
  suppressed. Capture it per output.
- **Gate every output with `tools/degenerate.py`.** Latency and word count are *inverted* quality
  signals: the fastest, longest run of one experiment was 1,730 words of collapsed repetition. Empty
  output fails the gate too — that is deliberate.
- **Gate JSONL with `tools/jsonl_gate.py`, not `degenerate.py`.** Repeated field names read as a
  token loop to a trigram test. It also fails a file whose last line is an unterminated object,
  which is what a run that hit its token cap looks like — full of good records, silently covering
  a fraction of its batch.
- `tools/run_batches.sh` (prose) and `tools/run_extract.sh` (JSONL) encode all of the above, retry
  once on a failed gate, and skip work already passing. Both take engines as arguments; `codex` is
  one of them.

## Where the project is

Architecture settled, registry machinery working, ten corpora acquired and all ten now yielding acts,
and the telos facet derived, stress-tested, frozen, and then probed a second time against material
it had never seen. It is still **known incomplete** and now knows more precisely where and why.
Nothing has been named yet, and no evaluation has been run. Most commits are already on the public
origin via nightly autopush — see above.

| phase | state |
|---|---|
| 0 architecture | done — absorb SDA's model; faceted coordinates, not a hierarchy; narrow form scope |
| 1 registry + linter + CI | done — 26 nodes, lint green |
| 2 effect / state-kind / modality / requisite | done |
| 2.5 civil-law audit + corpus verification | done |
| 3a corpora P1–P10 | done |
| 3b sampling frame + rating protocol | done, seed pre-registered |
| **T telos derivation** | T1–T4 done; **T-supp done 2026-08-25**; T5 naming not started |
| 3c draw the gold sample | blocked on T — but P1 and P2 now have act corpora, so half of it is built |
| 4 gold standard (Daniel rates) | not started |
| 5–8 reliability, repair, comparison, paper | not started |

## Reading order

1. **`syntelos-2.0-plan.md`** — the design record. Long. §1 architecture, §3 scope, §6 the validation
   programme and the civil-law audit, §7 registry discipline, §8 phases.
2. **`telos-T4-frozen.md`** — the frozen partition. Ten roots, five children, each with an outward
   test. The semantic contract.
3. **`telos-T-supp.md`** — the supplementary pass and its results. `govern`, the density floor, the
   argument against the experiential family, four test defects. §7 is what needs Daniel.
4. **`telos-stress-cases.md`** — Daniel's adversarial cases and the v1 back-test. Its §10
   recommended the supplementary pass, which has now run.
5. **`telos-T2-discriminators.md`** — how each outward test was arrived at, and the T3 rulings.
6. **`naming-criteria.md`** — for T5, when it comes. Not yet applied.
7. **`horizon-and-depth.md`** and **`adversarial-and-expressive-acts.md`** — the two conceptual
   detours, both containing retractions worth reading before re-deriving anything.
8. `sources/` — raw analyses from delegated seats, plus every prompt used.

## The next action

**A decision from Daniel, then T5 naming.** The supplementary pass is done and `design/telos-T-supp.md`
is the write-up. It ran fifteen blind passes over a 670-act pool built from P1, P2, a P9 redraw and
P10, and consolidated them against the frozen partition on three engines. Two things need his call
before anything else moves — both are in §7 of that document — and nothing in the pass suggests
reopening the derivation a third time.

  [ Q-CQC1 ]  **Does `govern` enter the partition?** 13/15 passes, three independent consolidations,
  a clean discriminating question against all four neighbours. Stronger evidence than `belong` or
  `judge` carry today. Check it against the modality facet first — "issues a rule that binds
  members" is adjacent to what modality expresses, and this project's recurring failure mode is a
  distinction that belongs on another facet.

  And whether to accept the four test repairs, which are cheap and well evidenced.

## Known missing from the frozen partition

- **`govern`** [F-AC2S] — issue, amend or repeal a rule, office, budget, programme or binding
  decision for a collective. **Found by the corpus, 13/15**, and the only new root any of the three
  consolidations proposed. Missed the first time because the pool held no rule-making and because
  the T1 question — `telos-T1-review.md:114`, "one root, two, or three?" — offered only `conform` and
  `judge`, so nobody asked who makes the standard.
- **`coerce`** [F-9BKW] — apply or threaten force against a non-consenting party. Found by a case.
  **The supplementary pass had no power to confirm or refute it**: coercion is under 2% of the pool
  even after P1 and P2 were drawn from at full strength, and the smallest group any pass emitted was
  4% of a batch. See [F-MVTY].
- **`agree`** [F-6WDN] — establish a mutual or unilateral binding undertaking. Found by a case. Same
  density problem, worse — under 1%.
- **ritual and commemoration** — all three consolidations name it as what the corpus cannot decide.
  It is the surviving part of the experiential family.

  [ F-MMJT ]  **The rest of the experiential family [F-7HTQ] has a real argument against it.** At
  adequate density, all three consolidations split play/performance/decoration between a widened
  `provide` — an event is a deliverable — and the horizon screen. Not a failure to find it.

## Open defects in the frozen tests

Four are now well evidenced enough to just apply; the rest still need a call.

- [F-7PQD] `protect` covers barriers, not rescue or extraction. **Third independent arrival** —
  the supplementary consolidations found it from firefighting and post-breach response. Settled.
- [F-8H3R] `judge`'s "contested claim" misses uncontested probate, name changes, adoption decrees
  and administrative determinations. All three consolidations.
- [F-5FY5] `provide`'s "artifact" misses events, services and operated capabilities. All three.
- `communicate`'s "identified audience" misses publishing and broadcast. One consolidation, but
  plain on inspection.
- [F-6CTX] `belong` covers changing membership, not exercising it — **participation is uncovered**.
  Found four separate times and **not resolved** by the supplementary pass, which mapped it into
  `belong` without answering the objection.
- [F-2NVJ] `communicate` does not distinguish authoring from relaying.
- [F-8KMR] receptive acts (accept, receive, admit) fit awkwardly.
- [F-2QLJ] `transfer`'s test excludes theft; it is drawn too narrowly.
- [F-4RDM] some species distinctions (dowry: `trade` or `give`?) are contested by participants, not
  merely hard to observe.

## Standing decisions that constrain everything

- **[D-2CFX]** every telos node must be **externally checkable**; a distinction a stranger cannot
  decide from observable features is not a node.
- **[D-6PVH rev.2]** the outward test may appeal to an outcome the act **determines** through
  mechanism; not to outcomes needing further acts, another party's uptake, or repetition.
- **[D-7NKQ]** hierarchy depth means **species-of**, not further-downstream-from.
- **[D-3HBK]** telos is **multi-valued**; MECE is a property of the partition, not a one-label rule.
- **[D-3WQP]** standing relations are not purposes — they belong on the relation facet.
- Verbs, not nouns. Names are a separate pass and none has been chosen.

## The recurring failure mode, stated once

Four times, a distinction has turned out to belong on a facet other than the one it first appeared
on: `representing` (relation), causal horizon (constraints), `create`/`preserve` (effect),
adversariality (requisite and modality). **When a candidate root looks compelling, test first whether
it is another facet in disguise.**

A second failure mode, found 2026-08-25 and distinct from the sampling ones below: **a consolidation
can only choose among the options its adjudicating question admits** [P-GK0W]. `govern` was not
rejected in T1, it was foreclosed — the question was framed as `conform` versus `judge` and no pass
was ever asked about the third arm. When settling a contested boundary, check that the question
being put is not a binary imposed on a wider set.

And four times, a corpus's **selection principle** has produced a hole that looked like a finding:
the v1 simulated scrape measured a model's priors; four instrumental corpora agreed about `/relate`
because all four inventory instrumental activity; social APIs missed mourning because an API holds
what someone found it profitable to build a button for; and the telos pool missed coercion because
the legal corpora were acquired and then not drawn from. Agreement between corpora that share a
selection principle is not independent corroboration.

And a **density floor** underneath all of it [F-FPHH]: a family below ~4% of a pool is invisible to
recurrence-across-blind-passes, whatever its importance. Drawing from the right corpus does not fix
a family that corpus holds too little of — coercion went from 0% to under 2% and stayed invisible.
Cases reach what density cannot, which is why the two instruments belong in the paper together
rather than one being presented as the evidence base.

## What a new session loses

The state is in these files, which is why a break here is safe. What does not survive is the
conversational thread — which arguments Daniel found persuasive, the shape of his objections, and
the several places where his corrections overturned my recommendation. The commit messages carry
most of that deliberately; `git log` is worth reading for the reasoning, not just the changes.

Three of his calls are worth knowing about before reopening anything: he kept `/relate` against my
recommendation and was vindicated three separate ways; he rejected causal horizon as a hierarchy
axis, which retracted a whole design I had written; and he corrected my reading of v1's telos
definition, which retracted a finding. **The pattern is that his objections have been right, and
mine have been the ones needing retraction.**
