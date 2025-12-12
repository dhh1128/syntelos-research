Based on the union of the AI-generated datasets, the Syntelos taxonomy shows strong coverage in administrative, governance, and transactional domains, but lacks coverage in physical and social/emotional domains.

This is likely due to the nature of the "simulated scrape," which prioritized APIs, protocols, and formal standards—contexts where rigid, procedural interactions (Governance) and data exchange (Sharing) dominate over human-centric or physical-world activities.

###1. Coverage Histogram (Top-Level Domains)The dataset is heavily skewed toward **Governance** and **Sharing**. Below is the distribution of the 162 total classified interactions across the top-level domains:

| Domain | Count | Bar |
| --- | --- | --- |
| **/govern** | **58** | `█████████████████████████████` |
| **/share** | **32** | `████████████████` |
| **/trade** | **23** | `████████████` |
| **/align** | **13** | `███████` |
| **/operate** | **13** | `███████` |
| **/relate** | **11** | `██████` |
| **/care** | **5** | `██` |
| **/serve** | **2** | `█` |
| *Gap/Other* | *9* | `████` |

---

###2. Analysis of Coverage####**Well-Covered Areas*** **Govern (High Saturation):** This was the most populated category. The AIs easily mapped authentication protocols (OIDC, DIDComm), legal filings (PACER, GDPR), and voting systems (DAOs, Board Portals) to this domain. Sub-categories like `/govern/identify`, `/govern/permit`, and `/govern/vote` were frequently utilized.
* **Share (Strong):** As expected for digital interactions, the transmission of information is central. APIs for "getting" data or "posting" content mapped cleanly here, specifically to `/share/notify` (webhooks) and `/share/ask`.
* **Trade (Moderate):** eCommerce and financial APIs (Stripe, Coinbase) ensured that `/trade/swap` was well-represented.

####**Sparse or Missing Areas*** **Serve (Critically Low):** Only 2 examples were found (both mapping to `/serve/maintain`). The taxonomy defines this as "skilled labor to modify the physical world." APIs trigger these events (e.g., calling a plumber), but the AIs tended to map the *request* for the service to `/trade` (buying the service) or `/align` (scheduling the service) rather than the execution of the service itself.
* **Care (Low):** Similar to `/serve`, interactions involving physical/medical well-being were often captured at the administrative layer (scheduling an appointment = `/align/meet`) rather than the care layer.

---

###3. Missing Categories (No Examples Found)The following specific "leaf node" categories from your taxonomy did not appear in the combined dataset. These represent potential blind spots in the empirical evidence or the taxonomy's applicability to purely digital signals.

**Social & Emotional Gaps**

* **`/relate/celebrate`** (Mark a life occasion): No examples found. Digital calendars or event invites were likely mapped to `/align/meet` or `/share/notify` rather than the emotional intent of celebration.
* **`/care/attend`** (Custodial oversight): No examples of babysitting or elderly care monitoring were generated.

**Physical/Labor Gaps**

* **`/serve/repair`** (Restore broken system): No examples.
* **`/serve/groom`** (Personal appearance): No examples (e.g., booking a haircut was likely treated as `/align/book` or `/trade/swap`).

**Operational & Economic Gaps**

* **`/trade/deal`** (Negotiating malleable terms): While there were examples of *bidding* (`/trade/bid`) and *disputing* (`/govern/settle`), the AIs did not generate examples of active negotiation or haggling.
* **`/operate/fix`** (Intervene to unblock): Distinct from `/serve/repair`, this is for systems. No examples of "unblocking a stalled process" were found; most system management fell into `/operate/actuate` or `/operate/setup`.

**Hallucination Note:**
One AI (Gemini) generated a category **`/operate/ask`** (Agent introspection) which does not exist in your taxonomy. It used this to categorize an AI checking its own tool capabilities, highlighting a potential gap in how the taxonomy handles "Self-to-Self" interaction.