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

Ordered by how much they constrain. The first two are inherited and non-negotiable; the rest trade
off.

1. **Conformance to v1 §4.1.** Machine-friendly kebab-case ASCII matching
   `^[a-z0-9]+(-[a-z0-9])*$`, compared case-insensitively after trimming. Non-negotiable; the paths
   are identifiers.

2. **Verbs, not nouns. Settled 2026-08-20.** v1 §4.1 already says category names "are verbs that
   describe the telos," and every v1 root obeys it — `relate`, `share`, `care`, `serve`, `align`,
   `trade`, `operate`, `govern`. Nearly every derived label breaks it: `knowledge`, `communication`,
   `provision`, `conformity`, `exchange`, `justice`, `participation`, `persuasion`, `union`,
   `ecology`, `coordination` are all nouns.

   Daniel's ruling, and it is not a style preference: this is a taxonomy of **actions**, so noun
   categories are wrong on their face. A telos is an end an actor *pursues*; a verb names the
   pursuing and a noun names the thing. `/knowledge` invites reading the root as a subject area,
   which is precisely the category error v1 §2.2 levels at UNSPSC — it "classifies the *direct
   object* of the sentence, but lacks the *verb*." A taxonomy of acts that names its roots with
   nouns has committed the error it was built to correct.

   **This is also a semantic test, not only a naming rule.** A category that resists verbing is
   often a category that was mis-drawn. `protect`, `exchange`, `coordinate`, `care` verb without
   strain. `ecology` does not — the underlying group is really *sustain an ecosystem*, and `sustain`
   may not be distinct from protection or provision, which would mean the ~3/15 root is a subject
   area masquerading as a purpose. `conformity` verbs to `conform`, which describes the *governed
   party* rather than the actor, suggesting the group is drawn from the wrong vantage. Run the
   verbing before treating the partition as final, and treat every root that resists as a candidate
   defect in the semantics rather than a hard naming problem.

3. **Distinct initial letters.** Abbreviation happens whether a spec sanctions it or not — in
   policy files, log lines, diagrams, conversation. Thirteen roots need thirteen distinct initials.
   The current labels have five in `c` (`care`, `communication`, `conformity`, `coordination`,
   plus `commerce` as an input name), four in `p` (`protection`, `provision`, `participation`,
   `persuasion`), and two in `e` (`exchange`, `ecology`). Unusable as it stands, and it is a real
   constraint on the naming search rather than a nicety.

4. **Terseness.** Paths are typed, read aloud, and put in tables. `conformity` and `participation`
   are five and six syllables against v1's uniformly one-or-two. Prefer short words, and prefer a
   short common word to a precise long one where the definition carries the precision anyway.

5. **No collision with the other facets.** The coordinate carries telos alongside `effect`
   (`observe`, `create`, `modify`, `preserve`, `destroy`), `state-kind` (`information`, `record`,
   `commitment`, `authority`, `resource`, `relationship`), `modality`, `channel`, and `requisite`.
   Two live hazards: a telos root named `communication` or `knowledge` sits confusingly beside
   state-kind `information`, and any relational-sounding telos label sits beside state-kind
   `relationship`. A reader who has to ask "which axis is this word on?" has been failed by the
   naming, not by the model.

6. **Neutral connotation.** `conformity` carries a pejorative shade in English that its definition
   does not; `persuasion` reads as manipulation; `justice` is freighted and far broader in ordinary
   use than the group it labels. Names shape adoption and are quoted in argument, so a label that
   editorialises about its own category is a liability.

7. **Cross-linguistic legibility.** This is proposed as an international standard. Prefer words with
   stable cognates or plain equivalents, and avoid ones whose English sense is idiomatic. Worth a
   check against at least the languages the corpora already touch — French and German are free,
   given the civil-law corpus.

8. **Non-collision with v1 names whose extension changed.** If a derived group's extension differs
   from a v1 root, reusing the v1 name is worse than coining a new one, because implementers will
   assume continuity. Reuse a v1 name only where the extension is genuinely close, and say so.

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

Also open, and cheaper: the global initial-letter assignment. It cannot be solved greedily per
root, since thirteen roots competing for twenty-six letters with five natural `c` words is a
constraint-satisfaction problem, not a sequence of independent choices.
