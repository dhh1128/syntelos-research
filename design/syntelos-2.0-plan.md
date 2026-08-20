# Syntelos 2.0 — a development plan

Living design record. Started 2026-08-18.

Sources read for this plan: `~/code/me/papers/syntelos.md` (v1.1), `~/code/me/papers/sda.md`
(v1.2), `~/code/me/papers/3dim.md`, this repo's `prompts/` and `analysis/`,
`~/code/bakobo/schema/gcd/`, `~/code/3GR/custos/spec/custos-4.2.md`,
`~/code/bakobo/utina/docs/`, `~/code/bakobo/tefa/` (docs + 15 archetype research dirs),
`~/code/bakobo/products/concepts/steward/`, and a 1-in-14 sample (2,044 of 28,606) of Utah Code
section headings from `~/code/bakobo/utah-id-law/corpus/utah-code/`.

Four of those were analyzed by OpenRouter seats rather than by me, to conserve budget; raw
outputs are in `design/sources/e{1,2,3,4}-*-analysis.md` and are quoted below. Every load-bearing
claim from them is attributed.

---

## 1. The finding that reframes the request

You asked for "syntelos 2.0 with expanded scope." The expansion has already happened — in a
different paper, under a different name.

`~/code/me/papers/sda.md` ("The Shape of Delegated Authority", v1.2, 2026-07-14) already carries
every element you described wanting. It adds an **effect** axis (`observe`, `create`, `modify`,
`preserve`, `destroy`), a **state-kind** axis (`information`, `record`, `commitment`, `authority`,
`resource`, `relationship`), a **relation** facet (`delegation`, `guardianship`, `controllership`,
`stewardship`), first-class **duties** with cadence and priority, acts as **vectors** of
coordinates rather than single nodes, and gates **derived** from coordinates rather than
hand-assigned. It also states, in §3, exactly the diagnosis you arrived at independently:

> Syntelos scopes itself deliberately, through a *refusal test* … This is a sound boundary for an
> intent-negotiation grammar. It is the wrong boundary for a delegation.

And `~/code/bakobo/schema/gcd/` already **implements** that model. The GCD schema's
`a.constraints.acts[]` is literally the matrix — a two-axis coordinate with a brace grammar
(`"observe {info, record}"`, `"{create, modify} commitment"`), 5 × 6 = 30 syntactically valid
cells, with the rule that an act is authorized only if *every* cell it occupies is covered
(E1, quoting `gcd/gcd.schema.json`). Duties live at `r.duties[]` with `{bearer, effect, goal,
cadence, priority}` and fail-loud precedence.

So the real question is not "what should Syntelos 2.0 contain." It is:

  [ D-7VXK ]  **Absorb, settled 2026-08-18.** Syntelos 2.0 becomes the whole act model — the name
  is worth keeping as the expression of what this is for. The binding constraint Daniel attached:
  it must carry **SDA's full scope**, not be v1 with axes bolted on. See "Guarding against v1 skew"
  below; that constraint has teeth and changes real work.

Three architectures were live, and this was the one-way door — everything downstream (registry
shape, conformance suite, what Custos cites) follows from it.

**A — Absorb.** Syntelos 2.0 becomes the whole act model: all facets in one normative spec with
one registry and one conformance suite. SDA is retitled as the theory/motivation paper and cites
Syntelos 2.0 for the vocabulary it currently defines inline. GCD cites Syntelos for all axes.

**B — Federate.** Syntelos keeps the telos facet only, but drops the refusal test so the tree
covers unilateral and legal acts. SDA keeps effect/state-kind/relation. A new thin composition
grammar spec joins them. Two normative specs.

**C — Layer.** Syntelos 2.0 = expanded telos tree + a profile registry mapping telos paths onto
legal-act classes for Custos, with effect/state-kind referenced by normative reference to SDA.

**Recommendation: A**, for three reasons. (i) GCD already needs all the axes in one credential;
splitting the normative source across two papers guarantees the drift that already exists —
SDA says `information`, GCD says `info`; GCD's `README.md` describes separate `effects` and
`stateKinds` fields while the schema uses composed `acts` (E1 §5.10). (ii) Custos requires a
**committed** act class and forbids inference (see §3 below), which means one canonical identifier
per act, not a composition each integrator assembles their own way. (iii) The single biggest defect
E1 found is that GCD's 11 axis tokens have **no individual definitions anywhere in the source** —
"NOT IN SOURCE" against every one of them. Writing those definitions, with examples and
counter-examples and an inter-rater study behind them, is precisely the work a taxonomy spec
exists to do. It is Syntelos's job, and nobody else is doing it.

The cost of A is honest: it makes Syntelos 2.0 a substantially different document from v1, not a
revision. Hence 2.0.

### Guarding against v1 skew

Absorbing has a specific failure mode — the merged spec inherits v1's centre of gravity and treats
SDA as an appendix. Three concrete guards, because "don't skew it" is not self-executing.

1. **No facet is the parent.** The canonical identifier is the coordinate tuple. The spec must not
   also define a single slash-delimited rendering of it, because anything that looks like a path
   will be treated as one, and the telos facet will quietly become the spine again. v1's §4
   path/wildcard conventions survive only *within* the telos facet, not over the whole coordinate.

2. **Re-derive the eight roots; do not grandfather them.** `/relate /share /care /serve /align
   /trade /operate /govern` were derived under the refusal test, for a two-party interaction
   grammar. Under the governability test of §3 they are a **hypothesis to test against the merged
   corpus, not a given**. The evidence that they will not survive unchanged is already in hand: E3
   §4 finds 40–50% of the steward corpus non-interactive, and those acts — reconcile a ledger, run a
   DPIA, update a setpoint, mark a bug cannot-reproduce — have no home in a partition built for
   interactions. Expect the root set to change. If it does not, that is a finding to justify, not a
   relief.

3. **The merged paper's frame is SDA's, not v1's.** SDA opens on Pharaoh's ring, three modern
   reductions, and a model simpler than the problem; v1 opens on Alice clicking "Watch." SDA's frame
   already contains v1's as a special case — v1's semantic void is one instance of the reduction SDA
   names — and the reverse is not true. Draft from SDA's spine and fold v1's argument in as the
   intent-grammar chapter, rather than appending SDA's axes to v1's §5.

---

## 2. The structural break: Syntelos stops being a tree

Three independently-prompted models, given different corpora, reached the same conclusion by
different evidence. I discount agreement between LLMs heavily — but the *evidence* differed, which
is what makes this worth acting on.

From the Utah Code (E4 §5): the same institutional form crosses purposes — "registration" covers
doing business (§16-1a-503), voting (§20A-2-101), motor vehicles (§41-1a-201), and support orders
(§81-8-610). Calling all of these `/operate/register` erases the legally decisive object and
effect; distributing them across purpose roots erases their shared form. Conversely one purpose
requires legally non-interchangeable forms: "protect my child" is served by creating a trust
(§75B-2-401), delegating parental powers (§75-5-103), petitioning for annulment (§81-4-303), and
buying coverage (§31A-22-655) — and purpose determines none of validity requirements, authorized
actor, third-party effect, revocability, forum, or remedy.

From Custos (E2 §5): purpose is not byte-derivable, and axiom 4 (§1.4) forbids a fold consuming
anything underivable from committed bytes. The demo's centerpiece proves it — D3 and D6 are the
same decision, same purpose, same dissenter, defeated under unanimity and pending under the board.
A telos node would carry zero evaluator payload.

From GCD (E1 §5): ten concrete pairs where two annotators would classify the same act differently
because the axes have no definitions — signing a contract as `create commitment` vs.
`create relationship`; deleting a database as `destroy record` vs. `destroy info` vs.
`destroy resource`; transferring money as `modify resource` *and* `create commitment` *and*
`create record` in one transaction.

  [ D-K2M9 ]  **Syntelos 2.0 is a faceted coordinate system with a tree on one facet, not a
  hierarchy.** An act is located by a coordinate, not named by a path. This preserves v1's cascading
  consent (still true within the telos facet) while admitting the acts v1's scope excluded.

Proposed facets, held to SDA's own "as simple as possible, but not simpler" test:

| Facet | Values | Answers | Provenance |
|---|---|---|---|
| **telos** | the v1 tree, scope-expanded | why | Syntelos v1 |
| **effect** | 5 closed | what transformation | SDA §4 / GCD |
| **state-kind** | 6 closed | over what kind of state | SDA §4 / GCD |
| **modality** | may / must / must-not | deontic force | new — see §4 |
| **form** | open, profiled | what makes it legally effective | new — see §5 |

`relation` (delegation/guardianship/controllership/stewardship) stays on the *grant*, not the act —
SDA §5 is right that it is a property of the arrangement, and GCD already places it at
`a.facet.relationType`. Do not move it.

The act-is-a-vector rule from SDA §4 carries over unchanged, and it is what makes this tractable:
filing a return is `create`-in-`record` *and* `create`-in-`commitment` in one move, and its gate is
the join.

### Telos re-derivation, attempt 1 — halted 2026-08-20, and why

Guard 2 says re-derive the eight roots rather than grandfathering them. The first attempt was a
blind bottom-up partition: 621 acts pooled from P5 and P8, shuffled with the pre-registered seed,
handed to seats with **no sight of v1's taxonomy**, each asked to derive 5–12 purpose roots from the
acts alone. Blinding was the point — shown the eight roots and asked whether they work, a model
confirms them.

One seat completed (`design/sources/telos-partition-*`); two hit the 600-second cap on the 621-row
assignment table. The completed partition returned eleven roots — `discovering` 241, `coordinating`
91, `transforming` 89, `governing` 47, `assuring` 37, `authorizing` 33, `transacting` 24,
`publishing` 21, `remediating` 18, `deciding` 10, `staffing` 10.

**The result is not a taxonomy. It is a measurement of the corpus.** `discovering` takes 39% of the
pool because MCP tool definitions are dominated by reads. And a direct term-probe over the pool —
not a model's opinion, a regex I can re-run — shows what is absent:

| v1 root | acts in pool | note |
|---|---|---|
| `/care` | 1 | false positive — "treat like cases alike" |
| `/serve` | **0** | no repair, install, clean, construct, manufacture |
| `/relate` | 2 | both false positives |
| `/trade` | **0** | no buy, sell, purchase, bid, price |
| `/govern/vote` | 1 | |
| `/share/teach` | **0** | |
| read/observe | 204 (33%) | for contrast |

  [ F-QN7X ]  **The pool cannot re-derive telos, and proceeding would have been worse than not
  trying.** Four of v1's eight roots have zero support in it and two more have one act each. A
  partition derived here would have deleted `/relate`, `/care`, `/serve`, and `/trade` on the
  evidence that a corpus of software tools and office roles does not contain them — replacing v1's
  interaction skew with a software-and-office skew. That is precisely the failure guard 2 exists to
  prevent, arrived at by the opposite route.

The completed partition's own section E says the same thing unprompted, which is the one part of it
worth keeping: it lists physical production, caregiving, learning, experimentation, consumption,
social bonding, civic representation, market exchange, environmental stewardship, and personal
self-maintenance as domains the corpus cannot speak to, and concludes that its roots "should not be
treated as a proven universal taxonomy."

**What the corpus needs before attempt 2.** P1 (Utah) and P2 (CCQ) will supply market exchange,
family, property, and civic acts once drawn. They will not supply care, physical service, teaching,
or social bonding, because statutes regulate those activities without enumerating them as acts.

  [ R-2VBH ]  **Acquire O\*NET Work Activities as a population.** It is a public, enumerable,
  cross-economy catalog of what people actually do at work — including the healthcare, construction,
  agriculture, personal-service, and education occupations this pool has none of. `sda.md` already
  cites it (ref [13]) as one of the three traditions that "takes the act surface seriously." It is
  the cheapest available fix for exactly the gap measured above, and without it the telos facet
  cannot be re-derived honestly at any level of effort.

Attempt 2 waits on that. Nothing else in the program does — the effect, state-kind, and modality
facets are unaffected, and the gold standard can be built on them if the telos facet is explicitly
deferred to a second rating round. That trade (two rating passes) is now worth re-examining against
[Q-4HKN], which assumed one pass was achievable.

**O\*NET acquired 2026-08-20, and it closes five of the six gaps.** P9 brings 19,898 acts from
O\*NET 30.3 across 923 occupations. Re-running the probe that condemned the earlier pool, with
substring artefacts removed by hand: care 1,269, physical service 1,829, teaching 627, market
exchange 292, civic 39. Read-operations fall from 33% of the pool to 8%. The corpus that could not
support a derivation now can, for five of the six domains it lacked.

  [ F-5TQD ]  **`/relate` is still empirically unsupported, and it is the only root that is.**
  One act in 19,898 — *"…teaching, counseling, or befriending them"*, from a caregiving occupation.
  Not an acquisition failure: O\*NET catalogues paid work, so befriending, celebrating, playing, and
  mourning are outside its frame by construction. They are equally absent from the protocol corpus,
  the steward corpus, and — once drawn — the statutes, which regulate marriage and adoption as legal
  acts without ever naming the bonding they solemnise.

That four independent corpora, assembled for different reasons, all miss the same root is more
interesting than a sampling gap. A plausible reading is that `/relate` acts fail the governability
test of §3 on their own terms: no principal writes policy about celebrating a birthday, and nobody
delegates being someone's friend. If so, `/relate` is not under-sampled but out of scope for a
taxonomy of governable acts — and v1 included it because v1 was a grammar for *signalling* intent to
a stranger, where "why is this person contacting me" makes `/relate` entirely real.

  [ D-8MRC ]  **`/relate` stays in scope, and a corpus gets acquired for it. Settled 2026-08-20,
  against my recommendation, and the argument that settled it is worth recording because I had it
  wrong.**

I had reasoned that `/relate` fails the governability test: nobody writes policy about celebrating a
birthday, nobody delegates being a friend. Daniel's counter-example is professional matchmaking —
Indian matchmaking, the Jewish *shadchan*, the marriage broker — and it is decisive.

The error was conflating **the act** with **authority over the domain**. You cannot delegate *being*
someone's friend. You can, and people routinely do, delegate *negotiating a marriage*, *screening
suitors*, *issuing invitations*, *representing someone socially*, and *managing a public persona*.
Matchmakers, publicists, social secretaries, agents, guardians arranging a ward's contacts, and
diplomatic protocol officers all exercise delegated relational authority, and some of it — an
arranged marriage negotiation — carries stakes at the very top of the range this taxonomy exists to
gate. v1's `/relate/seek`, "find new connections," is exactly the matchmaking node.

Note what this says about the governability test itself. Applied to an act *in isolation*, it
produced the wrong answer, because "celebrate a birthday" looks ungovernable while "arrange my
daughter's marriage" plainly is not, and they sit under the same root. The test is sound but has to
be applied to the act as a delegate might perform it, not to the act as a principal performs it for
themselves. That is a real refinement to §3 and it came from the counter-example, not from theory.

  [ F-6BKW ]  The absence of `/relate` from four corpora is therefore **a property of the corpora,
  not of the domain**. Protocols, statutes, steward roles, and paid-work catalogues are all
  inventories of instrumental activity; O\*NET catalogues occupations and there is no SOC code for
  matchmaker. That the gap replicated across four independent sources made it look like a finding,
  which is a good reminder that replication across sources sharing a *selection principle* is not
  independent replication at all.

**P10 acquired 2026-08-20.** 481 acts at `bakobo/relational-acts/`: 361 from W3C ActivityStreams
2.0/ActivityPub, schema.org's Action hierarchy, five social platforms pinned to commit shas, and the
iCalendar RFCs — plus 120 **delegated relational** acts across 16 roles, held in a separate file
because their provenance discipline differs. Contamination: 0 hits. 874 screen-outs recorded.

The delegated subset is the half that justifies [D-8MRC], and it came back better sourced than I
expected: IMBRA (8 U.S.C. § 1375a), Korea's marriage-brokerage act, four US state dating-service
statutes, UGCOPAA and Utah Title 75 all enumerate an agent's relational acts one by one, several
consent-gated on a *named* counterparty. The cultural roles are thinner — the *nakōdo* rests on one
journalistic article and the *shadchan* on a 1906 encyclopedia — and the caveat in the corpus notes
is the right one: a statute says what an agent *must* do, which is adjacent to, not identical with,
what a principal *permits*.

Coverage after artefact correction: bonding 26, boundary 28, delegated 23, ceremony 17, play 5. The
raw `play` count of 16 was inflated threefold by `party` matching "third party" and `join a` matching
every membership call — the same substring trap that made the earlier `/relate` count look like 47
when it was 1.

  [ F-7CDW ]  **Mourning and condolence are zero across every corpus assembled.** Not thin — absent.
  `condolence` and `congratulate` occur zero times in all 18,796 O\*NET task statements, and the 39
  `funeral` hits are funeral-*services* trade rather than consoling. Play stands at 5 acts.

The acquiring agent's own explanation is the right one and generalises: *an API holds the relational
acts someone found it profitable to build a button for.* That is the third time this session a
corpus's **selection principle** turned out to be the thing that mattered — the v1 simulated scrape
measured a model's priors, the four instrumental corpora agreed about `/relate` because they were all
inventories of instrumental activity, and now the social corpora are inventories of monetisable
interaction. Every population in the frame should carry an explicit statement of what its selection
principle systematically omits, not just what it contains.

### Licensing constraint on the derivation

The P10 sources do not share a licence: W3C permissive, schema.org **CC BY-SA 3.0** (share-alike),
Mastodon **GFDL-1.3**, Discord CC BY-SA 4.0, Slack MIT, Matrix Apache-2.0, Bluesky MIT/Apache-2.0,
IETF BCP 78. GFDL-1.3 and CC BY-SA are mutually awkward in a combined work.

  [ R-4XNP ]  Two rules, and they are cheap to follow if adopted now rather than discovered later.
  **Derive, do not copy.** A taxonomy category inferred from studying a corpus is not a derivative
  work of the source texts — systems and facts are not copyrightable — but reproducing schema.org's
  or Mastodon's *definitions verbatim* in the spec would be, and would drag a share-alike obligation
  onto a standard meant to be freely implementable. Every definition in `taxonomy/` must be written
  fresh. **And quarantine the GFDL material**: Mastodon's 60 acts overlap heavily with Discord,
  Slack, Matrix and Bluesky, so dropping them costs little coverage and removes the one genuinely
  incompatible licence from the pipeline.

Attempt 2 is unblocked. `/relate` support is real but thin, and the honest report will say the root
rests on 26 bonding acts and 23 delegated ones rather than on the thousands backing `/serve`.

### Telos attempt 2 — 2026-08-20

Domain-balanced sample of 1,076 acts (`syntelos/tools/build_telos_sample.py`), blind as before. The
balancing worked: the largest root took 17% of the sample against attempt 1's 39%, and read-heavy
`discovering` no longer swallows the partition. Two `panel` seats timed out again even on the
partition-only task; `codex` completed, on a separate quota. Result at
`design/sources/telos2-partition-codex.md`.

Eleven roots: `making` 186, `sensemaking` 175, `coordinating` 126, `assuring` 102, `governing` 94,
`restoring` 84, `authorizing` 69, `caring` 64, `representing` 57, `exchanging` 45, `developing` 40.

**`caring` emerged**, which it did not in attempt 1 — direct payoff from the O\*NET acquisition.

  [ D-3WQP ]  **`representing` is rejected as a root: it is the relation facet leaking into telos.**
  Daniel's argument, and it turns on the taxonomy's own criteria rather than on taste. `syntelos.md`
  §3.4 places intents on a proximate–ultimate continuum and §3.5 requires siblings to sit at roughly
  the same point on it. Representing is always a means: the matchmaker's end is the marriage, the
  publicist's is reputation, the attorney's is the settlement. Strip representation away and an end
  remains; strip the end away and representation has nothing to be.

The distinction that makes this sharp — and that saves `coordinating`, `authorizing`, and `assuring`
from the same objection, since each is arguably a means too — is **phase versus standing relation**.
Coordination completes on its own terms before whatever the meeting is for begins; it is a
time-slice with its own telos, which is exactly the decomposition argument of `syntelos.md` §3.11.
Representation completes never: it is a posture the actor holds across every phase. Standing
properties belong on facets, phase purposes belong on telos, and `sda.md` §5 already carries
representation as `relationType`. Admitting it here would encode one fact twice on two axes declared
orthogonal.

  [ F-2HXB ]  **The prompt, not the model, produced the bad root.** It said "purposes, not
  mechanisms," which screens the bottom of the continuum and says nothing about the middle.
  `representing` is neither a mechanism nor an ultimate end. The derivation prompt now carries an
  explicit proximate/ultimate screen with the strip-it-away test and a standing-relation exclusion
  (`design/sources/prompts/telos2-partition-only-prompt.md`). Any future attempt inherits it, and
  attempt 3 should be re-run with it rather than patched after the fact.

`representing`'s 57 acts are not lost — their telos is whatever they represent *toward*, so they
redistribute across the other roots on re-run rather than needing a home carved for them.

**`/relate` still did not emerge**, even balanced. Section D of the run is explicit: matchmaking and
introductions are present but facilitative, while "loving, befriending, or sustaining mutual intimacy
as an actor's own purpose is absent." The partition placed the matchmaking acts under `coordinating`
and `representing`, which is defensible — introducing two people genuinely is coordination. What the
corpus cannot settle is whether matchmaking's telos is *aligning parties* or *forming a bond*; that
is a theory question, and per [D-8MRC] the root stays on the author's judgment.

### Telos attempt 3 — chunked, 2026-08-20

Map-reduce instead of one heroic call. The 1,076-act sample split into 8 batches of ~135; each
batch clustered independently by two seats, blind to every other batch and to each other; the 15
surviving cluster sets then consolidated into one partition. Every batch output passed
`tools/degenerate.py` before use, and the runner
(`tools/run_batches.sh`) retries once on a failed gate — which recovered `ds-07` on attempt 2.
15 of 16 batches produced usable output.

This is better methodology than a single global partition, not merely a workaround for timeouts.
**Because the batches are independent and blind, the number of passes that independently recover a
root is evidence about that root** — something no single-call derivation can produce. Recurrence,
before consolidation: `care` 10, `communication` 9, `coordination` 8, `knowledge`/`compliance`/
`commerce` 7 each, `justice` 6, `safety`/`production`/`maintenance` 5 each.

Consolidated partition, with the count of passes independently finding each:

| root | passes | root | passes |
|---|---|---|---|
| `care` | ~14/15 | `coordination` | ~14/15 |
| `protection` | ~14/15 | `participation` | ~9/15 |
| `knowledge` | ~14/15 | `persuasion` | ~6/15 |
| `communication` | ~14/15 | `union` | ~5/15 |
| `provision` | ~14/15 | `ecology` | ~3/15 |
| `conformity` | ~13/15 | `justice` | ~10/15 |
| `exchange` | ~12/15 | | |

  [ F-4KDM ]  **`union` emerged — and it is `/relate`.** *"Bring particular parties into a durable
  pairing or alliance, especially marriage or kinship. It is narrower than generic matching: the
  relationship formed is itself the terminal outcome."* Its discriminating question is exactly the
  one attempt 2 could not settle: *is a continuing bond the end, rather than selection for a role,
  which serves the role's further purpose?* Five of fifteen independent passes isolated it.

That vindicates [D-8MRC] on evidence rather than on authority, and it says something about method.
Attempts 1 and 2 asked one model to partition a thousand acts at once, and in that setting a root
supported by ~3% of the corpus is invisible — it gets absorbed into whatever large neighbour it most
resembles. Splitting the corpus into slices where relational acts are locally salient let the root
surface in the passes that contained it. **A small root is not weak evidence; it is evidence that a
global partition cannot see.**

`representing` did not reappear in any of the 15 batches or in the consolidation, so the
ultimate-purpose and standing-relation screens [F-2HXB] held.

**The labels above are provisional handles, not results.** The derivation established each root's
*extension* — which acts group together — and its *discriminating question*. It established nothing
about names: `care`, `provision`, `conformity` and the rest are words the seats happened to emit
while describing groups. Naming is a separate design pass against stated criteria, set out in
`design/naming-criteria.md`. Two problems visible already: v1 §4.1 requires category names to be
**verbs** and almost every derived label is a noun, and the thirteen labels collide on initials —
five `c`, four `p`, two `e` — which is unusable for a vocabulary people will abbreviate.

So the comparison against v1 has to be stated **extensionally**, about where acts land rather than
about which word survived:

- The acts v1 filed under `/govern` distribute across **three** derived groups, separated by whether
  a contested question is authoritatively resolved, whether conduct is tested against an existing
  standard, or whether harm is prevented.
- The acts under `/share` split in **two**, on whether success is a justified state of understanding
  or receipt by an audience.
- `/serve` and `/operate` acts **merge** into one group whose terminal outcome is that something
  usable is available.
- `/relate` acts split in **two**: durable pairing of particular parties, and belonging or
  recognised presence in a community.
- `/care`, `/align`, and `/trade` each map to a single derived group with closely similar extension.
- **Four derived groups have no v1 antecedent at all** — harm prevention, standard-conformance,
  changing preference or support, and ecosystem condition.

Whether any derived group should inherit a v1 name is a naming question, and reusing one where the
extension has shifted is worse than coining a new word, because implementers will assume continuity.

Weak roots are flagged rather than hidden: `ecology` at ~3/15 is the thinnest retained, `union` at
~5/15 is sparse but sharply defined. Neither should be presented with the same confidence as the
~14/15 roots, and the paper must carry the recurrence counts.

---

## 3. Replacing the refusal test

v1 §3.1 admits an act if it has (1) counterparty volition, (2) policy relevance, (3) semantic state
change. The section is also, in the current file, textually corrupt — `syntelos.md:134-135` contains
a garbled paragraph ("they are incented. , and engage in interactions in cooperative ways, and to
constraints in its interface definition.) … restrict the scope of Syntelos to") that appears to be a
bad merge. Separately, `syntelos.md:274` ends mid-sentence ("but should propose the "), and
`syntelos.md:251` still uses the retired `/gov/Identity.Verify` notation. Whatever else happens,
these are shipped defects in v1.1.

The substantive problem is that criterion 1 is a bad proxy for what criteria 2 and 3 actually want.
It admits "swipe right" and excludes "deploy to production," "notify the breach authority within 72
hours," and "record a lien." E4 §4 lists 20 Utah acts that plainly need a normative name and have no
refusing counterparty — filings, severances, resignations, waivers, renunciations, revocations,
declarations of candidacy, and four *omissions* that are themselves legally operative (failure to
satisfy a judgment §41-12a-511, failure to report §76-18-221, refusing a chemical test
§41-6a-520.1). E3 §4 estimates **40–50%** of the steward action corpus is non-interactive —
"almost all the bookkeeper, financial-analyst, bug-triage, technical-writer, compliance-evidence,
and IAM-reconcile actions."

  [ R-8QHT ]  **Replace the volition test with a governability test, and derive it from the effect
  facet rather than asserting it in prose.** An act is in scope iff it occupies at least one
  (effect, state-kind) cell, and either the effect is not `observe`, or the observation is over
  state some principal restricts.

This is worth the trouble because it is *checkable*. A prose scope test cannot be put in CI; a test
derived from a facet can. Heartbeats and keep-alives occupy no state-kind and fall out for free —
the same answer v1 gives, reached mechanically. `assent` (unilateral / notice-dependent /
acceptance-dependent / consent-dependent / approval-dependent / adjudicated, per E4 §3e) becomes a
*dimension recorded on the act*, which is where volition belonged all along, rather than an
admission criterion.

**One hard constraint from Custos that shapes everything downstream.** Custos deliberately declines
to enumerate the act universe (§3: "it does not enumerate the act universe"; §16 lists "the
act-registry design" among its confessed-open interiors), and Utina binds clauses to act kinds by
*literal string equality* (`Clause.governs: tuple[str, ...]`). Q30 is explicit that a fold may not
infer that a domain's `amend-operating-agreement` is Custos's "enactment amending law" — that
inference "is precisely the uncommitted seam §8.5 says an evaluator refuses rather than legislates."

So a Syntelos coordinate must be **committed at authoring time and matched literally at evaluation
time**. No classifier runs inside the fold. This is not a limitation; it is the single most
important fact for §6, because it relocates the entire AI-error question from evaluation (where a
misclassification would corrupt a legal judgment) to authoring (where it costs a human review
round). Requirements R0–R10 in E2 §2 are the full list and should be lifted into the spec's
conformance section verbatim.

---

## 4. Modality, duties, and omissions

v1 has no deontic modality at all — every category is implicitly a permission. Three sources say
that is insufficient.

E4 §6 estimates **26–34%** of Utah sample headings are principally about mandatory or prohibited
behavior, against **10–15%** granting permissions or powers. GCD already models the "must" side
separately from the "may" side: `a.constraints` is "the enabling 'may'" and `r.duties[]` is
"first-class structured obligations (the 'must')," with an integer `priority` for "fail-loud
conflict resolution … ties escalate rather than being silently dropped" (E1 §3). Tefa treats
refusal as first-class — `ORIENTATION.md` §1: "A steward can say **no**. Refusing an action it deems
out-of-bounds is a first-class, expected part of the role — not a malfunction."

And tefa states the sharp asymmetry that the taxonomy must respect
(`clusters/access-and-privileged-data.md` X-7): "Floors forbid ACTS. They cannot compel TIMELY ONES.
Every archetype here has its most damaging failure in the inaction column."

  [ R-3PNW ]  Model modality as a facet with `may` / `must` / `must-not`, and make **omission** a
  first-class act rather than the absence of one. "Fail to file" and "refuse a chemical test" are
  legally individuated conduct (E4 §6), and the steward corpus's worst failures live in the
  inaction column.

Hohfeld is the right prior art for the effect side and Custos already cites him (§9: "a power held
is a liability borne by its counterparty"). E2 §6 and E4 §3c both land there. Hart's
primary/secondary rules is the right prior art for the law-amending-vs-acting-under-law split,
which Custos treats as load-bearing (§10 designated act classes, §12 reflexive class, §17
succession) and which E2 §4 rates the **strongest** dimension in the whole Custos corpus.

---

## 5. The form facet

**What it is.** Telos says *why* the act was done. Effect × state-kind says *what it transforms and
over what*. Form says *through what institution the act operates, and what makes it effective*.

The clearest way to see that it is genuinely a separate axis is to hold the other two fixed and
watch it vary. One purpose — provide for a child after your death — is served by executing a will
(§75-2-502 form requirements), creating a trust (§75B-2-401), petitioning a court for guardianship
(§75-5-211), and delegating parental powers (§75-5-103). All four are `create` over `commitment` or
`authority`. All four share a telos. They are not interchangeable, and nothing on the first two
facets tells them apart. What separates them is who may perform each, what makes each valid, whether
it binds strangers, and how it ends — all form.

Now hold form fixed and watch the others vary. "File with the registry" covers filing a financing
statement to perfect a security interest (§70A-9a-516), articles of incorporation to create an
entity (§16-1a-206), a D.B.A. to register a name (§42-2-201), and an annual certificate to preserve
a status (§16-11-14). Same form, four different telei and three different effects. Orthogonality
runs both ways, which is the test.

**The internal argument, which matters more than the statutory one.** SDA has already smuggled a
piece of form into state-kind, and it is the source of one of E1's ambiguity pairs. SDA §4 defines
`information` as "meaning not yet authoritative" and `record` as "an entry others may rely on," then
§4's gate rule distinguishes an internal record (automatic) from an *authoritative* record (needs
sign-off). But reliance is not a property of the state — it is conferred by an act of publication,
filing, or recording. That is why E1 §5 finds annotators splitting `create info` vs. `create record`
(#3) and `observe record` vs. `observe info` (#9) with nothing in the source to settle it. Pulling
form out as its own facet lets `record` mean a kind of state and lets *authoritativeness* be a form
property, which cleans up both facets at once. This is worth doing even if we never name a single
statutory instrument.

**What it decomposes into.** E4 §3d is right that formality is a bundle of independent predicates,
not a scale — a single high/low score loses which predicate supplies validity, which supplies
perfection, which supplies evidence, and which supplies notice. So `form` is two things, and the
spec should say so rather than shipping a compound facet:

- **channel** — closed, small, jurisdiction-invariant. The kind of organ the act runs through:
  `private` (between parties, no institution), `registry` (a filing or recording office), `agency`
  (an administrative decision), `tribunal` (court or arbitrator), `assembly` (a deliberative body's
  enactment). Every legal system has these organs under some name; the five-way partition is the
  portable part of E4's "institutional channel" axis.
- **requisites** — an open predicate set: `writing`, `signature`, `witnessed`, `notarized`, `filed`,
  `recorded`, `published`, `noticed`, `certified`. Individually portable; *which* an act needs is
  jurisdictional.

A jurisdictional instrument name — `financing-statement`, `D.B.A.`, `eidas-qes` — is then **not a
facet value**. It is a profile-registered identifier that bundles a channel with a requisite set for
one jurisdiction. That keeps the closed facets closed and pushes the unportable part into profiles.

**Worked, so it is concrete.** Utina's two demo strings become:

`open-bank-account` → effect × state-kind `create relationship` + `create authority` (the account is
a relationship; signature power over it is authority); modality `may`; channel `private`; profile
`form:us/deposit-account-agreement`, needed only if some clause turns on validity.

`amend-operating-agreement` → effect × state-kind `modify authority` — it changes the rules that
constitute who may bind the company, which is Hart's secondary-rule case and the distinction E2 §4
rates the strongest in the whole Custos corpus; modality `may`; channel `private`; profile
`form:us-ut/operating-agreement-amendment`.

Note which facet each would-be Custos clause binds on. "Any act changing who may bind the company
requires unanimous consent" binds on `modify authority` and ignores form entirely. "Any act
requiring recordation must be countersigned by counsel" binds on form and ignores effect. Different
clauses need different facets — which is what orthogonal means operationally, and why collapsing
them into one identifier would force every clause to enumerate instruments.

  [ D-QW4D ]  **Narrow scope, settled 2026-08-18.** Syntelos 2.0 normatively defines telos, effect,
  state-kind, modality, and `channel` — all closed, all jurisdiction-invariant. `requisites` is an
  open predicate set with a registered vocabulary. Instrument names live in **profiles**, and
  Syntelos ships one reference profile plus a conformance test for profiles. Jurisdiction-specific
  enumeration is a standing effort for others.

The bound on ambition is evidence-based. Only an estimated 35–45% of Utah statute headings are
act-shaped at all, and only 15–20% name affirmative private legal acts of the
`amend-operating-agreement` kind (E4 §1). E4 §7 is candid that D.B.A. registration, UCC financing
statements, trust deeds, and initiative petitions do not port to a civil-law system without a
mapping. And Custos does not want a universal registry — it wants a pinnable, committable, stable
vocabulary (E2 §2, R0–R1). Narrow gives it that today.

**The cost, stated plainly.** Each facet added is another place per-facet α can come out low in §6's
V2, and another annotation burden. `channel` should be cheap — five values with sharp institutional
boundaries. `requisites` will be the least reliable thing in the spec, because it is where
jurisdictional knowledge lives; it should probably be measured but not gated in CI until V4 shows
whether it converges.

---

## 6. Proving AI classification is reliable

This is the part you emphasized, and it is where I most want to push back on the existing plan.

**What exists.** `prompts/0-mentor-rag.md` lays out a three-phase program: coverage/corpus study,
inter-rater reliability via Fleiss' κ and semantic entropy, then comparative superiority. Phase 1
ran — three AIs produced 162 classified interactions, summarized in
`analysis/2-categories-coverage-summary.md` with a coverage histogram, four uncovered leaves, and
one hallucinated category (`/operate/ask`). Phase 2 and 3 have not run. `to-do.txt` confirms.

**Five problems with the plan as written.** These are not small; a hostile reviewer will find all
of them.

1. **The corpus is AI-generated, not sampled.** `prompts/1-research-asst-scrape-categories-1.md`
   asks for a "simulated scrape." Whatever the models produced, it is a sample from their priors,
   not from the world, and the coverage histogram in `analysis/2-*.md` measures the scrape's bias as
   much as the taxonomy's — the summary says so itself ("likely due to the nature of the simulated
   scrape"). Reviewer 2 stops reading here. Fix: sample from real populations with a documented
   frame. Four are already local — 28,606 Utah Code section headings, GCD's examples and invalid
   cases, tefa's 15 archetype action inventories, Utina's demo acts — plus DIDComm protocol
   registry and MCP tool definitions, which are enumerable from the web.

2. **Inter-rater agreement is not correctness.** Models trained on overlapping corpora agree while
   being jointly wrong; that is the standing caveat on the whole OpenRouter panel. κ is a necessary
   secondary measure, not the headline. Fix: a **human-adjudicated gold standard** on a stratified
   subsample, with you as final adjudicator, and report *accuracy against gold* as primary and κ
   as consistency.

3. **Fleiss' κ is the wrong statistic for this design.** An act is a *vector* — SDA §4, and GCD's
   rule that every occupied cell must be covered. That makes this multi-label classification across
   several facets, and Fleiss' κ assumes single-label assignment to mutually exclusive categories.
   Fix: **Krippendorff's α**, which handles multi-label, missing values, and the heavy skew you will
   see on the effect facet. Report α **per facet**, never pooled — a faceted scheme has different
   reliability per facet and one number hides exactly the facet that is broken.

4. **Accuracy is the wrong target; calibration is the real claim.** "Little probabilistic error of
   judgment" is a claim about *selective prediction*: the classifier should abstain when uncertain,
   and Custos makes abstention normatively correct (E2 §2 R10 — missing vocabulary yields refusal,
   not failure; demo D8's `declare-dividend` produces a refusal naming the missing rule). Fix:
   report **risk–coverage curves** and expected calibration error alongside accuracy. The publishable
   claim is "at 90% coverage the error rate is X%, and the 10% abstained cases are routed to human
   review" — which is both stronger and more honest than a bare accuracy number.

5. **A random test split will overstate performance.** Fix: report **two splits**. A random split
   from the sampling frame, and a **hard split** built from the adversarial cases the analyses
   already produced — E1 §5's ten MECE pressure points (contract as commitment vs. relationship,
   database deletion three ways, money transfer occupying three cells) and E3 §6's ten hardest
   steward actions (hold-and-escalate an unmatched invoice; route a low-confidence case; mark a bug
   cannot-reproduce; authorize a worker to publish; return unused authority). Never report a headline
   number on the random split alone.

**The reframe that makes the claim defensible.** Because Custos forbids inference at evaluation time
(§3 above), an AI misclassification never corrupts a legal judgment — it produces a coordinate that a
human accepts or rejects at commit time. So the thing to measure is **authoring-time accuracy with
abstention**, and the cost of error is a review round. That is a far more defensible claim than
"AIs classify correctly," and it is *true*, which the stronger claim would not be.

**Program.**

- **V0 — sampling frame.** Document the frame per population, with inclusion rules and sample sizes.
  Pure human/spec work; do not delegate.
- **V1 — gold standard.** Stratified subsample (target ~600 acts, ~150 per facet-stratum), labeled
  independently by ≥3 raters, disagreements adjudicated by you. This is the expensive, irreducible
  human step and the whole program's foundation. Budget real hours.
- **V2 — reliability.** ≥5 models × ≥3 temperature/seed replicates on the full corpus. Krippendorff's
  α per facet; confusion matrices per facet; a per-node error budget so a bad definition is
  attributable to a node rather than to "the taxonomy."
- **V3 — calibration and abstention.** Risk–coverage, ECE, abstention rates on both splits.
- **V4 — definition repair loop.** Every confusion pair above threshold becomes a definition edit
  plus a counter-example in the registry, then V2 re-runs. This loop is the actual product; the
  statistics are its instrumentation.
- **V5 — human ceiling.** Measure inter-*human* α on the hard split. If humans only reach α = 0.6
  on the pressure points, an AI at 0.55 is near ceiling and the honest report says so. Without this
  number, no AI figure can be interpreted.
- **V6 — comparative.** Head-to-head against Aries goal codes (what GCD's `goals` field uses today),
  schema.org Actions, and raw strings (what Utina uses today). The most persuasive result available:
  same corpus, same raters, better α.

Delegation: V2, V3, V6 are mechanical and belong on OpenRouter seats and cheap local scripts. V0,
V1, V4, V5 need you.

### V-CIV — the civil-law falsification track

Everything above is a *reliability* program: can raters apply the facets consistently. It cannot
detect the failure that would matter most, which is that the closed facets are **common-law
artifacts** dressed as invariants. Every source this design drew on is common-law or
software: the Utah Code, the Restatement (Third) of Agency, Hohfeld, Hart, GCD, Custos. E4 §7's
transferability warning is an untested assertion by a model that only read Utah.

This is a falsification test, not a coverage test, so it runs **early and gates the registry**, not
late as a portability check. If the facets cannot express civil-law doctrine, the closed sets are
wrong and phase 1 would be building the wrong skeleton.

Two prongs, because they fail differently.

**Doctrinal (cheap, decisive).** Civil law has something common law lacks: an explicit, worked-out
theory of the *juridical act* — `acte juridique`, `Rechtsgeschäft`, `negozio giuridico`,
`rechtshandeling` — which is *itself a rival taxonomy of acts*, with axes the common-law sources
never name (unilateral/bilateral/plurilateral, onerous/gratuitous, inter vivos/mortis causa,
consensual/solemn/real, commutative/aleatory, causal/abstract, and `acte juridique` vs. `fait
juridique`). E2 §6's prior-art list contains no civil-law doctrine at all, which is a real gap in
that survey. The test is an expressibility audit: for each doctrinal axis, can the facets express
it, derive it, or not represent it. Four specific tests are load-bearing:

- **The abstraction principle.** German law separates the obligational act
  (`Verpflichtungsgeschäft`) from the disposition (`Verfügungsgeschäft`) — a sale is *two* juridical
  acts with independent validity, where French law transfers by consent alone (`solo consensu`). Can
  an act-vector represent one transaction as two doctrinally independent acts? If not, the vector
  model is under-powered where it most claims strength.
- **Causa vs. telos.** A purpose facet sitting next to legal acts is an invitation to conflate
  `telos` with `causa`, which is a validity concept in some systems and abolished in others. If
  implementers make that conflation they will draw wrong legal conclusions. The spec must say
  explicitly that telos is not causa.
- **The five channels.** The Latin notary's `acte authentique` has evidentiary and executory force
  with no common-law analogue, and a `Grundbuch` registration is *constitutive* of title rather than
  notice — which is a different thing from the `registry` channel as derived from Utah recording
  statutes. `notarized` in the requisite list is a probable false friend for
  `notarielle Beurkundung`.
- **Nullity vs. prohibition.** `must-not` may conflate "forbidden" with "void." Civil systems keep
  them apart (`nullité absolue` / `nullité relative`), and an act can be forbidden yet valid, or
  permitted yet void. Since this proposal already separates validity (form) from permission
  (modality), it should be able to carry the distinction — but that has to be checked, not assumed.

**Corpus (expensive, confirmatory).** Sample a civil code the way Utah was sampled, and re-run V2/V3
against it with the same instrument. Nothing suitable is local — `bakobo/eidas-eudi` and
`bakobo/eu-data-law` are EU *regulations*, supranational instruments about digital identity and
data, not codes of private law, and they do not exercise juridical-act doctrine. Acquisition is a
task, not a blocker: the German BGB has an official English translation (gesetze-im-internet.de),
the French Code civil is published by Légifrance with an English translation of the 2016 obligations
reform, and the Civil Code of Québec is officially bilingual — the last is the best first pick, since
it is civil-law doctrine natively expressed in English, which removes translation as a confound.
Louisiana is a useful second, as a mixed jurisdiction that bridges the two traditions.

**Success criterion.** Report per-facet α on the civil-law corpus alongside the common-law figure.
A facet whose α drops materially across traditions is not jurisdiction-invariant, whatever the
doctrinal audit concluded, and belongs in profiles rather than the closed core.

### V-CIV doctrinal prong: first results and triage, 2026-08-19

Run on the Mistral seat (the panel's European seat, chosen for likely exposure to French and German
doctrine). Raw output: `design/sources/e5-civil-law-audit.md`. It returned nine ranked "required
changes." I accept four, reframe three, and reject the rest as scope creep. Relaying its severity
ranking unmodified would roughly double the facet count and violate the discipline SDA sets for
itself.

**The headline finding is misdiagnosed.** The audit's #1 severity item claims the act-vector "cannot
represent two independent acts," so a German sale — `Verpflichtungsgeschäft` plus
`Verfügungsgeschäft` under the `Abstraktionsprinzip` — cannot be modelled, and proposes a new
"transaction-layer" facet. This conflates *one act is a vector of cells* with *one transaction is
one act*. Nothing in the model forces the second; a German sale is straightforwardly two acts, each
with its own vector, its own validity, and its own gate. The audit invented a constraint and then
solved it.

But there is a real gap underneath, and it is one the audit found by accident: **the spec never says
what individuates an act.** Nothing tells an annotator whether a transaction emits one coordinate or
two, and that is precisely the question the abstraction principle makes legally decisive. So:

  [ F-N4RB ]  Syntelos 2.0 needs an explicit **individuation rule** — when is this one act and when
  is it two — and it must be stated so that a jurisdiction whose doctrine splits an act can follow it
  without a bespoke facet. Hardcoding `obligation`/`disposition` would burn German doctrine into a
  supposedly invariant core; an individuation rule lets German law emit two acts and French law
  (`solo consensu`) emit one, from the same spec.

**Accepted, and cheap.**

1. **`notarized` is a false friend and must split.** *Corpus-verified 2026-08-19 — see below; the
   audit's account of WHY was wrong, and my restatement of it repeated the error.*
2. **Registration is constitutive in some systems and declarative in others.** *Corpus-verified and
   refined to three functions, not two — see below.*
3. **The spec must state that telos is not causa.** Predicted in the prompt and confirmed: a purpose
   facet sitting beside legal acts invites implementers to treat telos as a validity condition,
   which it is not — and German abstract transfers are valid with no causa at all. One paragraph of
   normative text, high value.
4. **Scope boundary: Syntelos covers juridical acts, not juridical facts.** The
   `acte juridique` / `fait juridique` distinction is real and load-bearing — a tort, a birth, a
   death produce legal effects that nobody performed. These are events, not acts, and a taxonomy of
   acts should say so rather than leave the boundary to be discovered.

**Reframed.**

5. **`channel` is damaged, not patchable.** The Latin notary genuinely breaks the five-way
   partition: a `notaire` is a public officer exercising delegated authority, so neither `private`
   nor `tribunal` fits, and `agency` implies administrative decision-making a notary does not do.
   The audit proposes bolting on a sixth value. The honest reading is that `channel` was derived
   from one common-law jurisdiction and has not earned closed status. **Demote it to open/profiled
   until re-derived against both traditions** — see the facets.yaml change of 2026-08-19.
6. **Validity vocabulary belongs on form, not on modality.** The audit is right that `must-not`
   alone cannot carry `nullité absolue` / `nullité relative`, and right that an act can be forbidden
   yet valid or permitted yet void. It is wrong that this is a modality problem: the design already
   separates permission (modality) from validity (form). Void / voidable / valid is an outcome
   property and belongs with the requisites that produce it. No new facet.
7. **Party structure is already covered.** The audit calls unilateral/bilateral/plurilateral
   INEXPRESSIBLE, but the `assent` dimension carried since §3 (unilateral, notice-dependent,
   acceptance-dependent, consent-dependent, approval-dependent, adjudicated) subsumes it. My prompt
   omitted `assent`, so this is my error, not the seat's. Worth re-testing with a corrected prompt.

**Rejected as scope creep.** New facets for onerous/gratuitous, commutative/aleatory,
causal/abstract, and consensual/solemn/real. Each is a real doctrinal axis and none is needed to
*gate a delegated act*, which is what this taxonomy is for. Whether a contract is aleatory does not
change whether an agent may enter it. Adding six facets would add six places for per-facet α to
degrade (V2) against no gain in authorization power. If a jurisdiction needs them for validity, they
belong in that jurisdiction's profile.

**Two caveats on the audit itself.** Its code citations are unverified and at least one looks wrong
— it cites French *Code civil* art. 1104 for commutative/aleatory, where 1104 is the good-faith
provision in the post-2016 numbering. **No article number from this run may reach the paper without
independent verification by someone competent in the tradition.** And the audit is one seat's
recall, not a corpus reading; it sharpens the questions for the corpus prong, it does not settle
them.

**What this validates.** The audit found nothing wrong with the five effects — the facet already
populated — and damaged the two that were still empty. That is the argument for having run it
before phase 2 rather than at phase 5, and it is the only reason `channel` did not harden into
five nodes and a gold standard first.

### Citation audit result, 2026-08-19 — [A-TQ8F] discharged

A primary-source corpus now exists at `~/code/bakobo/civil-law-acts/` (local, committed, unpushed),
built to the `id-law-kit` convention: quote-or-drop, with required `validity` and `authority_tier`
on every item. It holds the Civil Code of Québec in both official languages (3,523 articles each),
the French Code civil (2,896 articles, French original), and the BGB official English translation
(2,506). Full results in that repo's `findings/citation-audit-2026-08-19.md`.

**Of the 25 citations the V-CIV audit produced, 6 were wrong — a 24% error rate.** None was
unverifiable; every cited article existed and was legible, so each failure is a failure of what the
article says rather than of retrieval. I verified three of the six corrections against the corpus
myself rather than accepting the report: French art. 1104 is the good-faith provision, art. 1108 is
commutative/aleatory, art. 1109 is consensual/solemn/real.

  [ F-M2WD ]  **Half the errors trace to superseded law.** Rows 8 and 12 reflect pre-2016 French
  numbering, from before the `Ordonnance n° 2016-131` recodification of obligations. Row 11 claims
  the BGB treats loan as a real contract, which was true before the 2002
  `Schuldrechtsmodernisierung` and is not now — § 607 reads that the lender *agrees to make
  available*, which is consensual, and German law today has no real contract of loan at all.

This is the finding with reach beyond these 25 rows. A model asked about civil-law doctrine recites
the doctrine as it stood before the reform that changed it, fluently and with article numbers
attached. Everything the V-CIV doctrinal prong concluded was produced the same way — which means
**the doctrinal prong's substantive findings are as suspect as its citations, and the corpus prong
is not optional confirmation but the thing that decides.** The triage above stands on its own
reasoning, not on the audit's authority; where it does not, it must be re-derived from the corpus.

It is also a datum for §6's argument. A reasoning model producing verifiable claims in a specialist
domain got 24% of them wrong while sounding uniformly confident — which is the case for a
human-adjudicated gold standard and against treating inter-model agreement as correctness, made
empirically rather than by assertion.

### A second, harder measurement — quote fabrication with the source in the prompt, 2026-08-20

The 24% figure could be dismissed as a recall problem: the model was citing from memory. So the P5
re-extraction (`syntelos/eval/sampling-frame.md`) is the sharper test, because it removes recall
entirely. Two seats were given the 15 tefa archetype files **in the prompt** and asked to extract
acts, each carrying a verbatim quote from the file it came from. The prompt said the quotes would be
checked mechanically and that unquotable acts should be omitted rather than guessed.

**92 of 301 candidate acts — 31% — carried a quote that does not occur in the source file.** Not
misremembered: invented, with the text available in the same context window, under an explicit
instruction that fabrication would be caught.

  [ F-3JRP ]  Fabrication rates differ sharply by model and are not predictable from general
  capability. DeepSeek anchored 70% of its extractions; the GPT seat anchored 48% — it invented the
  majority of its own supporting quotes. Any pipeline that treats seats as interchangeable, or that
  accepts model output without a mechanical evidence check, inherits whichever rate it happened to
  draw.

**One result cuts against my earlier claim and should be recorded rather than buried.** Acts found
by *both* passes verified at 92%; acts found by one verified at 56%. Agreement was strongly
predictive of truth here — which is the opposite of the caution I have applied throughout that
inter-model agreement is weak evidence.

The reconciliation is a real distinction, not a save. Agreement on a **quote drawn from a shared
source** is cheap to be right about and expensive to be wrong about together: two models landing on
the same real passage is unremarkable, while two independently landing on the same *fabricated*
passage is very unlikely. Agreement on a **judgment** — is this act `create` or `modify` — carries
no such asymmetry, because correlated training makes correlated error the expected case. So
agreement is evidence for extraction and remains weak evidence for classification, and V2's α must
still be read against a human gold standard rather than treated as accuracy. The n here is 13
overlapping acts; the mechanism is more convincing than the sample.

**The methodological consequence for everything downstream.** Any stage of this program that
consumes model output must have a mechanical check that the output is anchored in something —
`verify_quotes.py` for extraction, `disqualified.py` for contamination, quote-or-drop for law. Where
no such check is possible, the stage cannot be delegated to a model at all. That is now an empirical
finding twice over, not a methodological preference.

**Two standing rules from this.**

- **Cite Québec first.** The CCQ is officially English rather than translated, publisher-direct, and
  current, and it states the doctrine compactly — art. 704: *"A will is a unilateral and revocable
  juridical act drawn up in one of the forms provided for by law, by which the testator disposes by
  liberality of all or part of his property, to take effect only after his death."* That single
  sentence carries unilaterality, revocability, act-hood, form, and liberality. Juridical acts are
  at arts. 1372, 1371, 2130, 704; classification 1378; form 1385, 1414, 1824, 2814, 2819, 2827;
  nullity 1416, 1417, 1419, 1422; mandate 2130, 2176, 2181.
### Doctrinal verification against the corpus, 2026-08-19

The three accepted V-CIV items that rested on model recall, re-derived from primary text. All three
hold; two are materially different from how the audit stated them, and one of my own restatements
was wrong.

**Claim 1 — `notarized` is a false friend. CONFIRMED, and the reason is not what the audit said.**
The audit located the difference in notarial procedure (drafting, reading, explanation), and I
repeated that plus "executory force." The corpus says the difference is **evidentiary and
procedural-adversarial**. French CC art. 1371: the authentic act *"fait foi jusqu'à inscription de
faux"* — it stands as proof until a party brings the special *inscription de faux* proceeding. CCQ
art. 2818: the officer's recital *"makes proof against all persons."* CCQ art. 2821: *"Improbation
is necessary ... to contradict the recital."* Contradicting an authentic act requires a dedicated
judicial procedure; a common-law notarized document is ordinary evidence, rebuttable in the normal
way. That is a categorical difference, not a procedural nicety.

Two corrections that follow. **Executory force is not in the Code civil** — art. 1369 defines the
authentic act and 1371 gives it probative force; the agent's audit found `force exécutoire` lives in
the Code des procédures civiles d'exécution, outside this corpus, and declined to supply it from
memory. My §6 text above asserted it and was wrong. And art. 1370 shows validity is graded, not
binary: an act that fails to be authentic through the officer's incompetence or a defect of form
*"vaut comme écrit sous signature privée"* — it downgrades rather than voiding.

**Claim 2 — constitutive vs. declarative registration. CONFIRMED, and it is three functions, not
two.** CCQ art. 2941 states them in one sentence: *"Publication of rights allows them to be set up
against third persons, determines their rank and, where the law so provides, gives them effect."*
Opposability, **rank**, and constitutive effect are separable, and the same article adds that
*"rights produce their effects between the parties even if they are not published"* — registration
is about third parties, not the parties. BGB § 873(1) supplies the constitutive case: transfer of
land ownership *"require[s] agreement ... and the entry of the change of rights in the Land
Register."*

  [ F-9GKT ]  **Priority/rank is a function of registration that neither the audit nor my triage
  named.** It is not opposability — two competing registered claims are both opposable and still
  need ordering — and it is not constitutive effect. The requisite vocabulary needs three values
  here, and a system that models registration as a boolean cannot express which of the three a
  given filing buys.

**Claim 3 — the Latin notary breaks the five channels. CONFIRMED, on better evidence than the audit
offered.** Both codes make the notary a public officer: French CC art. 1369, *"reçu ... par un
officier public ayant compétence et qualité pour instrumenter"*; CCQ art. 2813, *"received or
attested by a competent public officer."* But the decisive text is CCQ art. 2814, which enumerates
authentic documents: Parliament documents, government letters patent and orders, court records,
municipal documents, *"public records required by law to be kept by public officers,"* **notarial
acts**, and boundary-marking minutes. The code's own list spans four of my five proposed channels
and carries notarial acts as a co-ordinate category beside them. `notarial` is not reducible to
`private`, `agency`, `tribunal`, or `registry` — established by a legislature's own taxonomy rather
than by a model's opinion.

**A structural finding that vindicates the [D-QW4D] decomposition.** That same art. 2814 shows
authenticity cutting *across* channels — a parliamentary document, a court record, a public register
entry, and a notarial act are all authentic. Authenticity is therefore a property of how an act was
executed, orthogonal to which institution it ran through. Had `form` been shipped as one compound
facet rather than split into `channel` and `requisite`, this would have been inexpressible.

- **Do not cite German law normatively yet.** Légifrance answers with a Cloudflare challenge and
  gesetze-im-internet.de refuses TCP from this host, so the French text came from a third-party
  mirror of DILA open data and the BGB from an Internet Archive snapshot of the official
  translation, manifested `validity: amended` against its own 10 Aug 2021 cut-off. The French mirror
  is verifiable article-by-article against Légifrance by LEGIARTI id, so it is serviceable. The BGB
  is a five-year-old snapshot of a translation of a non-authentic text, which is three removes from
  law; re-fetch from a different network path before the paper relies on it.

---

## 7. Spec hygiene: registry, goldens, CI

The drift E1 found is the argument for all of this. SDA writes `information`; GCD writes `info`.
GCD's `README.md` describes `effects` and `stateKinds` as separate fields; the schema composes them
into `acts`. Both papers cite each other's vocabulary in prose, so neither can be checked.

  [ R-6DHZ ]  **The registry is the source of truth and the paper is generated from it.** Not the
  reverse. A taxonomy that lives in prose cannot be linted, and every drift above exists because it
  currently does.

- **Registry.** One `taxonomy/` tree of YAML — one file per node, carrying id, parent, definition,
  ≥2 positive examples, ≥1 counter-example with the reason ("not this, because…"), and the
  discriminating question against each sibling. The counter-examples are not decoration: E1's ten
  pressure points are all cases where a counter-example would have settled it.
- **Goldens.** `goldens/*.jsonl`, one record per act: source citation (Utah §, GCD file, tefa
  archetype), the full coordinate on every facet, adjudication provenance, and split membership.
- **Worked examples.** Full traces, not fragments: Utina's six demo acts, GCD's five example
  credentials, and a handful of law-derived ones — each showing the coordinate, the derived gate,
  the Custos clause it would bind, and why each facet value beat its nearest rival.
- **CI.** Every node has definition + examples + counter-example. No duplicate ids. Every golden
  validates against the registry. Every path mentioned in the generated paper exists in the
  registry. **Cross-repo:** GCD's schema enums equal the registry's closed facets — this check must
  also run in `bakobo/schema`, or the drift comes straight back. MECE lint: pairwise definition
  similarity above threshold flags an overlap for human review. Frozen eval: classifier α on the
  gold set may not regress.

The generated-paper rule also fixes `syntelos.md:134`, `:251`, and `:274` by construction — those
are exactly the defects a build step catches.

---

## 8. Sequence

Phase 0 is the only one with a hard dependency: [Q-7VXK] absorb/federate/layer and [Q-QW4D] the
form facet's reach both change the registry's shape, so nothing durable should be built before
they're settled.

| Phase | Work | Who | State |
|---|---|---|---|
| 0 | Settle architecture: absorb, faceted, narrow form scope | — | done 2026-08-18 |
| 1 | Registry, linter, CI harness | me | done — 26 nodes, green |
| 2 | Define the 11 SDA/GCD tokens; add modality; add requisite | me | done |
| 2.5 | V-CIV doctrinal audit, then corpus verification of its claims | seats + me | done |
| 3a | Corpus acquisition (P1–P10) | agents | done — 10 populations |
| 3b | Sampling frame + rating protocol, seed pre-registered | me | done |
| **T** | **Telos derivation** — not in the original plan; became necessary once guard 2 forbade grandfathering v1's roots | me + seats | **partition derived, not frozen** |
| 3c | Draw the P1/P2 samples and the 600-act gold subsample | me | **blocked on T** |
| 4 | V1 gold standard | Daniel | not started |
| 5 | V2/V3 reliability + calibration, both traditions | seats | not started |
| 6 | V4 definition-repair loop | me + seats | not started |
| 7 | V5 human ceiling, V6 comparative | Daniel + seats | not started |
| 8 | Paper generated from registry; worked examples; cross-repo CI | me | not started |

**Phase T decomposes, and only the first step is done:**

| T-step | Work | State |
|---|---|---|
| T1 | Derive a partition, blind and bottom-up | done — three independent consolidations |
| T2 | Verbing pass as a semantic check; redraw any root that resists | **next** |
| T3 | Resolve the contested boundaries the three consolidations disagree on | after T2 |
| T4 | Freeze the partition | after T3 |
| T5 | Name the roots against `design/naming-criteria.md` | after T4 — premature before it |
| T6 | Write the roots into `taxonomy/telos/` as registry nodes with discriminators | after T5 |

**Outstanding and unscheduled:** the three v1 paper defects (`syntelos.md:134` garbled paragraph,
`:251` stale `/gov/Identity.Verify` notation, `:274` sentence truncated mid-clause) are still
present. Phase 1 listed "fix the v1 defects" and it did not happen, because the registry-generates-
the-paper approach means they get fixed at phase 8 by construction rather than by hand now. That is
defensible but it should be a decision rather than an omission.

Phase 2.5 is placed before the corpus work deliberately. The doctrinal audit is cheap and can
falsify a closed facet on its own; discovering in phase 5 that `channel` is a common-law artifact
would invalidate a gold standard that cost real human hours to build.

---

## 9. Caveats on the delegated analyses

- The tefa analysis (DeepSeek) leaked scratch notes into its §2 — lines 69–73 of
  `design/sources/e3-tefa-analysis.md` are visible self-talk, not findings. The surrounding content
  checks out against the files it cites, but treat that section's completeness claim as unverified.
- Three seats converging on "purpose and effect are orthogonal facets" is weaker evidence than it
  looks, since all three prompts pointed at the tension. What makes it worth acting on is that they
  reached it from *different* evidence — statutory form-crossing, Custos's byte-derivability axiom,
  and GCD's undefined tokens. I have not independently verified every section citation in E2 or
  every Utah citation in E4; the ones I spot-checked held.
- Percentages in §5 and §6 above are the seats' estimates from a 1-in-14 sample, calibrated against
  a full-population word-frequency table. They are order-of-magnitude, not measurements, and the
  plan does not depend on their precision.
