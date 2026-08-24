# Syntelos 2.0 — current state and handoff

Written 2026-08-25 at the end of the first working session, at a phase boundary. **Read this first.**

## Where the project is

Architecture settled, registry machinery working, ten corpora acquired, and the telos facet derived,
stress-tested and frozen but **known incomplete**. Nothing has been named yet, and no evaluation has
been run. Nothing is pushed.

| phase | state |
|---|---|
| 0 architecture | done — absorb SDA's model; faceted coordinates, not a hierarchy; narrow form scope |
| 1 registry + linter + CI | done — 26 nodes, lint green |
| 2 effect / state-kind / modality / requisite | done |
| 2.5 civil-law audit + corpus verification | done |
| 3a corpora P1–P10 | done |
| 3b sampling frame + rating protocol | done, seed pre-registered |
| **T telos derivation** | T1–T4 done; **T-supp pending**; T5 naming not started |
| 3c draw the gold sample | blocked on T |
| 4 gold standard (Daniel rates) | not started |
| 5–8 reliability, repair, comparison, paper | not started |

## Reading order

1. **`syntelos-2.0-plan.md`** — the design record. Long. §1 architecture, §3 scope, §6 the validation
   programme and the civil-law audit, §7 registry discipline, §8 phases.
2. **`telos-T4-frozen.md`** — the frozen partition. Ten roots, five children, each with an outward
   test. The semantic contract.
3. **`telos-stress-cases.md`** — the most active document. Daniel's adversarial cases, the v1
   back-test, and every open finding from them. §10 has the recommended next step.
4. **`telos-T2-discriminators.md`** — how each outward test was arrived at, and the T3 rulings.
5. **`naming-criteria.md`** — for T5, when it comes. Not yet applied.
6. **`horizon-and-depth.md`** and **`adversarial-and-expressive-acts.md`** — the two conceptual
   detours, both containing retractions worth reading before re-deriving anything.
7. `sources/` — raw analyses from delegated seats, plus every prompt used.

## The next action

**A supplementary derivation pass**, before naming and before adversarial review. Reviewing a
partition known to be incomplete would spend reviewers rediscovering what is already known.

Three targeted draws into the existing blind batch pipeline (`tools/build_telos_sample.py`,
`tools/run_batches.sh`, gated by `tools/degenerate.py`):

1. **P1 + P2** — never drawn from. Two missing roots trace to this.
2. **P9 redraw over-weighting SOC 27, 39, 21** — arts, personal service, community service. The
   material is already in the corpus; even-stratification thinned it to ~17 acts per group.
3. **P10** — retained.

Consolidate **against** the frozen partition rather than from scratch: *what does this corpus contain
that the twelve roots cannot express?* Smaller question, preserves the recurrence evidence.

## Known missing from the frozen partition

Three families, each found by a case rather than by the corpus:

- **`coerce`** [F-9BKW] — apply or threaten force against a non-consenting party. Attack, arrest,
  seize, punish, deter, enforce a judgment.
- **`agree`** [F-6WDN] — establish a mutual or unilateral binding undertaking. Treaties, contracts,
  promises, settlements. v1 had this as `/trade/deal`.
- **the experiential family** [F-7HTQ] — play, ceremony, decoration, performance. One family, not
  four gaps. Test works in the negative: no deliverable beyond the experience itself.

## Open defects in the frozen tests

- [F-7PQD] `protect` covers barriers, not rescue or extraction.
- [F-2NVJ] `communicate` does not distinguish authoring from relaying.
- [F-6CTX] `belong` covers changing membership, not exercising it — **participation is uncovered**.
  Found four separate times.
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

And four times, a corpus's **selection principle** has produced a hole that looked like a finding:
the v1 simulated scrape measured a model's priors; four instrumental corpora agreed about `/relate`
because all four inventory instrumental activity; social APIs missed mourning because an API holds
what someone found it profitable to build a button for; and the telos pool missed coercion because
the legal corpora were acquired and then not drawn from. Agreement between corpora that share a
selection principle is not independent corroboration.

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
