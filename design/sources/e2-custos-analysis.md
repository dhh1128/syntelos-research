# 1. WHERE ACTS APPEAR IN CUSTOS

Custos touches acts in exactly five structural places; everywhere else the act name is an **opaque string**.

**The two verbs (§1.3).** Every actor performs "exactly one of two verbs," Evaluate or Enact. The constructor "ratifies law, seats authorities, advances lifecycle, commits acts" (§5, "Evaluator; constructor"; repeated in §8.5's ratified separation quote). Act-ness is typed only at this altitude: enactment vs. evaluation.

**GEL contents (§5 "The three logs").** The GEL is "the committed record of a GARD's law: constitution, amendment, seating, enactment." Four content kinds, and "enactment" absorbs everything else.

**Designated act classes (§10, seal ladder).** The only place Custos names act classes with keyword force: "Designated act classes — charter, revocation of a seat, enactment amending law, and the succession acts of section 17 — SHALL anchor in establishment events; a domain whose law designates further classes commits that designation in its GEL." Classification here exists solely to fix **anchor grade** (establishment vs. interaction event), i.e., formality, not subject matter.

**The GEL grammar (§18).** Event types are per-domain committed data, not standard vocabulary: track two's ilk table "is itself committed data in the GEL — the table of event types a domain's law recognizes is law, enacted and amended under succession." The spine's only utterances are "anchorings: commitments of acts to coordinates."

**The explicit non-goal (§3, §16).** "Where this document names acts (enactment, seating, recovery, reconciliation), it binds their evidence requirements; it does not enumerate the act universe." §16 lists "the act-registry design" among the confessed-open interiors.

**Utina's binding (docs/interfaces.md).** This is where opacity is proven. `Clause.governs: tuple[str, ...]` — "act kinds this clause rules"; "Act kind — `str`, e.g. `"open-bank-account"`, `"amend-operating-agreement"`." The law body is `{"id", "governs": [...], "group": {...}}`; an enactment carries `"act"` naming the class it performs; the endorsement body carries a *different* `"act"` field valued `"issue" | "revoke"` (dossier-shaped) — a field-name collision the Q&A records (Q32). Q30 (custos-questions.md) confirms the binding is literal string match: a domain's clause governs "act classes the *domain* names," and "an enactment that names none is refused rather than judged under a guessed class."

**Conclusion:** to the fold, an act kind is a committed string. Structure attaches only through (i) anchor-grade designation, (ii) ilk-table placement, (iii) the clause's committed predicates. The vectors directory lists only `ledger.json` and `README.md`; their contents are NOT IN SOURCE.

# 2. WHAT CUSTOS NEEDS FROM AN ACT VOCABULARY

**Hard requirements:**

- **R0 — Committable packaging.** The vocabulary must itself be SAID-addressable law: clauses are "SAID-addressed bytes in the GEL" (§5, law ladder), ilk tables are committed data (§18), and any external semantics a finding consumes "is pinned by committed digest — an unpinned semantics is refused" (§1.4 axiom 4; §15's functional-dependency declarations). A vocabulary that cannot be pinned by digest is unusable.
- **R1 — Stable opaque identifiers.** The clause→act binding is string equality (interfaces.md `Clause.governs`; Q30). Determinism is byte-level: "Two verifiers holding the same bundle SHALL emit the same defeated finding down to the byte" (§8.3). Renaming an act kind is a law-changing event.
- **R2 — Class membership carried in the act's committed bytes.** Q30 pins this: the fold may not infer that a domain's "amend-operating-agreement" is Custos's "enactment amending law" — that mapping "is precisely the uncommitted seam [§8.5] says an evaluator refuses rather than legislates."
- **R3 — Kind/instance separation.** Q26: a prospective question binds to the *latest* committed act of its kind; re-tabling is a new event. §18: "a coordinate tuple is a location, never an identity."
- **R4 — Ex-ante enumerable requirement spaces.** §8.3: "the law commits the question's requirement space ex-ante — which is what makes completeness decidable and affirmation reachable"; "no finding is terminal while any enumerated check… is unexamined." Every act kind must support a committed, fully enumerable evidence checklist.
- **R5 — A law-amending flag.** The ordinary-act vs. law-changing-act distinction is load-bearing (§10 designated classes; §12's reflexive class; §17 succession; demo D4 judged under A2 while installing B2). The vocabulary must let a domain commit this designation so no fold guesses it.
- **R6 — Anchor-grade compatibility.** Classes must be assignable to establishment anchoring (§10) and credential form where toolchain-checkable (§7 object typing).
- **R7 — Events with positions.** §12's criterion: governable X has "committed events," key-state authentication, and "positions, so law committed before a position can judge it."
- **R8 — Second-order disposition acts.** The corpus requires acts *on* acts: endorse, decline (§9 slot grammar), retract (Q18 — Custos gap), re-present (§8.2's cure for expired/abandoned).
- **R9 — Ground fields for recourse acts.** §14.1: a grounded enactment "SHALL commit… the evidence bundle… the law head it invokes; the position at which it speaks; and the terminal finding it claims."
- **R10 — Refusal-graceful partial coverage.** Missing vocabulary yields refusal, not failure (§8.5; demo D8 "declare-dividend" → refusal naming the missing rule). Extension only by committed amendment (§18 ilk-table succession).

**Nice-to-haves:** shared cross-domain names (a vocabulary is precisely the "shared rule-object SAID" a federation envelope cites, §13.1); a committed form for expiry/supersession semantics (§9 delegates these to Constitutions but gives no shape; custos-proposals.md U2); sanity invariants for inoperative composition rules (Q22).

**Explicitly not needed:** a universal act registry (§3 non-goal), cross-frame force (§13), or quality ranking (§1.4: "declines to rank the choices").

# 3. THE ACTS THEMSELVES

**Identity/keys:** inception (§5 gAID genesis knot); rotation; custodian recovery rotation (§11, "a grounded enactment… inherits all of section 14.1"); delegation; delegated-gAID recovery profile (§11).
**Law-changing:** ratification (§17); amendment; succession (§17); ilk-table/grammar migration (§18); semantics-version migration (§15); registry designation and migration (§18); CESR genus reservation (§18); ilk seat enactments (§19); freeze (§15); fork (§14.3).
**Authority:** seating (§5); re-seating (§8.5); revocation of a seat (§10); expulsion from a seat (§14.2); custody-profile commitment (§15); tenure expiry via committed term (§11 — "no one deciding anything," §14).
**Evidence/registry:** credential issuance and revocation (§12); registry inception and management (§12); warranty issuance (§7 — "an enactment binding its maker to a finding's ground," §1.7); witness receipting (§12 obligated attestation); watcher discrepancy reports and key-state-notice comparison packages (§13.4); disclosure demand and response (§2.5); admission enactments (§2.4, §7).
**Decision/disposition:** propose/table, endorse, decline (interfaces.md Constructor); retract (Q18); re-present (§8.2).
**Inter-frame:** adoption (§13.1, "SHALL be committed"); revocation of adoption (§14.2); recognition (matched anchors, §13.1); exit/dissolution; testimony into the commons (§14.2).
**Recourse:** withdrawal of standing; revocation of empowerment; interim suspension (§14.1); rehabilitation (§8.3 — "rehabilitation is an act, not a transition").
**Domain business (demo + seed):** open-bank-account, hire-vp-sales, approve-budget, declare-dividend, seat-the-board, amend-operating-agreement (demo-script.md); "attestations, licenses, revocations" (§2.7); age-verification presentation (§2.0).

# 4. STRUCTURE LATENT IN THOSE ACTS

| Candidate dimension | Verdict | Evidence |
|---|---|---|
| Who is affected | **Accept, refine to perimeter/relation** | §14.2's recourse ladder is literally graduated by relation (within frame → envelope → consumption → commons → medium); §12's relation axis: "four distances from the frame's own keys" (self, seat, stranger, peer) |
| Reversibility | **Reject as stated; refine** | At record level nothing reverses: append-only, no backward edge (§8.3), "Grounds do not rot" (§14.1). The live axis is effect-level supersession/withdrawal (exit is unilateral, §13.1; retraction unresolved, Q18) |
| Changes rules vs. operates under them | **Accept — strongest dimension** | §1.2 succession ("the one place the tower touches itself"); §10 designated classes; §12 reflexive class; D4 judged under A2 while installing B2 |
| Binds a third party | **Accept as counterparty scope** | 0: consumption ("A cannot prevent consumption and need not know of it," §13.1); 1: warranty binds the warrantor; 2: envelope matched anchors; n: n(n-1)/2 envelopes (§13.1) |
| Creates/transfers/extinguishes a right | **Accept, note absence** | Conferral and extinguishment present (standing, seats; §9 with Hohfeld cited); *transfer* is absent from the entire corpus — data, not oversight |
| Requires counterparty assent | **Accept** | Bilateral envelope vs. unilateral adoption (§13.1); endorsements as assent acts (§9) |
| Formality/registration | **Accept — spec-native** | Anchor grade: "the difference between promise and physics" (§10); credential form vs. bare SAID (§7) |
| Speech act vs. physical | **Reject** | Every act is committed speech; recourse is "consequence as computation" (§14); physical effects are off-log by construction |

**Additional dimensions the corpus reveals:** initiation structure (unilateral spine vs. threshold multi-party — "Everything multi-party… enters as evidence the spine anchors," §18); judged vs. constructed (genesis is the sole unjudged act, §5/§12); fold tier (key/registry/governance, §8.4); obligated vs. voluntary speech (§12's attestation partition: "Duty-to-speak is governed ex ante; freedom-to-speak is convictable ex post"); terminality effect (slot-filling vs. slot-spending vs. reopening — Utina dispositions, §8.2 cures); time-windowing (§11 contest windows, cadence, §8.2 expiry).

# 5. THE SCOPE PROBLEM

**Position: telos and legal-act classification are orthogonal facets. Model them separately; share an identifier registry, not a hierarchy.**

Three spec-grounded arguments. **(a) Telos is not byte-derivable.** Axiom 4 (§1.4): "Nothing a fold consumes may be underivable from committed bytes." Purpose is ambient; a fold cannot compute it. Any act classification the *evaluator* consults must be keyed on committed form — which is why Custos classifies by anchor grade and evidence requirements, never by point. **(b) Identical telos, divergent acts.** The demo's centerpiece (D3 vs. D6): the same decision ("approve the budget"), the same purpose, the same dissenter — defeated under unanimity, pending under the board. Everything governance-relevant differs; nothing telos-relevant does. A telos node would carry zero evaluator payload. **(c) Identical form, any telos.** "Amendment" is individuated by what it changes and its anchor grade; its purpose is unconstrained. An endorsement is a disposition act whose motives vary while its legal effect is fixed — §8.3: pertinence is "derived, never declared."

**Strongest counterargument:** the constitutive-purpose reading. Searle's "counts as" — which Custos §9 itself adopts ("committed registry state counts as standing only within the context the covenant constitutes") — says institutional acts have purposes fixed by the institution, not the agent: the telos of a revocation *is* to extinguish standing. Under that reading telos≈effect and one tree serves both. But note what happened: "telos" was redefined as institutional effect. The counterargument collapses into the position — a taxonomy classifying by constitutive purpose *is* effect classification wearing purpose's name. Hence faceting: Syntelos keeps its interaction-telos axis for what it already covers (and some legal acts genuinely are interactions — offer/acceptance, endorsement — those nodes simply carry values on both facets), while governance acts get effect/form/authority axes. This also matches Custos's own pluralism: it types positions and "does not rank them" (§2.2, §1.4).

# 6. RECURRING JURISPRUDENTIAL PRIOR ART

- **Hohfeld's fundamental legal conceptions** — classifies legal *relations* (claim/duty, privilege/no-claim, power/liability, immunity/disability). Custos §9 already cites it ("a power held is a liability borne by its counterparty"). **Best fit for the effect axis.**
- **Hart's primary/secondary rules** — rules of conduct vs. rules of recognition, change, adjudication. The classic statement of the law-amending/act-under-law split (R5). Strong fit.
- **Searle's speech-act taxonomy; Austin's exercitives/verdictives** — utterance classes; declarations change institutional facts by utterance. Conceptual fit for enactments; weak operational granularity.
- **Contract-formation doctrine** (offer, acceptance, revocation, counteroffer) — bilateral assent sequencing. Fits the matched-anchor envelope (§13.1).
- **Agency law (Restatement (Third) of Agency)** — actual/apparent authority, ratification, termination. Fits seats, organs, delegation (§5, §11, DI2I edges §7).
- **Corporate-governance action classes (DGCL-style; Robert's Rules motion classes)** — Robert's Rules is literally a precedence-ordered taxonomy of motions (main, subsidiary, privileged, incidental). Fits ordinary/subject-matter acts. UNCERTAIN: any single canonical statutory enumeration exists; DGCL coverage is jurisdiction-specific.
- **XACML (OASIS)** — policies targeted at named action attributes; permit/deny with obligations. Architectural precedent for "clause governs act kind" (interfaces.md). Good system fit.
- **LegalRuleML (OASIS)** — deontic, defeasible legal-rule serialization. Fits clause/predicate representation (§5 law ladder), not act naming.
- **Akoma Ntoso (OASIS LegalDocumentML)** — legislative document lifecycles and amendment structures. Fits the law-acts group (amendment/succession lineage, §17).
- **LKIF-Core legal ontology** — legal roles, actions, norms as ontology classes. Reasonable conceptual fit; UNCERTAIN on current maintenance.
- **FIBO (EDM Council)** — financial contracts and corporate actions. Fits only the financial subject-matter acts; heavy.
- **ODRL (W3C)** — permissions/prohibitions/duties over named actions. Fits act-naming with deontic wrapper; modest.
- **schema.org Actions** — web-scale commerce verbs (BuyAction, TransferAction). Covers ordinary business acts; no governance semantics.

**Net assessment:** no existing taxonomy covers the corpus whole. Hohfeld (effect) + Hart (rule-change) + Robert's Rules (precedence) + XACML (name-matching architecture) jointly cover the dimensions §4 actually exhibits — which is further evidence for the faceted position in §5.
