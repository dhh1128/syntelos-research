## 1. ARCHETYPE INVENTORY

**Primary archetypes** (`research/archetypes/priorities.md` Part A, with raw outlines in `research/archetypes/<name>/raw/00-starter-outline.md`):

1. **Contract / procurement negotiator-reviewer** — reviews/redlines/negotiates commercial agreements and runs sourcing events. Actions: review inbound agreement; redline terms; reconcile counterparty changes; prepare counterproposal; issue RFI/RFP/RFQ; evaluate bids; run due diligence; award contract; onboard supplier; renew/review contract; escalate must-have concession; decline out-of-mandate concession; [INFERRED] accept within fallback ladder; [INFERRED] notify walk-away.

2. **Incident commander / on-call SRE** — coordinates production-incident response and steady-state reliability. Actions: declare incident; set severity; assign roles; coordinate mitigation; page responders; post stakeholder update on cadence; escalate costly/irreversible mitigation; hand off; run blameless postmortem; land action items; watch SLIs/SLOs; maintain runbook; reduce toil; manage error budget.

3. **Financial analyst / FP&A** — builds forecasts/budgets, analyzes variance, advises. Actions: build forecast; build budget; run variance analysis; explain material variance; reforecast; run scenario/what-if analysis; perform sensitivity analysis; maintain model integrity; document assumptions; reconcile actuals to ledger; present analysis; recommend decision; escalate unreconciled/unsupported assumption.

4. **Trust & safety / content moderator** — applies content policy, decides enforcement, runs appeals. Actions: review item against policy; decide violation; apply least-intrusive action (allow/label/restrict/downrank/remove/strike/suspend/ban); log specific reason; process appeal; independently review appeal; apply strike/repeat-offender ladder; route hard-limit case (CSAM/CTL); route low-confidence to human/senior review; publish transparency report; QA-sample decisions.

5. **Bookkeeper / AP-AR (fin-ops)** — keeps books: records, pays, reconciles, closes. Actions: record balanced journal entry; run three-way match; validate invoice; route invoice for approval; approve/pay within authority limit; apply cash receipt; age receivables; send dunning; reconcile bank; reconcile sub-ledger to GL; post adjusting entry; close period; flag anomaly; hold and escalate unmatched/duplicate/over-limit item.

6. **IT / IAM provisioning** — grants/changes/reviews/revokes access via joiner-mover-leaver. Actions: grant baseline access; provision approved request; re-provision on move; remove old access on move; deprovision leaver; validate business justification; route for owner approval; deny/hold missing justification; run access recertification campaign; reconcile identity store/target systems; detect toxic SoD combination; time-bound privileged grant; revoke on doubt; log grant.

7. **Compliance / audit** — maps controls to requirements, gathers evidence, asserts conformance. Actions: scope/map control to requirement; collect evidence; test design effectiveness; test operating effectiveness; sample defensibly; log gap; assign remediation owner/date; track gap closure; monitor drift; prepare evidence package; draft management assertion; escalate deficiency by severity; refuse unsupported conformance claim.

8. **Customer support / success** — resolves issues across multi-turn conversations, escalates appropriately. Actions: triage ticket; categorize; set priority impact×urgency; answer from KB/verified systems; resolve ticket; route to L2/L3; escalate authority-requiring exception; verify identity before sensitive action; offer refund/credit within policy; set expectations; communicate status; de-escalate conversation; close with verified resolution; contribute KB article; QA-review handled ticket.

9. **Recruiter / talent acquisition** — sources, authors JDs, runs structured selection. Actions: run intake; define success profile; author job description; source candidates; screen against job-related criteria; run structured interview; score before discussion; recommend candidate; reject/advance within rubric; communicate with candidate; escalate comp/level/scope; escalate legal/accommodation edge; review adverse-impact metrics; run reference check; [INFERRED] schedule interview.

10. **Social-media / content marketing** — plans/produces/publishes on-brand content within policy and law. Actions: plan editorial calendar; draft content; self-QA; route for brand/legal review; schedule post; publish post; monitor post performance; report performance; run A/B test; define success metric; disclose sponsored content; substantiate claim; document media rights/license; escalate regulated/crisis content; [INFERRED] modulate tone by channel.

11. **Data-privacy / DPO** — advises/monitors personal-data handling, runs DSAR/breach/DPIA. Actions: advise on compliance; maintain ROPA/data map; run DPIA; request prior consultation when high residual risk; handle DSAR; verify requester identity; collate data; redact third-party data; respond to DSAR within month; assess breach; notify authority ≤72h; notify data subject when high risk; log every breach; ensure Art. 28 DPA with processor; authorize sub-processor; conduct retention review; deliver training.

12. **Technical writer / docs** — produces/maintains accurate, usable documentation to house standards. Actions: draft doc to style; self-QA; route technical/SME review; route editorial review; publish doc; update doc against product version; maintain information architecture; fix broken link; retire stale content; audit doc accuracy; document API endpoint/parameter/response; write testable procedure; run code sample; escalate unverifiable technical claim; escalate product-behavior question.

13. **Executive assistant / chief-of-staff** — prioritizes, schedules, briefs, coordinates on principal’s behalf. Actions: triage principal’s inbox; maintain conflict-free calendar; protect focus time; draft agenda/pre-read; capture action items; chase action items to closure; prepare briefing note; coordinate stakeholders; gatekeep; act on known standing preference; escalate novel/high-stakes/irreversible request; track commitments; represent within delegated authority; hold confidences.

14. **Bug-triage / QA** — decides whether report is real/reproducible bug, classifies severity, manages defect closure. Actions: triage incoming report; determine whether oracle violated; check duplicate; reproduce defect; assign severity per rubric; route to owner; verify fix; close/reopen bug; work queue; watch triage/escape metrics; escalate priority/won’t-fix to product owner; file cannot-reproduce treatment; [INFERRED] group duplicates/root cause.

15. **Vendor / third-party-risk** — assesses third parties, scores/tier risk, monitors lifecycle. Actions: tier vendor by data access/criticality; select tier-appropriate questionnaire; send questionnaire; collect independent evidence; read SOC 2/ISO cert/pen-test; corroborate self-assertion; score risk; decide onboarding; track remediation; document risk acceptance; reassess on cadence; reassess on trigger; re-tier; offboard vendor; confirm data destruction/access revocation; escalate above-appetite risk; perform sanctions/adverse-media screening.

**Extra named archetypes or instances** (`docs/design.md`, `docs/architecture.md`, `docs/priorities.md`, `products/concepts/steward/north-star.md`, `research/archetypes/harm-floor-synthesis.md`):

16. **Newsletter steward** — dogfood example. Actions: read per-channel-granted channels; draft newsletter; verify draft against oracle; authorize worker to publish; check/decrement budget; sign authorization; evaluate reported artifact; write Decision log; post report; [INFERRED] accept/decline channel grant.

17. **Constitution Steward** — reflexive steward over the org’s steward roster (`docs/design.md`, `research/archetypes/priorities.md`). Actions: run MECE/RACI consistency checks over roster; propagate governance change; own escalation; manage role lifecycle; propose org-structure change; monitor external roster metric; [INFERRED] adjudicate ownership gap; [INFERRED] route escalation upward.

18. **Code-excellence / org-efficiency steward** — self-modification peer reviewer (`docs/design.md`). Actions: sweep Decision logs for precipitation candidates; review peer body-gate change; countersign body change; audit self-modification ledger; propose optimization; measure plumb-line metrics before/after; hold independent authorizer gate; [INFERRED] recommend rollback.

19. **Market-research steward** — event-tripwire proactive domain (`docs/design.md`, `north-star.md`). Actions: monitor tripwires; sense market/customer evidence; compile brief; propose new commission; report finding; [INFERRED] update evidence corpus.

20. **Best-practice hawk** — self-updating setpoint + passive sensing (`docs/design.md`). Actions: sense external best-practice drift; update internal setpoint; propose policy change; monitor without effect; [INFERRED] report gap.

21. **Pentester** — effectful sensing as commission (`docs/design.md`, `harm-floor-synthesis.md`). Actions: probe in-scope target; authorize worker probe; report finding; maintain scope credential; [INFERRED] refuse out-of-scope target.

Bench alternates named only without actions: **SDR/outbound**, **paralegal/legal-intake**, **grant-writer**, **community manager**, **trainer** (`priorities.md`, `north-star.md`). Actions NOT IN SOURCE except community manager covered by trust & safety.

---

## 2. ACTION CORPUS

Deduplicated at a consistent verb+object granularity. Inferrels marked `[I]` where not verbatim but required by material; otherwise drawn directly from outlined duties.

**Authorization / delegation**: authorize worker; sign authorization; issue worker token; revoke worker token; counter-sign body change; hold independent authorizer gate; approve access grant; deny access grant; approve invoice; approve payment; approve risk acceptance; approve manager exception; accept within mandate; decline outside mandate; escalate must-have concession.

**Review / assess / decide**: review inbound agreement; review content against policy; review access request; review self-modification diff; review bug report; review DSAR request; review vendor evidence; run due diligence; corroborate assertion; test control effectiveness; sample control; score risk; tier vendor; adjudicate ownership gap; adjudicate case; determine warranty/oracle violation; decide violation; decide onboarding; decide severity; set priority; classify bug; classify content; classify finding severity; classify incident severity; classify data breach risk; decide gap; decide risk treatment.

**Produce / draft**: draft newsletter; draft content; draft doc; draft briefing note; draft management assertion; draft counterproposal; draft redline; draft job description; draft agenda; draft disclosure; draft report; draft transparency report; draft press/status page [I]; draft invoice remit [I].

**Communicate / escalate**: post report; post stakeholder update; post content; send notification; send dun; send status to customer; communicate with candidate; communicate with vendor; escalate to lawyer; escalate to product owner; escalate to controller/CPA; escalate to HR/legal; escalate to L2/L3; escalate to supervisor; escalate breach to authority; escalate gap owner; escalate principal; route low-confidence; route hard-limit; hand off recipient; page responder; set expectation; disclose sponsored content; substantiate claim; present proposal; propose optimization; propose charter change; propose processing purpose? (forbidden); advise principal; interview candidate; offer feedback.

**Manage internal state / records / compute**: record journal entry; post adjusting entry; close period; reconcile bank; reconcile sub-ledger to GL; apply cash; age receivables; track remediation; track gap closure; track action items; log gap; log breach; log decision; log grant; log reason; write Decision log; maintain ROPA; maintain data map; maintain information architecture; maintain model integrity; maintain calendar; fix broken link; retire stale content; update doc; update internal setpoint; update runbook; update knowledge base; capture action item; chase action item; audit docs; audit decisions; audit self-modification ledger; audit evidence corpus; audit access recertification; monitor drift; monitor SLO; monitor error budget; monitor tripwire; monitor domain gap; measure plumb-line metric; sweep Decision logs for candidates; detect toxic SoD; detect duplicate invoice; detect orphan account; detect broken link; confirm reproducibility; reproduce defect; verify fix; verify identity; verify artifact; verify evidence; verify control; verify quote; run variance analysis; run sensitivity analysis; run scenario analysis; run model run; run A/B test; run QA sample; run access recertification; run DPIA; run prior consultation; run sanctions screening; run adverse-impact analysis; run completeness check; run syntax/link check [I]; run test sample [I]; collect evidence; collect request data; collate DSAR data; redact third-party data; retain/destroy data.

**Act on external world / hands**: publish doc; publish content; post newsletter; post announcement; schedule post; publish to channel; remove content; label content; restrict content; downrank content; suspend account; ban account; apply enforcement ladder; apply strike; close ticket; close period; close finding; close bug; reopen bug; route report; file cannot-reproduce; file issue; assign owner; assign severity; move state transition; transition record; soft-delete record; terminate vendor; offboard vendor; destroy/confirm vendor data; revoke vendor access; update payee? [I]; pay invoice; move money; extend refund; grant refund/credit; issue offer; make commitment; sign agreement; execute agreement (forbidden floor); transmit filing; upload evidence; send document; send DSAR response; notify breach; schedule meeting; cancel meeting? [I]; reserve calendar block; protect focus time; read channel; read vendor report; read ticket; read bug report; read resume; scan content; scan QA sample.

Need present as pooled list. Aim 80-200. The above has many. We can organize by families, with count maybe ~140. Need mark inferred. The prompt says "Keep them at a consistent granularity (verb + object)." Could include all. Might be too long but okay.

Need not list every action for extra archetypes? Include enough.

Let's ensure no "invented" actions: most from raw outlines; some inferred. We'll mark `[I]` where I added actions not explicit? Might be simpler to state all actions as synthesized from material; not necessary mark each? Prompt asks mark inferred in inventory, not necessarily corpus. But should be honest. We'll include note: bracketed actions in inventory. Corpus derived from those.

---

## 3. WHAT DISTINGUISHES DELEGABLE ACTIONS

The material reveals several properties; the list in the question maps unevenly.

- **Reversibility** — important but not a clean partition. `research/archetypes/clusters/money-and-commitment.md` says reversibility is "not a clean partition" and distinguishes reversible mitigation vs destructive verbs; `humans-and-fairness.md` proposes reversibility as a separate structural family and says it converts permanent harm into temporary harm plus discoverable record. Accepted, refined: reversibility must be accompanied by whether the record of the act survives, not just the effect.
- **Blast radius** — the harm-floor clusters repeatedly use blast radius, e.g. `access-and-privileged-data.md` IAM-4 "general blast-radius version" vs enumerable protected set; `humans-and-fairness.md` finds mass is the distinctive machine harm and rate caps are floors. Accepted as a differentiating property (mass vs single).
- **Whether it obligates the principal to a third party** — strongly present. `money-and-commitment.md` identifies binding/waving/representing/admitting by ordinary correspondence as unfloorable and CN-1 as incomplete; `paper/draft.md` §8 says "a principal can bind by conduct." This is likely the *strongest* property: it crosses commitment/authority.
- **Whether it spends money** — present but not sufficient: `money-and-commitment.md` treats payment as an irreversible effect, but notes many actions like draft invoice or record entry don’t spend and still matter. Accepted as a subclass of irreversible/effect.
- **Whether it discloses principal data** — central. Clusters `access-and-privileged-data.md` FINDING X-2 and `humans-and-fairness.md` F-3 favor context minimization/verdict-not-record. Accepted; best formulated as *whether the action moves information across a boundary or into a durable context*.
- **Whether it is irrevocable once witnessed** — closely related to publication. `speech-and-artifacts.md` C-3 states retraction is not a remedy; published output is indexed/mirrored/archived within minutes. Accepted as distinct: irrevocability-to-witnesses.
- **Whether it needs a human in the loop** — material does not treat as an intrinsic action property; rather, human countersignature is a *gate assignment* based on severity/irreversibility (`humans-and-fairness.md` F-4, U-7; `speech-and-artifacts.md` TW-6 note). Refined: not a property but a control chosen per action class, unsafe at volume.
- **Whether effect is inside the principal’s own systems vs outside** — accepted and refined: this cuts by whether the enforcement point is inside or outside the failure domain; `harm-floor-synthesis.md` P1/P2 and prong 1. Inside-world actions can often be structurally constrained; outside-world/counterparty-enforced actions are stronger floors (`money-and-commitment.md` C-2, VR-2).
- **One-shot vs standing** — standing/cadence is modeled through `duties` with `cadence` and event tripwires (`docs/design.md` proactivity model; `ORIENTATION.md` §4). Accepted but orthogonal to authorization: both may be bounded/enveloped.

**Additional properties the material reveals:**

- **Act grid dimension: effect × state-kind.** `docs/design.md` uses grids like `(create, authority)`, `(destroy, record)`; `harm-floor-synthesis.md` elevates the `destroy` row absent; `clusters/access-and-privileged-data.md` uses grid vocabulary. This is the strongest internal taxonomy: enable/disable/create/modify/observe × record/info/resource/authority/commitment.
- **Effect vs proposal/speech.** `ORIENTATION.md` centers authorize-only: the steward has no hands; it “proposes, communicates, and authorizes.” Thus classification must separate effects (external state changes) from proposals (which bind nothing).
- **Decidability / semanticness.** `harm-floor-synthesis.md` prong 3 requires decidable content classes; `clusters/*` repeatedly state semantic content is unfloorable (cruelty, deception, discrimination). So actions divide into decidable vs semantic, which affects auditability.
- **Whether a template exists in the mint.** `money-and-commitment.md` C-1: “there is no template for that act” is the floor; delegability depends on a fixed template catalog, not general capability.
- **Whether the action is refusal/omission.** Material treats refusal as first-class and omission as unfloorable (`ORIENTATION.md`; `clusters/access-and-privileged-data.md` X-7). This matters for taxonomy because refusal changes the polarity.

---

## 4. NON-INTERACTION ACTIONS

A large part of the corpus is **not interaction-oriented**. These are solitary/internal acts, computations, state changes, refusals, and omissions. Examples:

- Computations/analysis: run variance analysis, run scenario analysis, reconcile bank, run completeness check, score risk, update setpoint.
- Internal state changes: record journal entry, close period, reconcile sub-ledger, maintain ROPA, maintain data map, maintain calendar, update doc, fix link, retire stale content, audit evidence.
- Monitoring/observation: monitor SLO, monitor error budget, monitor tripwire, monitor domain gap, scan QA sample, watch metrics.
- Refusals/negative acts: deny access, hold/withhold invoice, decline concession, refuse unsupported claim, route out-of-scope.
- Omissions: not declaring incident, not raising finding, not notifying breach, not answering ticket.

Rough estimate: at least **40–50%** of the deduplicated corpus is non-interactive in the sense that it does not require two parties and is not captured by a taxonomy of interactions. This is a conservative count: almost all the bookkeeper, financial-analyst, bug-triage, technical-writer, compliance-evidence, and IAM-reconcile actions fall outside. `Syntelos` v1 as interaction-only misses the steward’s core accountability loop, which records and analyzes even when nothing is sent.

---

## 5. DUTIES AND OMISSIONS

Yes, the material models obligations and omissions as first-class, but asymmetrically.

**Duties are modeled.** `docs/design.md` “The proactivity model” says proactivity is a **duty, not a feature**; duties carry **cadence** and arise from GCD `duties` `{effect, goal, cadence, priority}`. `ORIENTATION.md` §4 defines duty as “an obligation the steward owes, usually with a cadence.” `architecture.md` §2 lists scheduler firing cadenced duties.

**Refusal is first-class.** `ORIENTATION.md` §1: “A steward can say **no**. Refusing an action it deems out-of-bounds is a first-class, expected part of the role — not a malfunction.”

**Omission is modeled but unfloorable.** `research/archetypes/clusters/access-and-privileged-data.md` FINDING X-7: “Floors forbid ACTS. They cannot compel TIMELY ONES. Every archetype here has its most damaging failure in the inaction column… The constructible substitute is always the same shape — an INDEPENDENT detector writes an undeletable trigger.” `clusters/money-and-commitment.md` N-4 repeats: “A floor forbids acts; it cannot compel them… Missing an auto-renewal notice deadline… all irreversible, all invisible to a floor.” So the material recognizes obligations and omissions, but distinguishes permissions/floors from duties, and states that duties cannot be enforced by prohibition.

---

## 6. ADVERSARIAL: CLASSIFICATION AMBIGUITY

Ten corpus actions that would be hardest for an AI annotator to classify consistently into any purpose-based hierarchy, and why.

1. **`decline a counterparty redline / accept within fallback`** — Is this a communication, a decision, or a commitment? It changes the negotiation state and may bind, but its purpose is contested: protecting the principal vs advancing the deal. The material puts it under position integrity, not choice; `contract-negotiator/raw/00` makes it a concession boundary. An AI can easily mislabel it as `share/respond` when it is actually `transact/negotiate` or `protect/refrain`.

2. **`hold and escalate unmatched invoice`** — This is a refusal to act plus an escalation. It is not an approval, not a payment, not a communication. The material calls it fail-closed (`bookkeeper/raw/00`). A purpose hierarchy must encode it as a *negative control action*, not a positive workstep; annotators will split between “route,” “deny,” and “escalate.”

3. **`route low-confidence case to human/senior review`** — This is an internal routing action that depends on a confidence judgment. It is neither a decision on the case nor a message to the user. It appears in `trust-and-safety/raw/00` as an escalation boundary. Its purpose is deference/containment, not resolution.

4. **`mark bug as cannot-reproduce`** — This closes a report with a negative result. It is an evidentiary classification (epistemic) rather than a work effect. `bug-triage-qa/raw/00` lists it as a structured output. An AI may classify it as `assess` or `report`; the actual purpose is to document an inability to verify.

5. **`adjudicate a risk acceptance above appetite`** — The material forbids the analyst from accepting risk; it must escalate. But the action of *documenting* a risk acceptance is a state change in a GRC system that transfers authority. It is both a record and an authorization if signed by the accountable owner. `money-and-commitment.md` VR-3 says ACL enforcement matters; classification depends on *whose identifier writes it*, which no taxonomy of telos captures.

6. **`authorize worker to publish`** — This is the steward’s only external-effect path. It is not itself the publication, nor a message; it is a delegation. `architecture.md` §3 treats it as a gated act. If the taxonomy classifies by purpose, this action sits at the intersection of `authorize`, `transmit`, and `effect`, and its purpose is precisely *not* to do the thing but to permit it.

7. **`run DPIA before processing`** — This is a legally mandated internal analysis, not an interaction. It produces a document but doesn’t send it; its purpose is compliance/anticipation. `data-privacy-dpo/raw/00` includes it under proactive duties. A human annotator may recognize it as `assess`; an AI tends to classify every document-producing action as `share`, which is wrong.

8. **`notify breach authority within 72 hours`** — This is a mandatory communication to a third party with a hard legal clock. It is both a disclosure and a compliance act. Its telos could be `notify`, `comply`, or `disclose`; the material does not unify these. `data-privacy-dpo/raw/00` treats it as a deadline duty. The purpose is not to inform the authority as a peer but to satisfy a statutory obligation, which many purpose taxonomies collapse into `share/inform`.

9. **`update internal setpoint based on sensed drift`** — A self-modifying monitoring action. It changes the steward’s own target, not the world. `docs/design.md` lists it under the “best-practice hawk” archetype, a “self-updating setpoint + passive-but-metered sensing.” Is this `transact`, `relate`, `share`, or an internal action? No interaction exists at all.

10. **`return unused authority/narrow own charter`** — The material’s remit-evolution doctrine says a steward may propose offering back unused authority (`docs/design.md` “metered frustration, priced proposals”). This is a negative authorization: reducing its own bounds. Its purpose is governance/trust, not performing work. An AI annotator will struggle because it reverses the usual direction of delegation flows.

These ten share common causes: they are negative, epistemic, boundary-crossing, self-referential, legally-clocked, or delegation-like rather than ordinary work. Any purpose-based hierarchy must explicitly model **refusal, escalation, negative findings, self-modification, delegation authorization, and mandatory compliance notifications**; otherwise a large fraction of the corpus will be misclassified.
