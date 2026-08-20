# Naming the telos roots — a separate problem

Draft 2026-08-20. Written because the derivation's output was being read as if it had settled names,
which it did not and could not.

## The distinction this document exists to hold

The chunked derivation established two things about each root: its **extension** (which acts belong
to it) and its **discrimination** (the question that separates it from its nearest neighbour). Those
are semantic findings backed by recurrence counts across 15 independent passes.

It established **nothing about names.** `care`, `provision`, `conformity` and the rest are labels the
seats happened to emit while describing groups. They are working handles, and treating them as
results imports one model's vocabulary into a standard by accident.

So: **the partition is a finding; the names are a design decision**, taken later, against criteria
stated in advance, and revisable without disturbing the semantics. Until then every label in the
plan is provisional and should be read as `<root-7>` with a gloss attached.

A concrete cost of having conflated them: the plan's comparison against v1 was written as
`/care` → `care`, `/govern` → `justice` + `conformity` + `protection`. That reads as though v1's
`/care` survived and v1's `/govern` split. What the evidence supports is a claim about
**extensions** — the acts v1 filed under `/govern` distribute across three derived groups — and it
is silent on whether any of those groups should be called `justice`. The comparison has been
restated extensionally in the plan.

## Criteria

Grouped by kind, because they are different kinds of thing and a flat ranked list obscures that.
Only group A binds absolutely. **B through E trade against each other**, and naming is a
multi-criteria compromise rather than a checklist — the tensions are noted where they bite.

### A. Hard constraints

1. **Identifier syntax.** Machine-friendly kebab-case ASCII matching `^[a-z0-9]+(-[a-z0-9])*$`,
   compared case-insensitively after trimming (v1 §4.1). The paths are identifiers.

2. **Verbs, not nouns.** Settled 2026-08-20 — see the section below, which also treats this as a
   semantic test rather than only a naming rule.

### B. Semantic fidelity

3. **Precision.** The name should pick out the category's actual extension, not a near approximation
   that a reader will over- or under-read. This trades directly against terseness (C5): the short
   common word is usually the vaguer one, and the precise word is usually longer and rarer.

4. **No collision with the other facets.** The coordinate carries telos alongside `effect`
   (`observe`, `create`, `modify`, `preserve`, `destroy`), `state-kind` (`information`, `record`,
   `commitment`, `authority`, `resource`, `relationship`), `modality`, `channel`, and `requisite`.
   A telos root named for information or relationship sits confusingly beside a state-kind of
   nearly the same word. A reader who has to ask which axis a word is on has been failed by the
   naming.

5. **No misleading reuse of a v1 name.** Where a derived group's extension differs from a v1 root,
   reusing that root's name is worse than coining a new one, because implementers will assume
   continuity that is not there. Reuse only where the extension is genuinely close, and say so.

### C. Ergonomics

6. **Terseness.** Paths get typed, read aloud, and put in table columns. v1's roots are uniformly
   one or two syllables; `conformity` and `participation` are five and six. Prefer a short word
   where the definition can carry the precision the short word lacks.

7. **Memorability and pronounceability**, including by non-native speakers.

8. **Disambiguation under abbreviation.** People shorten names in policy files, logs, diagrams and
   speech whether or not a spec sanctions it, so the set should degrade gracefully when shortened.
   *Distinct initial letters are one tactic for this, not a requirement* — distinct first syllables
   or distinct short prefixes serve as well, and a hard one-letter rule would badly over-constrain a
   thirteen-member set. The current labels do cluster (five `c`, four `p`), which is worth knowing
   as a pressure on the search rather than as a disqualification.

### D. Social and rhetorical

9. **Neutral connotation.** A label should not editorialise about its own category. `conformity`
   carries a pejorative shade its definition does not; `persuasion` reads as manipulation.

10. **Political and cultural sensitivity.** Names are quoted in argument and adopted by people with
    their own commitments. A term that is contested, loaded, or reads as taking a side in someone
    else's dispute imports that fight into the standard. `justice` is the clearest current risk:
    freighted, far broader in ordinary use than the group it labels, and unavoidably political.

11. **Cross-linguistic legibility.** This is proposed as an international standard. Prefer words
    with stable cognates or plain equivalents; avoid ones whose English sense is idiomatic. A check
    against French and German is free, given the civil-law corpus already in hand.

### E. Set-level coherence

12. **Parallelism and consistency.** This is a property of the *set*, not of any name, and it is
    the one most easily lost by naming roots one at a time. v1 has it: eight single common verbs,
    same register, same grammatical form, same level of specificity. A set mixing `care` with
    `authoritatively-resolve` is incoherent even if each name is individually defensible. Parallelism
    can pull against precision (B3), since forcing every root into one grammatical shape may
    distort the one root that does not fit — when it does, that is worth noticing, because it is
    often the category rather than the name that is wrong.

13. **Even granularity.** Roots should sit at comparable levels of abstraction. A set where one
    name is far more specific than its siblings signals a partition problem, not a naming problem.

## Procedure

Name after the semantics are frozen, not before, and treat it as its own pass: propose candidate
names per root against these criteria, check the initial-letter set as a whole rather than per root
(it is a global constraint and greedy per-root choice will fail it), and record why each name won.
Names are cheap to revise before publication and expensive after, which argues for doing this
deliberately and late rather than inheriting whatever the derivation emitted.

## Open

Criterion 2 is settled, which fixes the shape of every candidate: all roots are verbs. What remains
open is the consequence — the verbing pass has to run *before* the partition is frozen, because
roots that resist verbing are evidence of a mis-drawn category rather than of a stubborn name. At
least two current groups are already suspect on that test (see criterion 2), and both are among the
weakest by recurrence, which is suggestive rather than conclusive.

Also open: how much weight the ergonomic and social criteria (C, D) get against semantic fidelity
(B) when they conflict — which they will, since the precise word is usually the long one and the
neutral word is usually the vague one. That is a judgment about who the standard is for, and it is
Daniel's to make rather than something these criteria can settle among themselves.

One procedural note that follows from criterion 12: because parallelism and disambiguation are
properties of the whole set, the naming pass cannot be run greedily root by root. Candidates have
to be proposed for all thirteen and then evaluated as a set, with at least two full alternative
sets compared, rather than a single set patched name by name until nobody objects.
