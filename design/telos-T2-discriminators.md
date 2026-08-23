# T2 — rewriting the discriminators as outward tests

Working document, 2026-08-22. Applies [D-2CFX] (every telos node must be externally checkable) to
each candidate root from T1. Each entry: the discriminator the derivation produced, an attempt to
restate it as an outward test, and a verdict.

## The rule that emerged from doing this

Restating a handful of these surfaced a sharper form of the requirement, and it does more work than
the original:

  [ D-6PVH ]  **The outward test must turn on features present at the time of the act, not on
  outcomes that unfold afterwards.**

Two reasons, and they are the same two failures we have already hit.

*Horizon.* A test that appeals to a later outcome is a horizon test wearing observational clothes.
"Did the learner become capable" is not checkable *now* — and by the time it is, the act is long
over and the verifier has gone.

*Counterfactual success conditions.* Several candidate purposes succeed by something **not**
happening. Protection succeeds when harm does not occur; you cannot observe a non-event. So
protection cannot be defined by its success condition at all, and must be defined by the act's
observable structure — *does it install, monitor, or enforce a barrier against an identified
hazard?* That is present-tense and inspectable.

This turns out to be the general repair. Where a purpose resisted an outward test, defining it by
**what the act does** rather than **what the act achieves** rescued it — and where even that failed,
the node dies.

## The rewrites

| # | candidate | derived discriminator (intent-phrased) | outward test (present-tense, structural) | verdict |
|---|---|---|---|---|
| C1 | care | "the beneficiary's condition is the end" | Does the act operate on the body, mind, or living conditions of a person or animal? | **survives** — the patient is the act's object, observable |
| C2 | protect | "the end is a hazard that never materialises" | Does the act install, monitor, or enforce a barrier against an identified hazard? | **survives, redefined** — by barrier, not by non-event |
| C2b | secure vs protect | "the threat is an adversary's intent, not accident" | Does the act's structure presuppose an agent to be defeated — authentication, authorisation, intrusion detection — rather than a hazard to be contained? | **marginal** — often visible, but may be a *target* property rather than a purpose. See below. |
| C3 | know | "something true becomes known" | Does the act acquire, verify, or produce a representation of some state of affairs? | **survives** — there is an inquiry and a result |
| C4 | educate | "the end is a changed person, not a produced fact" | Does the act involve curriculum, sequencing, practice, or assessment directed at a learner? | **survives, redefined** — by pedagogical structure, which is an artifact you can point at |
| C5 | communicate | "success is receipt and shared awareness" | Does the act transmit content to an identified audience? | **survives** |
| C6 | persuade | "the audience becomes more favourable" | Is there a sponsor with an interest in the outcome, consideration paid for placement, or a call to action? | **survives, much narrowed** — becomes *sponsored advocacy*, not *persuasion*. See below. |
| C7 | coordinate | "the end is synchronised action" | Does the act fix a time, place, sequence, or role assignment among two or more parties? | **survives** |
| C8 | produce / maintain | "create something new vs keep an existing thing functional" | Both observable — but the effect facet already carries `create` vs `preserve` | **merge at telos** — the distinction is real and belongs on the other axis |
| C9 | exchange | "reciprocal value is transferred" | Does consideration pass between parties? | **survives** — the strongest node in the set |
| C10 | conform | "conduct kept within a normative boundary" | Is the act a test, audit, attestation, or filing against a *stated external standard*? | **survives** — the standard is a document the act references |
| C11 | adjudicate | "authoritatively resolve a contested question" | Does the act resolve a contested claim through a procedure whose determination binds the parties? | **survives** — forum, parties, determination all observable |
| C12 | belong | "who may belong and interact" | Does the act change who may enter, act, or be recognised within a bounded group? | **survives** — rolls, roles, bans |
| C13 | unite | "a continuing bond is the end" | Does the act establish a formal, registered, or publicly recognised bond between named parties? | **survives, redefined and narrowed** — see below |
| C14 | ecology | "the ecological system is the beneficiary" | Is the object of the act a natural system? | **dies** — passes checkability, fails the verb test; it is a subject area |
| C15 | move | "the end is change of location" | Does the act change the physical location of something? | **survives** — highly observable; whether root or child is a granularity call |

## The four that needed real surgery

**C6 persuade → promote.** The rewrite follows advertising regulation, which has faced exactly this
problem and does not ask about intent. It asks whether placement was paid and whether it was
disclosed. So the node survives only as *sponsored advocacy* — narrower than "persuasion" and
correctly so. Unsponsored argument made in good faith is `communicate`, and that is the right
answer: a taxonomy should not claim to detect rhetoric.

**C13 unite, and what happens to matchmaking.** Defining the node by *formal, registered, publicly
recognised bond* makes it checkable — marriage, adoption, partnership are all matters of record. But
it narrows sharply: the matchmaker's own acts (screening candidates, arranging an introduction,
negotiating terms) are individually acts of coordination and communication, and fall outside.

That is the right outcome and it does not lose Daniel's case, but it does surface a distinction the
model has not yet named:

  [ F-9WTC ]  **Telos-of-the-grant is not telos-of-the-act.** A matchmaker delegated to negotiate a
  marriage is granted authority toward `/unite`, while nearly every act they perform is coordination
  or communication. GCD already carries these separately — `a.constraints.goals` alongside
  `a.constraints.acts` — but nothing in the model states the relationship, and the T1 derivation
  clustered *acts*, so it has been deriving act-telos throughout. Whether the tree serves both, or
  whether goals need their own vocabulary, is unresolved and load-bearing for delegation.

**C2b secure vs protect.** The outward test mostly works — authentication and intrusion detection
look different from guards and backups. But the distinction may be a property of the **threat
model**, which is a target attribute, not of the purpose. Same shape as the `create`/`preserve`
duplication in C8: a real distinction sitting on the wrong axis. Recommend one `protect` node with
threat type as a parameter, pending T3.

**C14 ecology dies, and on the verb test rather than the checkability test.** "Is the object a
natural system" is perfectly observable — but that makes it a *subject area*, which is the UNSPSC
error v1 §2.2 names. Its acts redistribute: research on pollution is `know`, clearing fallen timber
is `maintain`/`provide`, sealing abandoned wells is `protect`.

## Where this leaves the count

Thirteen candidates in, ten or eleven out: `care`, `protect`, `know`, `instruct`, `communicate`,
`promote`, `coordinate`, `provide`, `exchange`, `conform`, `adjudicate`, `belong`, `unite`, `move` —
minus `ecology` (dissolved), minus `secure` (folded into `protect` pending T3), minus one of
`produce`/`maintain` (merged). `move` and `instruct` are granularity calls rather than existence
calls.

Notably **nothing died from the checkability rule alone.** Two nodes were narrowed by it (`promote`,
`unite`) and one was redefined by it (`protect`); the only outright casualty fell to the verb test.
That is mild evidence the derivation was sounder than the intent-phrased discriminators made it
look — the extensions were largely right and the prose describing them was wrong, which is what
[the T1 layering argument] predicted.

## Next

Adversarial probe per surviving boundary: *produce two acts a competent observer could not assign
between these two nodes using only observable features.* A boundary that falls to it is not
checkable in practice whatever the table above claims, and the probe's output doubles as the
counter-examples and near-misses the linter requires on every node.

---

## Revision of D-6PVH, 2026-08-22

Daniel's counter-example: a poisoner serves a meal; the victims die days later. Under the rule as
written, only features present at the time of the act count, and the act is "serving food." That is
plainly wrong about the telos, and the rule needs repair rather than defence.

The repair is not to admit outcomes generally. It is to distinguish **outcomes the act determines**
from **outcomes the act merely contributes to.**

  [ D-6PVH, rev.2 ]  **The outward test may appeal to a later outcome where the act causally
  determines it and the intervening chain is mechanism. It may not appeal to outcomes that require
  further acts, another party's uptake, or repetition to come about.**

Applied to the two cases:

*Poisoning determines its outcome.* The meal contains death cap; nothing further need be done by
anyone. The intervening days are physiology running, not agency. And crucially the determining
feature — what is in the food — **is present at the time of the act and is inspectable**. So the
outcome is admissible, and the telos is killing rather than feeding.

*Instruction does not determine character.* At the time of a lecture there is no feature that makes
it character-forming. The outcome requires the learner's uptake, repetition, and a hundred other
acts by other people. The chain passes through further agency, so the outcome is inadmissible and
`instruct` must still be defined by its structure — curriculum, sequencing, assessment.

This is the law's own distinction and it is worth borrowing the vocabulary: an intervening free human
act (*novus actus interveniens*) breaks the chain; a natural process does not. Digestion does not
break it; the learner's decision to study does.

The revised rule also settles the middle cases consistently with what T2 had already concluded on
other grounds. Persuasion requires the hearer's uptake → outcome inadmissible → the node survives
only as structurally-defined `promote`. Protection's non-event is not determined either → still
defined by the barrier. A marriage registration constitutes the bond rather than causing it later →
no horizon question arises.

## What the counter-example exposes about the facets

Following it through produced something larger than the rule fix.

  [ F-3XNM ]  **The state-kind facet cannot express an act on a person.** Its six values are
  `information`, `record`, `commitment`, `authority`, `resource`, `relationship`. A poisoning is
  `destroy` over — what? A patient is not a `resource`; that is both wrong and dehumanising. Neither
  is a person `information` or a `commitment`. **There is no state-kind for a human being.**

This is not a corner case. It means the entire `care` root — the most strongly evidenced concept in
the whole derivation, 14–15 of 15 passes, thousands of acts — has no coordinate on the state-kind
axis. Treating a patient, feeding someone, safeguarding a dependant: none of them can be located.

The explanation is provenance, and it fits everything else we have found. `sda.md`'s six state-kinds
were derived from *delegated organisational authority*, where acts fall on systems, records, and
grants. That corpus contains no medicine, no bodily care, no violence. Once P9 brought in the whole
economy, the facet ran out — the same way v1's roots ran out once the corpus stopped being
interaction protocols.

Consequences:

- A seventh state-kind is probably required — `person`, or `subject`, or `body` — and naming it is
  delicate for the same reasons `resource` is wrong.
- The closed sets in `taxonomy/state-kind/` are `status: draft` and would need reopening, with the
  cross-repo GCD check following.
- This is also where the delegation model is most consequential and least developed: acts on persons
  are exactly where the affordance constraints of §7.2 and the subject-as-verifier idea apply, and
  the model currently cannot even name their object.

Recorded here rather than acted on. It is a change to a facet the T-phase was not chartered to
touch, and it wants Daniel's decision before anything moves.

---

## T3 rulings, 2026-08-23

### Applied — three merges/deaths I am confident in

**C8 `produce` / `maintain` → MERGE.** The effect facet already carries `create` versus `preserve`.
Splitting at telos would encode one distinction on two axes declared orthogonal, which is precisely
the objection that killed `representing`. One node; the effect coordinate distinguishes building a
thing from keeping it working.

**C2b `protect` / `secure` → MERGE.** Accidental versus adversarial is a property of the **threat
model**, which is an attribute of the target, not of the purpose. Same shape as C8. One `protect`
node, defined by the barrier it installs; threat type is a parameter. Note this does not lose
anything a delegation needs — "may guard against intruders but not against fire" is expressible as a
target constraint.

**C15 `move` → DIES.** Not a granularity call after all: it fails the *purposes-not-mechanisms*
test. Relocation is **how** you achieve something else — moving a patient serves care, moving freight
serves availability or exchange, evacuating serves protection. A node that appears under many
purposes is a mechanism. Its acts redistribute by what the relocation is for.

**C9 → `transfer`, with two species.** Settled by Daniel's case: *a grandmother giving a birthday
gift isn't reciprocal.* The parent is **transfer of value**; reciprocity is a checkable species
beneath it — did consideration flow back?

    /transfer            value moves from one party to another
    /transfer/trade      …with consideration flowing back
    /transfer/give       …with none

Theft is **not** a third species. It is `/transfer` with the **consent requisite absent** — a
validity defect, not a kind of transfer — which keeps it consistent with fraud (consent obtained by
deception) and preserves the finding that adversariality lives on requisite and modality.

### Not applied — two I am genuinely unsure of

**C10/C11 governance — one root or two?** Both outward tests work: *conform* asks whether the act
tests conduct against a stated external standard; *adjudicate* asks whether it resolves a contested
claim through a binding procedure. Two of three consolidations split it. But the boundary blurs in
the middle: a regulatory enforcement action both applies a standard **and** issues a binding
determination, and much of what a regulator does sits exactly there. I can argue either way and have
no confident call.

**C13 `unite` / `belong` — separate or one?** Both are now checkable — a formal registered bond
between named parties, versus a change in who may enter or act within a bounded group. Evidence for
the split is 5/15, which settles nothing. The case against separating: a marriage could be read as
membership in a two-person group, making them one concept at different scales. The case for: the
acts, the instruments and the law are all different, and the relational-delegation statutes regulate
one and not the other. I lean toward separate, weakly, and would not defend it hard.
