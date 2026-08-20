# V0 — the sampling frame

Draft 2026-08-19. The protocol that has to be fixed *before* any act is drawn, so that the
reliability figures in V2–V3 mean something. Everything here is a commitment made in advance; a
change after sampling begins is an amendment with a date and a reason, not an edit.

Why this exists at all: the v1 corpus was AI-*generated* (`prompts/1-research-asst-scrape-categories-1.md`
asks for a "simulated scrape"), so its coverage histogram measured the scrape's priors as much as
the taxonomy's — `analysis/2-categories-coverage-summary.md` says so itself. Everything below is
sampled from an enumerable population that exists independently of this project.

## 1. The unit of analysis

**The unit is an ACT, not a source item.** A statute section, an archetype duty list, and a
credential example each yield zero, one, or several acts. This matters because it forces two
decisions that would otherwise be made silently during annotation.

**Extraction rule.** An act is a verb applied to an object, at a granularity where a principal could
plausibly permit or forbid it. "File a financing statement" is an act. "Commercial transactions" is
not (no verb). "Click submit" is not (below the granularity where permission is meaningful).
Where a source item names several acts joined by `--` or `;`, each becomes its own unit.

### The granularity condition, sharpened

*Added 2026-08-20, after P8 acquisition exposed the gap.* The clause above screens on the presence
of a verb, which is mechanical, and on granularity, which was pure judgment — so the P8 harvest
put `"click an element on the page"` (`p8-mcp-0196`, from `puppeteer/puppeteer_click`) into the
corpus beside "settle a payment", and nothing in the rule excluded it. A condition that only a
careful rater can apply is not a rule; it is a hope.

Anchor it in the machinery the papers already have. An act sits at the right granularity if it
falls on an **intent boundary** — the point, defined in `syntelos.md` §3.7 and `sda.md` §3, at
which one party's knowledge of another's intent becomes inadequate, so that proceeding without a
fresh decision would overstep. That is exactly the granularity at which permitting or forbidding is
meaningful, and it is not circular, since it appeals to neither the facets nor the classification.

Two operational tests, both applicable without reading the taxonomy:

- **Subsumption.** If any policy a principal would write about this act is entirely subsumed by a
  policy about its obvious parent act, it is too fine. A rule about clicking an element is really a
  rule about operating a browser session; a rule about settling a payment is not merely a rule
  about using the finance system.
- **Parameterisation.** If naming this act requires enumerating an unbounded set of siblings that
  differ only in a parameter, it is too fine. This is `syntelos.md` §3.9's own principle — there are
  no separate categories for buying blue shoes and red shoes — applied to extraction.

**And measure it rather than trusting it.** Each rater records a granularity verdict per item —
`in-scope`, `too-fine`, `too-coarse` — and V2 reports α on that judgment alongside the facets. If
raters cannot agree on granularity, the rule is broken, and it is far better to learn that from the
reliability run than from a reviewer.

**Screening happens AFTER sampling, never before.** Only 35–45% of Utah Code headings are
act-shaped at all (E4 §1, estimated). It is tempting to filter the population down to act-shaped
items and then sample — that is wrong, because the filter's bias becomes unmeasurable and its
decisions unauditable. Instead: draw from the whole population, then screen each drawn item, and
**record every screen-out with its reason**. The screen-out rate is then itself a result — an
empirical test of E4's 35–45% estimate, which is currently one model's guess from a sample.

Over-draw accordingly. To land 135 acts from a population screening at ~40%, draw ~340 items.

## 2. Populations

| # | Population | Frame | Size | Role |
|---|---|---|---|---|
| P1 | Utah Code section headings | `bakobo/utah-id-law/corpus/utah-code/`, `<section>` catchlines | 28,606 | Common-law legal acts |
| P2 | Civil Code of Québec | `bakobo/civil-law-acts/corpus/CCQ-1991-en.txt.gz` | 3,523 arts | Civil-law legal acts — the invariance comparison |
| P3 | French Code civil | `bakobo/civil-law-acts/corpus/CC-FR.txt.gz` | 2,896 arts | Second civil-law jurisdiction |
| P4 | German BGB | `bakobo/civil-law-acts/corpus/BGB-en.txt.gz` | 2,506 §§ | **Orientation only** — see §6 |
| P5 | Tefa archetype actions | `bakobo/tefa/research/archetypes/*/raw/00-starter-outline.md` | 15 archetypes | Delegated/agentic acts — the target domain |
| P6 | GCD examples and invalid cases | `bakobo/schema/gcd/{examples,invalid}/` | 18 files | Whole population |
| P7 | Utina demo acts | `bakobo/utina` demo strings | 6 | Whole population |
| P8 | DIDComm protocols + MCP tool definitions | `bakobo/interaction-acts/corpus/acts.jsonl` | 445 acts | Digital interaction — v1's home turf |
| P9 | O*NET Work Activities | `bakobo/work-activities/corpus/acts.jsonl` | 19,898 acts | Whole-economy work — care, physical service, teaching, trade |
| P10 | Relational and social acts | `bakobo/relational-acts/corpus/*.jsonl` | 481 acts | ActivityStreams 2.0, schema.org, social APIs, iCalendar, and 120 delegated relational acts |

P8 is load-bearing for the telos re-derivation (plan §1, guard 2): the v1 roots were built for
exactly this domain, and re-deriving them against only legal and agentic corpora would replace one
skew with another.

**Acquired 2026-08-20** — 50 DIDComm protocols (the whole registry, 250 message types) plus 25
referenced specs at pinned commits, and 325 MCP tool definitions across 37 servers, yielding 445
distinct acts (132 DIDComm, 313 MCP). Contamination screen: 0 hits against the registry's 82 cited
acts, re-run independently. 445 comfortably exceeds the 105 allocation, so no shortfall and no
reallocation.

Three known noise sources in this population, all to be reported with any P8 result rather than
quietly absorbed:

- **55 of the 132 DIDComm acts take their object from the protocol name rather than the message**,
  because the message name is a bare verb. This works for `rooms/1.0/join` → "join a room" and
  reads badly for `calendar/1.0/accept` → "accept a calendar". Expect depressed rater agreement on
  that slice and check whether P8's α gap concentrates there.
- **54 payload-named messages were screened out** (`keylist`, `message`, `availability` — nouns with
  no verb). Correct call: supplying "send a *X*" would have manufactured 54 acts sharing one
  extractor-invented verb. But the loss is systematic rather than random, and it removes precisely
  the notification-shaped acts, so P8 under-represents them.
- **20 reply messages** (`-response`, `-ack`, `-received`) were screened out as entailed by their
  request, while `mediate-grant` / `mediate-deny` were kept as discretionary decisions. That line
  was drawn by hand. The rule it implies — *a reply that a protocol obliges is not a separate act; a
  reply that embodies a choice is* — should be stated and tested, not left as an extractor's habit.

**P9 acquired 2026-08-20** — O\*NET 30.3 (May 2026), CC BY 4.0 with USDOL/ETA attribution and
trademark conditions recorded in the corpus repo. 332 IWA, 2,034 DWA, 17,532 task statements across
923 SOC occupations. Contamination screen: 0 hits. It closes five of the six domains that halted the
telos re-derivation — care 1,269 acts, physical service 1,829, teaching 627, market exchange 292,
civic 39 — and drops read-operations from a third of the pool to 8%.

Two caveats that bind on how it may be sampled.

- **P9 is not 19,898 independent observations.** The expected collapse between the DWA layer and the
  task layer did not happen — only 7 texts deduped — which means the two layers largely describe the
  same work at two granularities rather than covering different work. **Sample stratified by
  `level`, and never treat a DWA and its cognate tasks as independent evidence about coverage.**
- **The 41 Generalized Work Activities were deliberately excluded.** They are O\*NET's own top-level
  partition, and admitting them into a corpus whose purpose is bottom-up derivation would seed that
  derivation with another taxonomy's categories. Reversible via `--include-gwa` if ever wanted for a
  comparison rather than a derivation.

**Every population must state what its selection principle omits.** Added 2026-08-20 after the
third occasion this bit. A corpus is not neutral about what it contains: the v1 simulated scrape
measured a model's priors; protocols, statutes, steward roles and O\*NET all miss social bonding
because all four are inventories of instrumental activity; and the social APIs miss mourning and
condolence because an API holds the relational acts someone found it profitable to build a button
for. Agreement between corpora that share a selection principle is not independent corroboration,
and it reads exactly like a finding until someone names the principle. So each population's entry
carries an omission note, and any cross-population agreement claim must first establish that the
populations do not share a selection rule.

## 3. Allocation

Target for the V1 gold standard: **600 acts.**

| Population | n | Rationale |
|---|---|---|
| P5 tefa | 150 | The domain the taxonomy is actually for |
| P1 Utah | 135 | Matched pair with P2 |
| P2 CCQ | 135 | Matched pair with P1 |
| P8 DIDComm/MCP | 105 | v1's domain; needed to re-derive telos honestly |
| P3 French CC | 45 | Second civil-law jurisdiction, guards against Québec being idiosyncratic |
| P6 + P7 | 30 | Whole populations, no sampling |

**P1 and P2 are deliberately equal.** They are the jurisdiction-invariance test: same instrument,
same raters, same n, two traditions. A per-facet α gap between them is then attributable to the
tradition rather than to sample size, which is the only way the "jurisdiction-invariant" claim gets
tested rather than asserted.

## 4. Sampling method

**Systematic sampling with a random start**, on the population's native order, at interval
`k = ceil(N / n_draw)`. Not simple random sampling: the codes are ordered by subject, so systematic
draw guarantees spread across the whole book, and the Utah extraction already used a 1-in-14
systematic draw whose behaviour is understood.

**Seed the start from a value fixed in advance and recorded**, so the draw is reproducible and
cannot be quietly re-rolled if the first sample looks inconvenient.

  **Seed: `3249626741`.** Drawn from `secrets.randbelow(2**32)` and recorded here at
  2026-08-20T00:01:03Z, before any act was sampled. `sha256("3249626741")[:16] =
  ddfb026bb1e28a53`, so the commit that introduced this line timestamps the pre-registration. Every
  population's systematic start is `seed mod k` for that population's interval. If this seed is ever
  changed, the old value stays in this file with the date and reason — a silently replaced seed is
  indistinguishable from a re-rolled sample.

**Stratify only on source-native variables** — Utah title number, CCQ book, tefa archetype. Do NOT
stratify on facet values. Stratifying on the thing being measured is circular: it would guarantee
coverage of every `(effect, state-kind)` cell and thereby destroy the coverage finding, which is one
of the results V2 is supposed to produce. Facet coverage is an **outcome**, not an input.

## 5. Rare cells, and the honest way to handle them

600 acts across a 5 × 6 grid averages 20 per cell, but the real distribution will be badly skewed —
`create`/`record` will be crowded and `destroy`/`authority` sparse. So facet-level α will be well
estimated and **cell-level estimates will be thin**. Say so in the report rather than presenting one
number.

Where a cell is empty or near-empty after the probability sample, draw a **supplementary targeted
sample** for it. That sample is non-probability by construction, must be labelled as such, and must
never be pooled with the probability sample for any α or coverage figure. It exists to exercise
definitions, not to estimate anything.

## 6. Exclusions, and why each

- **P4 (BGB) is excluded from the gold standard.** The corpus item is an Internet Archive snapshot
  of the *official English translation* — three removes from authentic law (snapshot → translation →
  non-authentic text), manifested `validity: amended` against its own 10 Aug 2021 cut-off. Usable
  for orientation and for checking a doctrinal claim; not usable as a sampling frame. Re-fetch from
  a working network path, then reconsider.
- **P3 is annotated in French, and kept.** *Resolved 2026-08-20.* Every English rendering of the
  Code civil is unofficial, so translating it would introduce a translation confound into precisely
  the comparison meant to detect a tradition effect. Dropping P3 would instead cost the guard
  against Québec being idiosyncratic — leaving a single civil-law source carrying the whole
  invariance claim.

  Neither is necessary, because the CCQ is officially bilingual and its **French text is
  equally authoritative** with its English. So French-language adjudication has a doctrinal
  reference in the same language: a rater working P3 in French consults CCQ-1991-**fr**, not a
  translation of anything. The V1 gold subsample for P3 is 45 items, small enough to adjudicate
  this way, and the model raters in V2 are competent in French.

  The residual risk is real and gets reported rather than designed away: rater fluency is a
  variable P1/P2 do not have, so a P3 α that trails P2's is ambiguous between a tradition effect
  and a language effect. P3 is therefore read only as a *guard* — it can disconfirm a P2 finding,
  and it may not carry one alone.
- **Repealed and reserved provisions** are screened out and counted, not silently dropped.

## 7. Contamination control

**Any act cited in the registry as an `example`, `counter_example`, or `near_miss` is disqualified
from the evaluation corpus.** Those items were used to *write* the definitions; scoring a classifier
on them measures memorisation of the spec's own worked cases.

This is not a promise, it is a check: `syntelos/tools/disqualified.py` emits the disqualification
list mechanically from the registry, and the eval harness must diff every drawn act against it. The
list grows whenever a node gains an example, so it must be regenerated at draw time rather than
cached.

The risk is concentrated in P6 and P7, whose items are heavily cited in the effect and state-kind
nodes. Expect most of those 30 to disqualify, and treat that as correct behaviour rather than a
shortfall to be topped up from elsewhere.

## 8. Blinding

Raters see the act text and its source citation. They do **not** see:

- any classification the source itself carries (GCD example files name their own `acts` coordinates;
  strip them),
- other raters' labels,
- which population an item came from, where that is inferable and would cue a facet — in practice
  this is impossible for statutes and unnecessary for them, so the rule binds on P6/P7 only.

## 9. The hard split

Held entirely separate from everything above. Seeded from the 20 adversarial cases already
identified — E1 §5's ten GCD pressure points and E3 §6's ten hardest steward actions — and grown
during annotation with any item where the three raters split three ways.

It is **non-probability by construction**. It is reported alongside the random split and never
merged with it. A headline figure computed on the random split alone would overstate performance,
which is the fifth objection in plan §6.

## 10. What is fixed and what is open

Fixed by this document: unit of analysis, extraction rule, screen-after-sample discipline,
population list, allocation, sampling method, stratification ban, exclusions, contamination rule,
blinding, hard-split separation.

Settled since the first draft: the seed is fixed and pre-registered (§4); P3 is kept and rated in
French against the equally-authoritative CCQ French text (§6); P8 acquisition is under way against
the DIDComm protocol registry, the Aries RFCs, and the reference MCP servers, extracted to
`acts.jsonl` with no facet labels attached — pre-labelling the corpus would contaminate the
blinded classification step.

Still open, and each is a decision rather than a task:

- **Rater panel composition for V1.** Three independent raters are assumed throughout, with Daniel
  adjudicating. Whether the other two are models, people, or one of each changes what the human
  ceiling in V5 means and should be settled before the gold standard is built, not after.
- **Rater panel composition for V1** is the only genuinely open item left. Three independent raters
  are assumed throughout, with Daniel adjudicating. Whether the other two are models, people, or one
  of each changes what the human ceiling in V5 measures, and it should be settled before the gold
  standard is built rather than after.

**P5 resolved 2026-08-20 by re-extraction.** The original inventory was a model's report of what it
read in the archetype docs. It has been replaced by a quote-anchored extraction: two independent
passes over the 15 `00-starter-outline.md` files, unioned, with every act required to carry a
verbatim quote that `tools/verify_quotes.py` checks against the source. The corpus is
`eval/corpora/p5-steward-acts.jsonl` — **176 acts across all 15 archetypes**, 8 to 17 each,
comfortably above the 150 allocation.

Union rather than intersection is deliberate: over-recall is safe when every candidate must clear
quote verification, whereas an intersection would discard each real act that only one pass noticed.

The verification is not a formality. **125 of 301 candidate acts were dropped — 92 of them because
the quote does not appear in the source file at all.** See plan §6 for what that rate means; for
the frame's purposes, the corpus that survived is anchored and the corpus that was proposed was
not.
