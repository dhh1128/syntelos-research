# A. The partition

## discovering

Makes an existing condition, fact, resource, or prior record knowable. It includes retrieval, inspection, search, listing, measurement, and observation where the intended outcome is increased visibility rather than changed state.

**Discriminating question against `assuring`:** Is the act merely obtaining information, or is it establishing that a claim satisfies an oracle, evidence standard, or source of truth?

**Count:** 241

- T0001 — get file contents
- T0017 — search documents using autorag
- T0034 — get elevation data for locations on the earth
- T0188 — perform a web search using the brave search api
- T0418 — get certificate transparency data

## transforming

Changes the state, structure, location, or lifecycle of a technical artifact or data object. The changed artifact is the immediate outcome; any later informational, communicative, or governance use is incidental.

**Discriminating question against `publishing`:** Is success simply that an artifact or system state changed, or that audience-facing knowledge became fit for or available to readers?

**Count:** 89

- T0003 — create a directory
- T0064 — delete a file in the working directory
- T0200 — set a json value in redis at a given path
- T0419 — initialize a new git repository
- T0601 — move a file

## coordinating

Aligns actors, schedules, conversations, protocol participants, or multi-step processes so interaction can proceed. It covers messaging, invitations, requests, handshakes, workflow progression, and similar acts that neither independently confer authority nor transfer financial value.

**Discriminating question against `authorizing`:** Does the act facilitate interaction, or does it determine whether another actor may bind, access, delegate, or proceed?

**Count:** 91

- T0006 — post stakeholder updates
- T0077 — capture and chase meeting action items
- T0118 — prepare an agenda and pre-read
- T0253 — coordinate incident roles
- T0562 — coordinate stakeholders

## authorizing

Confers, withholds, activates, revokes, or verifies permission, delegated power, consent, or binding approval. It includes access decisions and protocol acts whose telos is a change in normative standing rather than merely message exchange.

**Discriminating question against `governing`:** Is the immediate purpose to decide who may act or bind, or to define and enforce the substantive constraints under which action is acceptable?

**Count:** 33

- T0022 — verify identity before a sensitive action
- T0030 — obtain sign-off for controlled spend
- T0264 — provision exactly approved access
- T0448 — provision exactly the access that was approved
- T0607 — grant access

## publishing

Creates, improves, reviews, maintains, or releases content intended to communicate durable knowledge to an audience. It includes documentation and editorial work where intelligibility, substantiation, review, and audience availability define success.

**Discriminating question against `transforming`:** Is the artifact being changed as an operational object, or being made accurate, usable, and available as communication?

**Count:** 21

- T0099 — perform editorial self-qa on content
- T0151 — update documentation to match the current version
- T0315 — draft to house style
- T0358 — publish reviewed documentation
- T0399 — plan an editorial calendar against content goals

## assuring

Establishes warranted confidence that a claim, record, control, implementation, or result corresponds to evidence or an applicable oracle. It includes validation, testing, reconciliation, corroboration, audit, reproducibility, and evidence-based refusal to assert correctness.

**Discriminating question against `discovering`:** Is information merely being collected, or is it being compared with a criterion so that correctness or evidential sufficiency can be concluded?

**Count:** 37

- T0010 — get a fact confirmed by an SME
- T0050 — monitor controls for drift
- T0190 — test control design and operating effectiveness
- T0280 — reproduce a reported bug
- T0577 — confirm a report is a real bug

## governing

Defines, applies, or preserves policy, legal, privacy, risk, fairness, and conduct boundaries. Its outcome is legitimate and proportionate behavior under constraints, including enforcement, escalation, risk acceptance, and protected-data handling.

**Discriminating question against `authorizing`:** Is the act changing a particular actor’s permission, or applying and maintaining the rules and risk boundaries that govern conduct generally or substantively?

**Count:** 47

- T0015 — scope and map controls to requirements
- T0126 — apply a proportionate content-enforcement action
- T0243 — maintain the ROPA
- T0423 — run a DPIA
- T0505 — maintain a breach register

## deciding

Produces a prospective judgment, classification, prioritization, interpretation, forecast, or plan that guides later action. Unlike assurance, its outcome is a choice or model rather than confidence that an existing claim matches evidence.

**Discriminating question against `assuring`:** Is the evidence being used to determine whether something is correct, or to choose, classify, forecast, or prioritize what should happen?

**Count:** 10

- T0145 — produce a financial recommendation
- T0213 — assign severity per the rubric
- T0266 — escalate business-priority calls
- T0412 — define success metrics up front
- T0528 — build forecasts and budgets

## remediating

Restores an impaired service or closes an identified defect, ticket, control gap, or harmful condition. Its endpoint is mitigation or verified resolution rather than diagnosis, classification, or general governance.

**Discriminating question against `governing`:** Is the act maintaining or applying a standing boundary, or eliminating a concrete failure or deficiency already requiring correction?

**Count:** 18

- T0028 — refuse to chase root cause while users bleed
- T0055 — run a blameless postmortem
- T0241 — verify a fix
- T0527 — triage a production incident
- T0565 — drive to mitigation

## transacting

Moves, settles, approves, records, or reconciles monetary value and accountable financial obligations. It includes accounting acts when their purpose is faithful stewardship of balances, invoices, payments, or ledgers rather than generic data manipulation.

**Discriminating question against `assuring`:** Is reconciliation being performed to establish general correctness, or specifically to preserve and settle accountable financial value?

**Count:** 24

- T0009 — apply cash
- T0082 — reconcile bank and sub-ledgers
- T0203 — pay an invoice
- T0474 — record a balanced journal entry
- T0550 — pay a matched and authorized invoice

## staffing

Defines workforce needs and finds, screens, evaluates, or selects people for roles. It is separated from generic deciding because the corpus repeatedly treats job-related evidence, structured evaluation, and hiring scope as a coherent end-to-end purpose.

**Discriminating question against `deciding`:** Is the judgment allocating or evaluating people for organizational roles, or is it a non-workforce classification, forecast, or plan?

**Count:** 10

- T0024 — define the success profile
- T0069 — run intake with the hiring manager
- T0154 — source candidates for a requisition
- T0384 — run a structured interview
- T0458 — screen against job-related criteria

# B. Assignment table

```text
T0001	discovering
T0002	discovering
T0003	transforming
T0004	discovering
T0005	discovering
T0006	coordinating
T0007	governing
T0008	coordinating
T0009	transacting
T0010	assuring
T0011	governing
T0012	discovering
T0013	assuring
T0014	assuring
T0015	governing
T0016	assuring
T0017	discovering
T0018	transforming
T0019	discovering
T0020	coordinating
T0021	transacting
T0022	authorizing
T0023	discovering
T0024	staffing
T0025	coordinating
T0026	authorizing
T0027	discovering
T0028	remediating
T0029	assuring
T0030	authorizing
T0031	transforming
T0032	governing
T0033	discovering
T0034	discovering
T0035	discovering
T0036	coordinating
T0037	discovering
T0038	transforming
T0039	discovering
T0040	authorizing
T0041	transforming
T0042	assuring
T0043	remediating
T0044	transacting
T0045	discovering
T0046	transforming
T0047	governing
T0048	discovering
T0049	discovering
T0050	assuring
T0051	transacting
T0052	coordinating
T0053	discovering
T0054	governing
T0055	remediating
T0056	governing
T0057	coordinating
T0058	coordinating
T0059	discovering
T0060	coordinating
T0061	coordinating
T0062	transforming
T0063	authorizing
T0064	transforming
T0065	discovering
T0066	discovering
T0067	discovering
T0068	staffing
T0069	staffing
T0070	coordinating
T0071	governing
T0072	discovering
T0073	discovering
T0074	discovering
T0075	discovering
T0076	discovering
T0077	coordinating
T0078	transacting
T0079	transforming
T0080	discovering
T0081	remediating
T0082	transacting
T0083	coordinating
T0084	transforming
T0085	discovering
T0086	authorizing
T0087	coordinating
T0088	discovering
T0089	assuring
T0090	coordinating
T0091	transforming
T0092	coordinating
T0093	discovering
T0094	authorizing
T0095	transforming
T0096	authorizing
T0097	discovering
T0098	transforming
T0099	publishing
T0100	discovering
T0101	publishing
T0102	transforming
T0103	coordinating
T0104	assuring
T0105	discovering
T0106	publishing
T0107	discovering
T0108	transforming
T0109	discovering
T0110	coordinating
T0111	discovering
T0112	discovering
T0113	discovering
T0114	discovering
T0115	discovering
T0116	remediating
T0117	coordinating
T0118	coordinating
T0119	transforming
T0120	coordinating
T0121	transforming
T0122	discovering
T0123	transforming
T0124	assuring
T0125	publishing
T0126	governing
T0127	discovering
T0128	governing
T0129	transacting
T0130	coordinating
T0131	discovering
T0132	discovering
T0133	transacting
T0134	assuring
T0135	transforming
T0136	coordinating
T0137	governing
T0138	discovering
T0139	coordinating
T0140	discovering
T0141	coordinating
T0142	discovering
T0143	transforming
T0144	discovering
T0145	deciding
T0146	transforming
T0147	governing
T0148	discovering
T0149	discovering
T0150	transforming
T0151	publishing
T0152	discovering
T0153	discovering
T0154	staffing
T0155	discovering
T0156	transforming
T0157	coordinating
T0158	publishing
T0159	staffing
T0160	transforming
T0161	discovering
T0162	discovering
T0163	transforming
T0164	remediating
T0165	discovering
T0166	coordinating
T0167	transforming
T0168	transforming
T0169	staffing
T0170	coordinating
T0171	discovering
T0172	discovering
T0173	coordinating
T0174	discovering
T0175	governing
T0176	governing
T0177	coordinating
T0178	discovering
T0179	authorizing
T0180	discovering
T0181	transforming
T0182	coordinating
T0183	coordinating
T0184	coordinating
T0185	transforming
T0186	discovering
T0187	discovering
T0188	discovering
T0189	discovering
T0190	assuring
T0191	discovering
T0192	coordinating
T0193	coordinating
T0194	discovering
T0195	governing
T0196	coordinating
T0197	coordinating
T0198	discovering
T0199	coordinating
T0200	transforming
T0201	transforming
T0202	transacting
T0203	transacting
T0204	coordinating
T0205	discovering
T0206	governing
T0207	authorizing
T0208	transforming
T0209	governing
T0210	staffing
T0211	discovering
T0212	discovering
T0213	deciding
T0214	authorizing
T0215	authorizing
T0216	discovering
T0217	discovering
T0218	coordinating
T0219	assuring
T0220	coordinating
T0221	discovering
T0222	transforming
T0223	authorizing
T0224	discovering
T0225	transforming
T0226	discovering
T0227	discovering
T0228	discovering
T0229	discovering
T0230	discovering
T0231	discovering
T0232	coordinating
T0233	governing
T0234	coordinating
T0235	transforming
T0236	transforming
T0237	discovering
T0238	governing
T0239	discovering
T0240	governing
T0241	assuring
T0242	discovering
T0243	governing
T0244	transforming
T0245	coordinating
T0246	discovering
T0247	governing
T0248	discovering
T0249	discovering
T0250	transforming
T0251	discovering
T0252	publishing
T0253	coordinating
T0254	discovering
T0255	coordinating
T0256	coordinating
T0257	discovering
T0258	assuring
T0259	governing
T0260	transforming
T0261	governing
T0262	transforming
T0263	coordinating
T0264	authorizing
T0265	publishing
T0266	deciding
T0267	coordinating
T0268	remediating
T0269	discovering
T0270	remediating
T0271	coordinating
T0272	authorizing
T0273	authorizing
T0274	discovering
T0275	discovering
T0276	authorizing
T0277	transforming
T0278	discovering
T0279	discovering
T0280	assuring
T0281	governing
T0282	governing
T0283	transforming
T0284	discovering
T0285	coordinating
T0286	coordinating
T0287	discovering
T0288	coordinating
T0289	discovering
T0290	transforming
T0291	discovering
T0292	transforming
T0293	coordinating
T0294	discovering
T0295	discovering
T0296	transacting
T0297	assuring
T0298	discovering
T0299	transforming
T0300	discovering
T0301	authorizing
T0302	deciding
T0303	governing
T0304	coordinating
T0305	discovering
T0306	discovering
T0307	transforming
T0308	discovering
T0309	transforming
T0310	discovering
T0311	assuring
T0312	discovering
T0313	discovering
T0314	discovering
T0315	publishing
T0316	assuring
T0317	discovering
T0318	assuring
T0319	discovering
T0320	discovering
T0321	coordinating
T0322	governing
T0323	coordinating
T0324	discovering
T0325	coordinating
T0326	publishing
T0327	remediating
T0328	transforming
T0329	coordinating
T0330	discovering
T0331	authorizing
T0332	discovering
T0333	assuring
T0334	discovering
T0335	discovering
T0336	discovering
T0337	governing
T0338	coordinating
T0339	assuring
T0340	governing
T0341	discovering
T0342	discovering
T0343	discovering
T0344	transforming
T0345	transforming
T0346	transacting
T0347	publishing
T0348	discovering
T0349	discovering
T0350	governing
T0351	discovering
T0352	discovering
T0353	transforming
T0354	governing
T0355	discovering
T0356	discovering
T0357	remediating
T0358	publishing
T0359	discovering
T0360	governing
T0361	discovering
T0362	transforming
T0363	assuring
T0364	transforming
T0365	coordinating
T0366	transforming
T0367	discovering
T0368	transforming
T0369	transacting
T0370	transacting
T0371	transforming
T0372	discovering
T0373	coordinating
T0374	discovering
T0375	assuring
T0376	discovering
T0377	transforming
T0378	discovering
T0379	discovering
T0380	discovering
T0381	publishing
T0382	assuring
T0383	discovering
T0384	staffing
T0385	transforming
T0386	transacting
T0387	deciding
T0388	discovering
T0389	discovering
T0390	discovering
T0391	assuring
T0392	coordinating
T0393	coordinating
T0394	staffing
T0395	authorizing
T0396	transforming
T0397	coordinating
T0398	discovering
T0399	publishing
T0400	transforming
T0401	discovering
T0402	publishing
T0403	transforming
T0404	transforming
T0405	publishing
T0406	publishing
T0407	coordinating
T0408	governing
T0409	discovering
T0410	authorizing
T0411	discovering
T0412	deciding
T0413	discovering
T0414	discovering
T0415	discovering
T0416	transforming
T0417	discovering
T0418	discovering
T0419	transforming
T0420	discovering
T0421	coordinating
T0422	authorizing
T0423	governing
T0424	publishing
T0425	transforming
T0426	discovering
T0427	governing
T0428	coordinating
T0429	discovering
T0430	transforming
T0431	governing
T0432	discovering
T0433	discovering
T0434	transforming
T0435	discovering
T0436	coordinating
T0437	coordinating
T0438	transforming
T0439	discovering
T0440	assuring
T0441	transforming
T0442	transforming
T0443	coordinating
T0444	deciding
T0445	discovering
T0446	coordinating
T0447	publishing
T0448	authorizing
T0449	discovering
T0450	discovering
T0451	coordinating
T0452	transforming
T0453	coordinating
T0454	discovering
T0455	transforming
T0456	discovering
T0457	discovering
T0458	staffing
T0459	authorizing
T0460	discovering
T0461	transforming
T0462	deciding
T0463	governing
T0464	coordinating
T0465	governing
T0466	authorizing
T0467	coordinating
T0468	discovering
T0469	transforming
T0470	transacting
T0471	discovering
T0472	transforming
T0473	discovering
T0474	transacting
T0475	discovering
T0476	discovering
T0477	authorizing
T0478	discovering
T0479	coordinating
T0480	coordinating
T0481	assuring
T0482	discovering
T0483	authorizing
T0484	remediating
T0485	discovering
T0486	discovering
T0487	remediating
T0488	discovering
T0489	authorizing
T0490	transforming
T0491	coordinating
T0492	governing
T0493	transforming
T0494	governing
T0495	discovering
T0496	authorizing
T0497	publishing
T0498	transacting
T0499	coordinating
T0500	discovering
T0501	discovering
T0502	discovering
T0503	discovering
T0504	governing
T0505	governing
T0506	discovering
T0507	transforming
T0508	discovering
T0509	remediating
T0510	discovering
T0511	discovering
T0512	governing
T0513	coordinating
T0514	discovering
T0515	coordinating
T0516	discovering
T0517	transforming
T0518	transacting
T0519	governing
T0520	discovering
T0521	discovering
T0522	discovering
T0523	transforming
T0524	discovering
T0525	coordinating
T0526	discovering
T0527	remediating
T0528	deciding
T0529	transacting
T0530	governing
T0531	discovering
T0532	discovering
T0533	coordinating
T0534	deciding
T0535	discovering
T0536	governing
T0537	discovering
T0538	coordinating
T0539	coordinating
T0540	discovering
T0541	discovering
T0542	discovering
T0543	remediating
T0544	discovering
T0545	coordinating
T0546	coordinating
T0547	governing
T0548	remediating
T0549	discovering
T0550	transacting
T0551	coordinating
T0552	discovering
T0553	assuring
T0554	transacting
T0555	discovering
T0556	discovering
T0557	transforming
T0558	discovering
T0559	discovering
T0560	coordinating
T0561	discovering
T0562	coordinating
T0563	governing
T0564	transacting
T0565	remediating
T0566	assuring
T0567	transforming
T0568	transforming
T0569	discovering
T0570	authorizing
T0571	governing
T0572	authorizing
T0573	assuring
T0574	assuring
T0575	transforming
T0576	authorizing
T0577	assuring
T0578	discovering
T0579	discovering
T0580	discovering
T0581	discovering
T0582	remediating
T0583	discovering
T0584	discovering
T0585	coordinating
T0586	discovering
T0587	assuring
T0588	discovering
T0589	coordinating
T0590	transacting
T0591	authorizing
T0592	coordinating
T0593	assuring
T0594	discovering
T0595	transforming
T0596	transacting
T0597	discovering
T0598	assuring
T0599	discovering
T0600	discovering
T0601	transforming
T0602	assuring
T0603	coordinating
T0604	discovering
T0605	transforming
T0606	discovering
T0607	authorizing
T0608	discovering
T0609	publishing
T0610	discovering
T0611	coordinating
T0612	governing
T0613	discovering
T0614	coordinating
T0615	discovering
T0616	transforming
T0617	transforming
T0618	coordinating
T0619	discovering
T0620	coordinating
T0621	discovering
```

# C. Unplaceable

None. All 621 acts admit a corpus-supported purpose under the stated tie-breaks, although several depend on weak or protocol-specific wording; those cases are identified below.

# D. Stress points

1. **T0029 — perform tier-appropriate vendor due diligence**  
   **Competing roots:** `assuring` and `governing`. Due diligence gathers and evaluates evidence, but it does so inside a vendor-risk regime; I assigned it to `assuring` because the immediate result is warranted confidence, while T0261 performs the governing act of assigning the tier.

2. **T0081 — escalate deficiencies according to severity**  
   **Competing roots:** `remediating` and `governing`. Severity-based escalation enforces a governance rule, but the deficiency is already concrete and the escalation exists to get it corrected; hence `remediating`.

3. **T0086 — accept a data agreement negotiation**  
   **Competing roots:** `authorizing` and `coordinating`. “Accept” may simply advance a negotiation protocol, but it plausibly changes binding standing; I treated acceptance as authorization and left offers, proposals, and requests in `coordinating`.

4. **T0123 — start a crawl**  
   **Competing roots:** `transforming` and `discovering`. The ultimate purpose of crawling is discovery, but this act does not return findings—it creates or changes a running crawl job; the immediate telos therefore determined `transforming`.

5. **T0134 — refuse to publish unsubstantiated claims**  
   **Competing roots:** `assuring` and `publishing`. It is embedded in publication, yet the reason for refusal is failure of substantiation rather than editorial quality or delivery; that makes `assuring` the stronger placement.

6. **T0195 — decide an enforcement action**  
   **Competing roots:** `governing` and `deciding`. Mechanically it produces a decision, but the decision exists specifically to apply policy and constrain conduct; domain-specific telos overrides generic decision-making, so it is `governing`.

7. **T0241 — verify a fix**  
   **Competing roots:** `assuring` and `remediating`. Verification establishes evidential confidence, while the larger process aims to restore service. I assigned the act itself to `assuring`; closure and mitigation acts remain `remediating`.

8. **T0346 — refuse to present an unreconciled number as fact**  
   **Competing roots:** `transacting` and `assuring`. The wording does not explicitly say the number is financial, but “unreconciled account/actuals/ledger” forms a strong recurring financial cluster in the corpus; I therefore placed it in `transacting`, though `assuring` is defensible.

9. **T0387 — run a sourcing event**  
   **Competing roots:** `deciding` and `coordinating`. A sourcing event coordinates bidders and process steps, but its purpose is to generate and select among procurement options; absent a procurement root, `deciding` is the narrower telic fit.

10. **T0548 — name a single incident commander**  
    **Competing roots:** `remediating` and `authorizing`. Naming the commander confers operational authority, but the corpus presents it as part of incident response whose reason is rapid restoration. I assigned it to `remediating`; a taxonomy with a richer command-and-control corpus might instead put it under authorization.

# E. What the corpus is missing

The corpus strongly supports information retrieval, software-state manipulation, organizational control, communication, assurance, finance, incident handling, publication, and hiring. It does not provide enough evidence to derive roots for several purposes a general taxonomy of human acts would likely need:

- **physical production:** manufacturing, construction, cultivation, transport of goods, and repair of physical objects;
- **caregiving:** clinical treatment, nursing, childcare, emergency aid, and other acts aimed at bodily welfare;
- **learning:** teaching, practice, coaching, and durable skill acquisition rather than knowledge retrieval;
- **scientific experimentation:** intervention designed to generate causal evidence, as distinct from search or operational testing;
- **consumption and enjoyment:** eating, recreation, play, aesthetic experience, and entertainment;
- **social bonding:** affection, celebration, mourning, reconciliation, and community formation beyond instrumental coordination;
- **civic representation:** legislation, voting in public institutions, adjudication, taxation, and delivery of public services;
- **market exchange beyond finance operations:** selling, negotiating price, fulfilling goods, and customer purchase decisions;
- **environmental stewardship:** conservation, waste reduction, habitat restoration, and resource management;
- **personal self-maintenance:** rest, exercise, hygiene, reflection, and management of one’s own non-work life.

Accordingly, the eleven roots are exhaustive only for this corpus. Their resemblance to familiar distinctions—information, operations, coordination, authority, assurance, governance, decision, remedy, finance, publishing, and staffing—arises from repeated act clusters here, but the missing domains mean they should not be treated as a proven universal taxonomy.
