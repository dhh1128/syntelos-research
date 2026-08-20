You are analyzing source material for a taxonomy design effort. Appended below is (a) the Custos specification — a standard for governed domains, constitutions, and evaluating decisions against them — and (b) a Q&A doc from Utina, an evaluation engine implementing Custos.

CONTEXT YOU NEED: a separate standard called Syntelos defines a hierarchical taxonomy of human/agent INTERACTIONS classified by telos (purpose), with paths like /relate/chat, /share/ask, /transact/buy. Its current scope is limited to interaction-oriented behaviors. Someone is considering expanding Syntelos so it can also name LEGAL/GOVERNANCE ACTS — Utina's demo currently uses ad-hoc strings like "open-bank-account", "seat-the-board", "amend-operating-agreement", "declare-dividend", "approve-budget", "hire-vp-sales". The question is what a normative vocabulary would have to cover to serve Custos/Utina.

TASK. Answer these with headers. Be precise and quote the spec.

1. WHERE ACTS APPEAR IN CUSTOS. Identify every place in the Custos spec where an action/decision/act is named, referenced, or typed. Quote the field names, the grammar, and say whether the act name is opaque to the spec (just a string) or structured. Cite section numbers.

2. WHAT CUSTOS NEEDS FROM AN ACT VOCABULARY. Derive, from the spec's own machinery (constitution computation, decision evaluation, authority, scope, quorum, delegation, revocation, whatever exists), the REQUIREMENTS a normative act vocabulary would have to satisfy. Be concrete: for each requirement, cite the spec mechanism that generates it. Distinguish hard requirements from nice-to-haves.

3. THE ACTS THEMSELVES. From the spec, its worked examples/vectors, and the Utina Q&A, enumerate every distinct real-world act that is named or implied. Group them. Aim for completeness — this is the empirical corpus a taxonomy would have to cover.

4. STRUCTURE LATENT IN THOSE ACTS. Looking at that corpus, what dimensions distinguish the acts from one another? Candidate dimensions to test (accept, reject, or refine each with evidence): who is affected; reversibility; whether the act changes the governing rules vs operates under them; whether it binds a third party; whether it creates/transfers/extinguishes a right; whether it requires a counterparty's assent; formality/registration requirement; whether it is a speech act vs a physical act. Propose additional dimensions the corpus reveals.

5. THE SCOPE PROBLEM. Syntelos v1 classifies by TELOS (purpose of an interaction). Legal acts are often classified by EFFECT or by INSTITUTIONAL FORM, not purpose. Argue rigorously whether a single taxonomy can serve both, or whether they are orthogonal facets that must be modeled separately. Take a position; do not fence-sit. Give the strongest counterargument to your own position.

6. RECURRING JURISPRUDENTIAL PRIOR ART. Name existing legal/philosophical taxonomies of acts that a standards effort should cite (e.g. Hohfeldian incidents, speech act theory, contract-formation doctrine, agency law, corporate-governance action classes, ISO/legal ontologies like LKIF or FIBO). For each: one line on what it classifies and whether it is a good fit. Only name things you are confident actually exist; mark anything uncertain as UNCERTAIN.

Rules: cite exact section numbers and filenames. Never invent spec content. If not determinable, say "NOT IN SOURCE". Target 1500-2500 words; density over prose.

=== SOURCE MATERIAL FOLLOWS ===
