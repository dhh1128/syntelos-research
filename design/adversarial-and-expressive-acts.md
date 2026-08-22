# Acts the model cannot currently express

2026-08-22, from Daniel's cases: poisoning, the Mona Lisa protest, political protest,
whistleblowing, and Tank Man. Each was offered as a question about classification. Taken together
they locate four gaps, and only the first is a taxonomy problem.

## 1. The state-kind gap covers animals too, and harm is not a new telos

Daniel: *a person and an animal are similar in this regard.* Correct, and it settles the shape of
the missing value. What is absent from state-kind is not `person` but **a living subject that can
be harmed**. Whether that subject is a person or an animal is a *target* property, not a state-kind
property — legally and morally enormous, but the same kind of state is being operated on, and
`sda.md` §4 already puts that sort of difference on the target ("the same coordinates cover wiping a
scratch cache and wiping the customer ledger; only the target tells them apart").

Daniel: *is destroy just a polarity on the care tree?* No — and the answer is better than that.
**Polarity already exists, on the effect facet.** Once state-kind can name a living subject:

- caring = `preserve` or `modify` over `living-subject`
- injuring = `modify` over `living-subject`
- killing = `destroy` over `living-subject`

Harm needs no telos of its own. It is the effect axis doing exactly what it was built for, and the
fact that it works the moment the state-kind gap is filled is evidence the two facets are cut
correctly.

*Are there other examples of this polarity?* Yes, and they are already expressible, which confirms
the pattern sits on effect rather than on telos:

- **Dissipating value** — spending to be rid of value rather than to acquire: `destroy` over
  `resource`. Burning goods to keep prices up, scuttling a vessel, defensive asset-stripping.
- **Destroying information** — `destroy` over `information` or `record`. Legitimate as retention-
  policy deletion or redaction; criminal as spoliation. Same coordinate, and the difference is
  modality and requisite, not telos.
- **Extinguishing authority** — `destroy` over `authority`, which the model already treats as its
  most reserved act.
- **Severing a relationship** — `destroy` over `relationship`.

Every one is the negative pole of a familiar positive act, and none needs a new root.

## 2. But v1's definition of telos presupposes cooperation, and adversarial acts break it

This is the sharper problem the poisoning case exposes, and it is not about state-kind.

`syntelos.md` §3.8 defines telos as *"the potential outcome that all rational stakeholders should
agree embodies the interaction category's raison d'être."* **A murder has no such consensus.** The
victim is not a stakeholder whose agreement can be sought; there is no shared raison d'être. The
same holds for fraud, theft, coercion, and every act whose success requires a counterparty's defeat.

  [ F-5RQW ]  **Telos as v1 defines it is undefined for adversarial acts**, and the expansion to a
  general taxonomy of actions has quietly made adversarial acts in-scope. Two ways out, and they
  cost different things.

  **(a) Restrict scope again** — telos covers cooperative acts, and adversarial ones are named some
  other way. This preserves v1's perspective-neutrality but reintroduces exactly the kind of scope
  boundary this project spent its first phase removing.

  **(b) Redefine telos as the *actor's* end** rather than the *shared* end. This admits adversarial
  acts naturally. It costs `syntelos.md` §3.6, the multiple-perspectives requirement — the reason
  buyer and seller meet at one `/trade/swap` node instead of at `Buy` and `Sell`. Under (b) their
  telei differ and the matching property that motivated v1's design is gone.

Unresolved, and load-bearing: (b) is what the delegation use case wants and (a) is what the
intent-signalling use case wants, and Syntelos 2.0 is now trying to serve both.

## 3. Expressive acts: stakes decoupled from physical effect

The Mona Lisa case. Physically: soup on protective glass. Coordinate: `modify` over `resource`,
trivially reversible, cleaning cost negligible. Stakes by the model's own gate function: near zero.

That is obviously wrong about the act. Its significance is entirely communicative — the physical
component is a *medium*, chosen for its capacity to command attention, and the audience is the
world's press.

  [ F-8DZK ]  **For expressive and symbolic acts, the (effect, state-kind) vector systematically
  understates stakes**, because `sda.md` §4 derives stakes from the target and the target is
  incidental to the act's purpose. Protest, ceremony, desecration, flag-burning, monument removal,
  and performative resignation all share this: cheap physical effect, large consequence.

The same act analysed for telos comes out as advocacy — `promote` under the structural definition,
since sponsorship and a call to action are present. So telos handles it; the **gate model** does not.
This is a defect in stakes derivation rather than in the taxonomy, and it means the gate function
needs an input it does not have: reach or audience, not just blast radius on a target.

Tank Man is the same shape at the limit. Physically: a man stands in a road. Effect: none. Telos:
`protect` by interposition — which the structural definition of protection actually captures, since
he is a barrier between a hazard and its target — plus communication of overwhelming reach. The
model can name what he did and cannot register what it cost.

## 4. Three things a delegation model structurally cannot say

The protest and whistleblowing cases expose gaps that are not taxonomy gaps at all. They are gaps in
what an authority model can represent, and each is a place where the model's frame is the limitation.

**Unauthorised as a deliberate stance.** Civil disobedience is not an act that failed to find an
authorisation; it is an act performed *because* it is unauthorised, asserting a standing the actor
was never granted. The model has exactly two verdicts — permitted, or refused for want of authority
— and no way to say *knowingly unauthorised, and that is the point.* A model built to describe what
a grantor permits cannot describe acting against the grantor's frame.

**Obligations that override the grantor.** Whistleblowing is a `communicate`/`destroy`-confidentiality
act that breaches a duty the grant imposed, in service of a norm the grant never contemplated and
whose whole purpose is to protect against the grantor. GCD's duty `priority` resolves conflicts
*between duties the issuer wrote*. It cannot express *"there exists an obligation that outranks this
grant and did not come from you"* — and statutory whistleblower protection is precisely that
obligation. A delegation model in which the grantor defines every obligation cannot represent
obligations that exist to constrain the grantor.

**Stakes borne by the actor.** `sda.md`'s gates protect the principal and third parties; blast radius
is measured outward. Tank Man's act cost him everything and cost the principal nothing. Self-
sacrifice, whistleblower retaliation, and hazardous rescue are invisible to a stakes model that
measures only harm to others.

## 5. What to do

Nothing here should be acted on inside phase T. Three of the four are outside the taxonomy entirely,
and the one that is inside — the living-subject state-kind — reopens a closed facet.

Ranked by how much they threaten the current work:

1. **F-5RQW (telos undefined for adversarial acts)** is the serious one, because it is a
   contradiction at the definition of the facet being derived right now, and either resolution
   changes what the derivation is producing.
2. **The living-subject state-kind** is a concrete, bounded change, blocked only on Daniel's
   decision to reopen the facet.
3. **F-8DZK (expressive stakes)** is a real defect in the gate model, and belongs in the SDA
   revision rather than here.
4. **The three representational gaps** in §4 are, arguably, correct limitations. A delegation
   credential *should not* be able to authorise civil disobedience; that is what makes it civil
   disobedience. But the model should say so explicitly rather than leaving the reader to discover
   that the vocabulary runs out. Naming a boundary is different from not having noticed it.

---

## 6. Retraction of F-5RQW, and of "unauthorised as a stance"

Both were wrong. Daniel, 2026-08-22.

### 6.1 F-5RQW rests on a misreading of v1

*"All rational actors would agree that the category of murder has a raison d'être, which is to
destroy the life of a person."*

That is what §3.8 says, and I read something else into it. The definition asks for consensus on
**what the category is about**, not consent to it. A buyer and a seller agree that `/trade/swap` is
about transferring assets while disagreeing violently about price; a victim can agree on what murder
is for while obviously not consenting to it. **Consensus on identification is not agreement on
desirability**, and I collapsed them.

  [ D-5RQW ]  **Withdrawn.** Telos is well defined for adversarial acts. Murder's telos is to
  destroy the life of a person; fraud's is to transfer value. Nothing about v1's definition requires
  the counterparty to want the outcome.

### 6.2 And the horizon rule was already doing the work

*"The fact that this could be a step along the way to more final teloses like intimidation, revenge,
and so forth doesn't change the resonance at a basic level."*

That is [D-6PVH rev.2] applied correctly, and more crisply than I applied it. Intimidation and
revenge are further horizons whose realisation needs an audience's uptake, so they are inadmissible
as telos and the act stops at destroying a life. Killing for insurance money is still killing; the
insurance claim is a separate act with its own coordinate.

### 6.3 What actually distinguishes adversarial acts, then

Not telos. *"Financial fraud has the purpose of transferring value, regardless of a deeper
motivation."* Which means fraud and an honest sale **share a telos** and differ elsewhere:

- **fraud** = transfer-value telos, with consent obtained by deception — a *defect in the consent
  requisite*
- **theft** = transfer-value telos, with no consent at all — the requisite absent
- **gift** = transfer-value telos, consent present, reciprocity absent
- **sale** = transfer-value telos, consent present, reciprocity present

The adversarial character lives on **requisite and modality**, exactly where the model already puts
validity and permission, and not on the purpose axis at all. This is the fourth time a distinction
has turned out to belong on a different facet than the one it first appeared on, and by now that
should be the default hypothesis rather than a discovery.

  [ F-2QLJ ]  **This breaks the outward test written for C9.** T2 defined the exchange node as
  *"does consideration pass between parties?"* — which excludes theft, since no consideration passes.
  The node is drawn too narrowly. It should be **transfer of value**, with reciprocity a species
  beneath it and consent a requisite across it. That is a real correction to the T2 table, arrived
  at from a case the corpus never contained, because O\*NET, the protocols, and the steward roles
  catalogue only lawful activity.

### 6.4 Lawful protest is authorised — by a right, not by a grantor

*"Lawful protest is a right; I would hardly say that's unauthorised. Unwanted, maybe."*

Correct, and it dissolves the framing of §4. I conflated *not delegated by a principal* with
*unauthorised*. A right **is** an authorisation; it simply does not originate in a grantor. In
Hohfeldian terms it is a privilege the actor holds of their own standing.

That collapses three of my supposed gaps into one, and states it better:

  [ F-6VTD ]  **The model can only represent authority that flows from a grantor, and cannot
  represent authority that inheres in the actor.** Rights, standing, legal capacity, and
  constitutionally protected liberties are all authority without a delegator. GCD's whole structure
  is issuer → issuee; there is no way to assert *"I act under authority I hold, not authority you
  gave me."*

Whistleblowing is the same gap rather than a separate one: statutory whistleblower protection is a
**right**, not a mysterious duty outranking the grant. The actor is exercising authority the grantor
never held and therefore could never have withheld. Civil disobedience is the limiting case — a
claim of authority the *law* does not recognise, which is why it accepts the sanction.

So the register of gaps is shorter and sharper than §4 claimed:

1. **F-6VTD** — inherent authority has no representation. Covers protest, whistleblowing, and any
   act performed under a right rather than a grant.
2. **Stakes borne by the actor** — unchanged, and genuinely separate. A stakes model that measures
   blast radius outward cannot see self-sacrifice.

"Unauthorised as a deliberate stance" is withdrawn; it described a case the model mislabels rather
than one it cannot express.
