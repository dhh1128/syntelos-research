# Stress cases against the frozen partition

Daniel's adversarial set, 2026-08-24, classified against the T4 outward tests. Two results: five
defects in the tests, and confirmation of his hypothesis about simultaneity.

## 1. His hypothesis is right, and the model already works this way on another axis

*"Possibly the way to resolve multiple polarities is to say that 2 or more things are being done at
the same time?"*

Yes. `sda.md` §4 already does exactly this for the other axes — an act is a **vector** of
(effect, state-kind) coordinates, and its gate is the join, the strictest any coordinate demands.
Filing a tax return is `create`-in-`record` *and* `create`-in-`commitment` in one move. Telos was set
`multi: false` in `facets.yaml` by inheritance from v1, where one interaction had one telos, and
these cases show that does not survive the expanded scope.

  [ D-3HBK ]  **Telos becomes multi-valued.** An act may carry more than one telos simultaneously,
  and its gate is the join.

The obvious worry — that this destroys MECE — does not hold, and it is worth stating why because the
same confusion will recur. **MECE is a property of the partition, not a constraint that each act
receives one label.** Two categories are mutually exclusive when their *definitions* do not overlap,
not when no act can instantiate both. `record` and `commitment` are mutually exclusive state-kinds
and a tax filing occupies both. Same here.

## 2. Five defects in the outward tests

Each was found by a case, and each is a genuine hole rather than a hard call.

  [ F-7PQD ]  **`protect` covers prevention but not rescue.** Its test asks whether the act
  *installs, monitors, or enforces a barrier against an identified hazard*. Rescuing a kitten from a
  tree removes a subject **from** a hazard; no barrier is installed. Extraction, evacuation, rescue,
  and release are all outside the test as written, which is plainly wrong. The test needs to cover
  interposing a barrier **or** removing a subject from harm's reach.

  [ F-2NVJ ]  **`communicate` does not distinguish authoring from relaying.** A courtroom interpreter
  transmits content to an identified audience and satisfies the test exactly, while originating none
  of the content. Translators, interpreters, messengers, relays, and repeaters all pass. Whether
  relaying is a species of communicating or a distinct purpose (*enabling* communication between
  others, which is nearer `coordinate`) is unresolved, and it matters for delegation: a principal
  may well authorise relaying and not authoring.

  [ F-6CTX ]  **`belong` covers changing membership but not exercising it.** Its test asks whether
  the act *changes who may enter, act, or be recognised* within a group. Attending a caucus does not
  change membership — it exercises it, or usurps it. So the entire act-class of **participating** is
  uncovered: attending, voting within a body, speaking in session, taking part. This is the larger of
  the five, because participation was one of the strongest recurring concepts in T1 (9–10/15) and the
  T2 rewrite silently narrowed it to administration.

  [ F-8KMR ]  **Receptive acts fit awkwardly.** Accepting an anonymous complaint is mostly *not
  refusing*; the HR officer's act is receptive. Every test in the partition is phrased around what an
  actor does. Receiving, admitting, accepting, and tolerating are real, governable acts — an HR
  intake duty is exactly the sort of thing a delegation imposes — and the tests do not reach them.

  [ F-5JWN ]  **"Being" is not act-shaped.** *Be an anonymous whistleblower* is a status, not an act.
  The act underneath is *disclose wrongdoing without attribution*. This is really a corpus-extraction
  rule rather than a taxonomy defect, but the sampling frame's extraction rule should say so: a
  status must be restated as the act that constitutes it, or dropped.

## 3. The classifications

Multi-valued where the case demands it, per D-3HBK.

| case | telos | notes |
|---|---|---|
| graft artificial skin on a burn patient | `care` | Less ambiguous than intended. The object decides — the act operates on the patient's body. The graft was *made* elsewhere; installing it is care. |
| rescue a kitten from a tree | `care` | Exposes F-7PQD. `protect` should reach this and does not. |
| advocate for a minor in a deportation proceeding | `communicate` + `protect` | Also a clean validation: this is the paradigm *representing* case, and because representation was moved off the telos axis to the relation facet, the act classifies without strain. |
| translate for a refugee in court | `communicate` | Exposes F-2NVJ. Also arguably `conform`, since courts *require* an interpreter. |
| accept an anonymous harassment complaint (HR) | `know` | Exposes F-8KMR. Intake is receptive; investigating it later would be `conform`. |
| interview a whistleblower (journalist) | `know` | Pull toward `communicate` is anticipatory — publication is a later, separate act. The horizon rule working correctly. |
| be an anonymous whistleblower | `communicate` (+ `protect`) | Exposes F-5JWN. Restated as *disclose wrongdoing without attribution*. |
| attend a caucus while unregistered | `belong`?? | Exposes F-6CTX. Uncovered as the test stands. |
| submit a regulatory filing | `conform` + `communicate` | The clearest dual. `conform`'s test names *filing* explicitly, and `communicate`'s test is satisfied too. |
| audit a regulatory filing | `conform` + `know` | The boundary T4 already flagged, confirmed live. |
| file taxes for a client | `conform` (+ `transfer` if payment accompanies) | Delegation handled off-axis by the relation facet. |
| pay a dowry or bride price | `transfer` + `unite` | Best case in the set — see below. |
| administer a test in a double-blind trial | `know` + `care` + `conform` | Triple. The for-profit framing hints at tension *between* the telei, which the join-gate would surface rather than hide. |

## 4. Dowry, and a question the partition cannot answer

`transfer` + `unite` is right, and then the species question bites: is a bride price `trade`
(consideration flowing back) or `give` (none)? The answer is **culturally contested** — that is
substantially what is disputed about the institution, by its participants.

  [ F-4RDM ]  **Some species distinctions are contested by the participants themselves, not merely
  hard to observe.** `trade` versus `give` asks whether consideration flowed back, which presumes the
  parties agree on what was exchanged. In dowry, bride price, gift economies, and reciprocal
  obligation systems, that is exactly what is at issue. A verifier can observe that value moved and
  cannot observe, even in principle, whether the participants take it to be reciprocal.

This is not the intent problem — nothing hidden is being inferred. It is that the *social fact* is
indeterminate. The honest resolutions are to classify at the parent (`transfer`) and leave the
species unstated, or to treat the species as an assertion by the classifier rather than a finding.
Either way the paper should carry it, because a Western-derived reciprocity test applied confidently
to non-Western institutions is precisely the failure mode a jurisdiction-invariance claim is supposed
to prevent.

## 5. What this costs

The freeze holds structurally: no root died, no boundary was shown to be spurious, and the two
cases most likely to break the partition (advocacy, double-blind trial) classified cleanly once telos
went multi-valued.

But three outward tests need rewriting (`protect`, `communicate`, `belong`), one act-class is
entirely uncovered (participation), and one extraction rule needs adding. That is a T4 amendment
rather than a re-freeze — the extensions were right and the tests describing them were too narrow,
which is the same failure mode as the T1 discriminators and should probably have been anticipated.

---

## 6. Military objectives, and a hole with a traceable cause

Daniel: *"what would we say about military objectives? Protecting is one goal, but attacking is
another..."*

The partition has no answer. `protect` is defined as installing or enforcing a **barrier against an
identified hazard** — it is the shield. There is nothing for **being** the hazard deliberately.

Attacking cannot be resolved into the existing set:

- Not `protect`. Offensive action in service of eventual safety is a *horizon* claim, and requires
  contingency the act does not determine — inadmissible under [D-6PVH rev.2].
- Not `transfer`, except incidentally when territory or materiel changes hands.
- Not `judge`. Judging issues the determination; enforcing it by force is a different act, and the
  T1 consolidations quietly absorbed enforcement into governance, which now looks like a mistake.

  [ F-9BKW ]  **A whole act-family is missing: applying or threatening force to compel or
  incapacitate a non-consenting party.** Attack, arrest, detain, seize, subdue, punish, sanction,
  deter, execute a judgment, use reasonable force. A checkable test is available and unremarkable —
  *does the act apply or credibly threaten force against a party who has not consented?* — so this is
  not a hard case. It is an absent one.

That it is absent from a taxonomy aimed at **governance** is serious. The state's monopoly on force is
the central fact of governance, and delegated coercive authority — police, military, bailiffs,
security contractors, use-of-force policy — is the highest-stakes delegation there is. A model that
can express "may sign contracts up to $10,000" and cannot express "may use force" has a hole where
its hardest problem should be.

### Why the derivation could not have found it

Checked rather than assumed, and the cause is exact. `tools/build_telos_sample.py` draws from P5
(steward roles), P8 (protocols and tools), P9 (O\*NET), and P10 (relational acts). **P1 (Utah Code)
and P2 (Civil Code of Québec) are not in the list.** The two corpora containing arrest, detain,
seize, prosecute, enjoin, commit, and punish were never in the telos pool.

A probe over the 1,076-act sample returns 27 apparent hits for coercive verbs, and inspection shows
every one is a false positive — `determine` matching `deter`, and "get l7 attack data" as a network
term. **Genuine coercive acts in the pool: zero.**

  This is the **fourth** time a corpus's selection principle has produced a hole that looked like a
  finding. The v1 simulated scrape measured a model's priors. Four instrumental corpora agreed about
  `/relate` because all four inventory instrumental activity. The social APIs missed mourning because
  an API holds what someone found it profitable to build a button for. And now the telos pool missed
  coercion because the legal corpora were assembled and then not used. The frame's rule — *every
  population states what its selection principle omits* — was written after the third occurrence and
  did not prevent the fourth, because the failure this time was not in a population's contents but in
  which populations were **drawn from**.

  [ R-7QSD ]  The frame needs a second rule to match: **record which populations feed each
  derivation, and justify every omission at the point of drawing** — not only at the point of
  acquisition.

### The fix is a supplementary pass, not a hand-added node

Adding `coerce` by hand would treat the symptom. If an entire family went missing because two
corpora were absent, others may be missing for the same reason — procedural acts, evidentiary acts,
ceremonial and status-conferring acts are all heavily represented in statute and thinly represented
in work catalogues.

So: draw a legal-corpus sample from P1 and P2, run it through the same blind batch pipeline, and
consolidate the result **against** the frozen partition — asking what it contains that the partition
cannot express. That is cheap, it reuses machinery that already works, and it answers the general
question rather than the one case Daniel happened to raise.

The freeze stands in the meantime, marked incomplete rather than wrong: nothing in it is refuted by
this, and it is now known not to be collectively exhaustive.

---

## 7. Reykjavík: a second missing root, and why trust-building is not a telos

Daniel, 2026-08-25, from the 1986 Reykjavík summit: strategic moves in the SDI and submarine
negotiations, then Reagan's request that a defector's sister be allowed to visit her brother, backed
by his personal word that she would return.

### 7.1 Negotiation has no home, and `agree` is missing

Test the negotiating moves against the frozen ten. Not `transfer` — no value moves, and an arms
control treaty transfers nothing. Not `coordinate` — nothing about time, place, sequence or role.
Not `communicate` — that is the medium, not the purpose. Not `conform` — no external standard is
being tested against. Not `judge` — no third party binds them; they bind themselves. Not `belong` —
no group membership changes.

  [ F-6WDN ]  **A second act-family is missing: establishing a mutual or unilateral binding
  undertaking.** Treaties, contracts, promises, covenants, settlements, ceasefires, alliances,
  pledges, guarantees. v1 had this as `/trade/deal` — *"reach an agreement on malleable terms"* — and
  the derivation lost it, because `transfer` was drawn around value movement and pure
  commitment-making moves no value.

The outward test is easy and satisfies [D-2CFX] without strain: *does the act create, modify, or
discharge an obligation binding its maker?* The obligation is the observable — it is what the effect
facet already calls `commitment`, and this is the telos that answers *what for*.

Note what this does to `unite`. A marriage is a formal registered bond (`belong/unite`) **and** a
mutual undertaking (`agree`); a treaty is the second without the first. Under [D-3HBK] that is
unremarkable — both labels apply — and it is mild evidence the multi-valued decision was right, since
a single-valued telos would have forced a false choice.

**Strategic moves within a negotiation are not separately modelled, and should not be.** Holding a
position, linking issues, walking out, making a concession contingent — these are tactics, and
enumerating them is exactly what `syntelos.md` §3.9 warns against. The telos is `agree`; the tactics
are parameters of how it is pursued. A refusal is the exception and is already covered: refusal is
first-class on the modality facet.

### 7.2 The visit, and why "build trust" cannot be the telos

Daniel: *"This is some kind of alignment, but I'm not sure it's 'belong'. It's a move designed to
show good will and build trust. Not sure where that goes."*

The puzzlement is the horizon rule working, and the answer is the same shape as persuasion. **Trust
is a mental state in another party, produced by their uptake.** It is not determined by the act, it
requires Gorbachev to be persuaded, and it is not observable at act time — so under [D-6PVH rev.2] it
is inadmissible as a telos, exactly as *form character* and *change disposition* were. Trust-building
is to promising what persuasion is to informing: the downstream effect, not the act.

What is fully expressible is the act itself, and it is `agree` in its unilateral species: **Reagan
made a specific, costly, publicly verifiable undertaking.** Every element is observable at the time —
a named commitment, a determinate performance condition (does she return), and a reputational cost to
defection that both parties could see. Gorbachev's permission is a separate act, `modify` over
`authority`, granting an exit he had previously withheld.

So the model can name every move and cannot name the point of them, which is right rather than a
defect. What made the gesture work was not any property the taxonomy should try to encode; it was
that the undertaking was **small enough to accept and cheap enough to verify.** Low stakes, high
checkability — and interestingly those are the two variables `sda.md`'s gate function already reads,
used here in the opposite direction. A gate uses low stakes to avoid asking a human; Reagan used low
stakes so that a human could say yes.

### 7.3 Two missing roots, one cause

`coerce` [F-9BKW] and `agree` [F-6WDN] were both found by a case rather than by the corpus, and both
are governance-central: the state's monopoly on force, and the power to bind. Contract formation is
everywhere in statute and treaty law, and arrest and prosecution are everywhere in criminal
procedure — and P1 and P2 were never drawn into the telos pool.

Two independent confirmations of the same diagnosis raise the prior considerably that the
supplementary legal pass will surface more. It should run before T5, not after: naming a partition
that is about to gain two or more roots is the waste the phase ordering exists to avoid.

---

## 8. Back-testing v1's 47 leaves against the twelve roots

2026-08-25. Every second-level category from `syntelos.md` §5, mapped onto the frozen ten plus
`coerce` [F-9BKW] and `agree` [F-6WDN]. This is a coverage test the derivation could not perform on
itself, because v1's leaves were deliberately kept out of the blind passes.

**Both new roots are confirmed by leaves that had no home without them.** `/trade/deal` — *"reach an
agreement on malleable terms"* — is `agree` and nothing else. `/govern/enforce` and `/govern/process`
are `coerce`. Three of v1's forty-seven leaves were unplaceable an hour ago.

**Thirty-eight leaves fit without strain.** All of `/care`, `/serve`, `/align`, `/operate`, most of
`/share`, and most of `/trade` and `/govern` map cleanly, several to more than one root now that
telos is multi-valued: `/trade/lend` is `transfer` + `agree`, `/govern/identify` is `know` +
`conform`, `/govern/settle` is `judge` or `agree` depending on whether a third party determines it.

### The failures cluster in one branch

| v1 leaf | problem |
|---|---|
| `/relate/play` | **No root.** Recreation undertaken for its own sake. Not `care` (not wellbeing), not `communicate`, not `coordinate`. |
| `/relate/celebrate` | **No root.** Marking an occasion by conventional observance — ceremony, ritual, commemoration. |
| `/relate/seek` | **Awkward.** Seeking a connection is not `belong` (nothing changes), not `coordinate`, and only weakly `know`. |
| `/relate/chat` | **F-6CTX.** Sustaining a connection. `communicate` fits structurally while missing the point, and `belong` only covers *changing* membership. |
| `/govern/vote` | **F-6CTX, from the other direction.** Casting a ballot exercises membership; it does not change it. |

Four of `/relate`'s four leaves are problematic, and it is the only branch where that happens.

  [ F-3MKC ]  **`/relate` is where v1 covers ground the derived partition does not**, and this is a
  second, independent confirmation of Daniel's judgment in [D-8MRC]. He retained the root against my
  recommendation and against a 5/15 evidence count; the back-test now shows the derived partition is
  weakest in exactly that branch, for the same reason it was weak in the corpora — play, ceremony and
  companionship are not paid work, not protocol operations, and not statutory acts.

  [ F-6CTX ]  **Confirmed twice more.** `/relate/chat` and `/govern/vote` are both participation
  rather than membership-administration, and they arrive from entirely different branches of v1.
  Whatever repairs `belong`, it must cover exercising a standing as well as conferring one.

### Two candidate roots, both plausibly checkable

- **play / recreate** — a rule-governed or expressive activity undertaken with no external product.
  Checkable in the negative: is there a deliverable? Games, sport, and leisure have none.
- **celebrate / observe** — marking a designated occasion by conventional form. Ceremony is
  *unusually* observable, since public conventional form is what makes a ritual a ritual rather than
  a private feeling. Pairs with the mourning gap [F-7CDW], which is the same family.

Neither should be added by hand. They go into the supplementary pass as candidates to be tested, and
that pass now has a clear brief: it must draw from **P1 and P2** for the coercion and agreement
families, and from a corpus that actually contains leisure and ritual for these two — which P10
touched only glancingly, at 5 play acts and 17 ceremony acts.

### Marginal, and worth watching rather than acting on

`/trade/hold` (escrow, custody, safekeeping) sits uneasily between `protect` and `provide`.
`/share/perform` (broadcasting an artistic experience) satisfies the `communicate` test while
"expression" surfaced as its own cluster in three T1 batches. `/govern/advocate` is `promote` only
where sponsorship is present, and unsponsored advocacy falls to `communicate`, which may understate
it.
