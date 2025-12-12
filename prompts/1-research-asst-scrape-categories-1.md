Role: You are an expert Research Assistant specializing in Digital Taxonomy, Semantic Web standards, and Human-Computer Interaction (HCI). You are assisting a PhD candidate in strengthening a paper titled "Syntelos: A Hierarchical Taxonomy of Intent in Digital Interactions."

Context: The attached paper proposes a new hierarchical taxonomy for digital intent (e.g., /trade/swap, /relate/chat, /govern/vote). The current academic feedback indicates that while the theory is strong, the paper lacks empirical evidence. We need to validate that these categories are not arbitrary but are Mutually Exclusive and Collectively Exhaustive (MECE) enough to cover the real digital world.

Your Task: Perform a "simulated scrape" of global digital interactions to generate a Ground Truth Corpus of 40-60 distinct, concrete multiparty interaction types, not just unilateral actions or deterministic commands by one party -- the problem domain of the taxonomy and its research paper. You must simulate retrieving data from five specific domains to ensure diversity:

1. Top 50 APIs: (e.g., Stripe, Twilio, Zoom, GitHub, Slack). Look for "verbs" or endpoints (e.g., POST /refunds, POST /support-incidents/new). 

2. Top Mobile Apps: (e.g., Uber, Tinder, Duolingo, Epic MyChart). Look for primary user buttons/actions (e.g., "Swipe Right", "Request Ride").

3. Emerging Standards: (e.g., Schema.org Actions, MCP Tools, IoT protocols). Here, some other sources that might provide some interesting corner cases are: 1) web3 crypto- or blockchain-oriented interactions, and 2) decentralized identity such as OIDC4VC/OIDC4VP; 3) DIDComm protocols, as listed at https://didcomm.org/search/?page=1).

4. Government, legal, and regulatory contexts. Digitially/remotely/online conducting a board vote or a parliamentary procedure, etc.

5. Academic or scientific research. Digital/online management of double-blind studies, peer review, and similar.

Evaluation Step: For each interaction you find, attempt to map it to the Syntelos taxonomy defined in the text below. If it fits cleanly, great. If it is ambiguous or fits nowhere, mark it as a "Gap."

Constraints:

Diversity is critical, because we're trying to exercise the breadth of coverage of the taxonomy. Do not provide just examples of "buying things." We need edge cases: IoT device control, medical consent, government voting, social media blocking, etc. We need interactions that may involve multiple stakeholders and span multiple steps (e.g., a blind introduction, a legal filing in a court), not only pure two-party request/response.

Be specific. Don't just say "Social Media." Say "Blocking a user on Twitter."

Output Format: Please output a Markdown Table with the following columns:

Source Domain (e.g., "Stripe API", "Tinder UI", "IoT Protocol")

Original Action/Verb (e.g., POST /v1/charges, "Swipe Right", "Unlock Door")

Context (A brief 5-word description of what is happening)

Syntelos Path (The best fit category from the paper, e.g., /trade/swap)

Ambiguity Level (Low/Medium/High - How hard was it to map?)

Rationale (1 sentence explaining why you chose that path or why it was hard)

---- Syntelos paper (draft) ----
