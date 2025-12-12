# Syntelos Ground Truth Corpus

Here is a simulated scrape of 50 diverse digital interactions.

This dataset is designed to stress-test the MECE (Mutually Exclusive, Collectively Exhaustive) properties of your taxonomy. I have intentionally included "corner cases"—interactions that sit on the boundary lines between categories—to highlight where the paper may need tighter definitions.

### Analysis Summary
* **Total Interactions:** 50
* **Domains Covered:** FinTech/SaaS APIs, Mobile/Consumer Apps, Web3/IoT/Identity, Government/Legal, Academic/Science.
* **Performance:** The taxonomy performs very well on commercial and mechanical interactions (`/trade`, `/operate`).
* **Friction Points:** High ambiguity arose in "mixed motive" interactions (e.g., crowdfunding, algorithmic moderation, and compulsory payments like taxes/fines).

---

### The Syntelos Ground Truth Corpus

| Source Domain | Original Action/Verb | Context | Syntelos Path | Ambiguity | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Top 50 APIs** | | | | | |
| Stripe API | `POST /v1/refunds` | Returning funds to a dissatisfied customer | `/trade/swap` | Low | Reversal of a static value exchange is part of the swap lifecycle. |
| Twilio API | `POST /Messages` | Sending a 2FA code via SMS | `/share/notify` | Low | One-way push of information (code) without conversation. |
| Slack API | `users.admin.invite` | Adding a new employee to workspace | `/govern/permit` | Medium | Could be `/operate/setup` (provisioning), but the *telos* is granting access rights. |
| GitHub API | `PUT /pulls/merge` | Approving code to go to production | `/share/guide` | High | Is it `/operate/actuate` (deploying) or `/share/guide` (authoritative direction)? Paper suggests "Commitments." |
| Salesforce API | `PATCH /Lead/{ID}` | Updating sales prospect status to "Lost" | `/operate/watch` | Medium | Technically updating a record, but the intent is tracking state. |
| Zoom API | `POST /users/meetings` | Scheduling a video conference | `/align/meet` | Low | Perfect fit: synchronizing time for interaction. |
| AWS IoT Core | `UpdateThingShadow` | Reporting a thermostat's current temp | `/operate/watch` | Low | Passive observation of system state. |
| DocuSign API | `POST /envelopes` | Requesting a signature on a contract | `/govern/identify` | High | Is the telos the *signature* (Identity/Consent) or the *deal* (`/trade/deal`)? Using `/govern` as it validates the actor. |
| Spotify API | `POST /me/player/queue` | Adding a song to a shared party playlist | `/relate/play` | Low | Shared activity for enjoyment. |
| LinkedIn API | `POST /people/invite` | Sending a connection request to stranger | `/relate/seek` | Low | Finding new connections. |
| **2. Mobile Apps** | | | | | |
| Tinder UI | "Swipe Right" | Expressing romantic interest in a profile | `/relate/seek` | Low | Establishing connection for its own sake (initially). |
| Uber UI | "Request Ride" | Booking a car from home to airport | `/align/travel` | Medium | Could be `/trade/swap` (buying a service), but paper explicitly maps transit to `/align/travel`. |
| Duolingo UI | "Start Lesson" | User begins a French exercise | `/share/study` | Low | Generating knowledge through methodical investigation. |
| Epic MyChart | "Refill Prescription" | Patient requests more medication | `/care/treat` | Low | Clinical care context prevails over the logistics of pharmacy pickup. |
| TaskRabbit UI | "Confirm Tasker" | Hiring someone to assemble furniture | `/trade/employ` | Low | Contracting for human labor. |
| Calm App | "Start Meditation" | User begins a guided breathing session | `/care/support` | Medium | Is it `/care/support` (mental welfare) or `/serve/groom` (fitness/self-work)? |
| DoorDash UI | "Place Order" | Ordering dinner for delivery | `/trade/swap` | Medium | A mix of `/trade/swap` (food) and `/align/move` (delivery). The dominant telos is the purchase. |
| Twitter/X UI | "Block @User" | Preventing a user from viewing profile | `/govern/permit` | Medium | Revoking access rights (personal governance). |
| YouTube Studio | "Demonetize Video" | Platform removing ads from content | `/govern/enforce` | High | Is it `/trade/deal` (changing terms) or `/govern/enforce` (policing content)? "Enforce" fits safety/order. |
| Venmo UI | "Pay Friend" | Splitting a dinner bill | `/trade/give` | High | It's a reimbursement, not a purchase (`/swap`) or a gift (`/give`). Taxonomy lacks a "Transfer" utility node. |
| **3. Emerging Standards** | | | | | |
| Ethereum (DAO) | `vote(proposal_id)` | Casting a token-vote for a protocol change | `/govern/vote` | Low | Collective decision making. |
| DIDComm | `issue-credential` | University issuing a digital diploma | `/govern/identify` | Low | Asserting identity/credentials. |
| Matter (IoT) | `UnlockDoor` | Smart lock opens for homeowner | `/operate/actuate` | Low | Changing physical state of a device. |
| Uniswap (Web3) | `swapExactTokens` | Trading ETH for USDC | `/trade/swap` | Low | Instant value exchange on static terms. |
| OIDC4VP | `present_proof` | User sharing "Over 21" credential | `/govern/identify` | Low | Verifying attributes to a verifier. |
| Nostr Protocol | `kind: 1 (Text Note)` | Broadcasting a censorship-resistant post | `/share/perform` | Medium | Is it `/share/notify` (update) or `/share/perform` (broadcast)? Nostr emphasizes "Voice," so Perform fits. |
| Filecoin | `StorageDeal` | Renting hard drive space to store data | `/trade/subscribe` | Medium | Recurring access to a resource (storage). |
| Tesla (OTA) | `Install Update` | Car downloading new firmware | `/serve/maintain` | Medium | Routine prevention/upkeep of a system. |
| MCP (Claude) | `list_tools` | AI asking what capabilities it has | `/operate/ask` | **GAP** | This is an agent introspection. Is it `/share/ask`? `/operate/watch`? It doesn't fit human social telos well. |
| WorldCoin | `Verify Orb` | Scanning iris to prove personhood | `/govern/identify` | Low | Strongest example of high-assurance identity. |
| **4. Gov / Legal / Reg** | | | | | |
| Court API | "File Amicus Brief" | 3rd party submitting opinion to court | `/govern/advocate` | Low | Persuading prior to a decision. |
| IRS Portal | "Pay Balance" | Citizen paying tax bill | `/govern/process` | **GAP** | Is this `/trade/swap`? No, there is no "deal." It is compulsory. `/govern/process` is close, but lacks the "money" semantic. |
| City Council | "Motion to Table" | Moving an agenda item to next week | `/govern/chair` | Low | Managing the flow of procedure. |
| GDPR Request | "Data Erasure" | User demanding deletion of data | `/govern/enforce` | Medium | Enforcing legal rights against a data controller. |
| Notary Service | "Notarize Document" | Witnessing a signature officially | `/govern/audit` | Medium | Verifying adherence to rules/identity? Closest to Audit. |
| Border Control | "Deny Entry" | E-Gate rejecting a passport | `/govern/enforce` | Low | "Denying entry to a secure facility." |
| Patent Office | "Grant Patent" | State assigning IP rights to inventor | `/govern/permit` | High | Granting rights. Could be `/share/create` (IP), but it's a legal act. |
| Voting Machine | "Spoil Ballot" | Voter ruining ballot to start over | `/govern/vote` | Low | Part of the voting mechanics. |
| Building Dept | "Issue Code Violation" | Inspector flagging unsafe wiring | `/govern/audit` | Low | Verify adherence to building code standards. |
| **5. Academic / Science** | | | | | |
| Peer Review System | "Submit Review" | Scientist grading a colleague's paper | `/operate/evaluate` | Low | Assessing performance against a standard. |
| Lab Equipment | "Calibrate Spectrometer" | Technician adjusting baseline settings | `/serve/maintain` | Low | Routine upkeep of equipment. |
| University Portal | "Post Grades" | Professor finalizing student scores | `/operate/evaluate` | Low | Formal assessment. |
| Clinical Trial | "Informed Consent" | Patient agreeing to experimental risks | `/govern/permit` | Medium | Granting access to one's body/data for science. |
| arXiv.org | "Upload Pre-print" | Sharing findings before peer review | `/share/study` | Medium | Or `/share/notify`? "Study" implies the *process* of knowledge generation. |
| ResearchGate | "Request Full Text" | Asking author for a PDF copy | `/share/ask` | Low | Retrieving specific data/files. |
| Grant Portal | "Submit Proposal" | Lab asking for funding | `/trade/bid` | High | It is competing for funds (`/trade/bid`) but also science (`/share/study`). |
| IRB Portal | "Approve Protocol" | Ethics board clearing a study to run | `/share/guide` | Medium | Authoritative technical/ethical direction. |
| Mendeley | "Co-author Add" | Adding a name to a paper citation | `/share/create` | Low | Co-creation of IP. |
| Telescope Control | "Slew to Coordinates" | Moving telescope to view a star | `/operate/actuate` | Low | Remote device control. |

---

### Critical Gap Analysis for the PhD Candidate

Based on the simulated scrape, here are the three areas where the taxonomy struggled to map the "Real World" to a specific Telos.

**1. The "Compulsory Payment" Gap**
* **Interaction:** Paying taxes, paying a speeding ticket, paying court-ordered alimony.
* **The Problem:** These are financial transfers, so they gravitate toward `/trade`. However, `/trade` implies exchange or voluntary giving. `/govern` covers the compulsion (`/govern/enforce`) but doesn't explicitly handle the asset transfer.
* **Recommendation:** Clarify if `/trade/give` covers "Involuntary giving" or if `/govern/enforce` can carry a financial payload.

**2. The "Introspection" Gap (Agentic AI)**
* **Interaction:** An AI agent checking its own tool list (MCP `list_tools`) or a system checking its own health status (Heartbeat).
* **The Problem:** The taxonomy is "Interaction-centric" (between parties). Introspection is "Self-centric."
* **Recommendation:** You may need a reflexive category or clarify that internal agent loops are out of scope.

**3. The "Crowdfunding/Pledge" Ambiguity**
* **Interaction:** Kickstarter pledges or Grant writing.
* **The Problem:** A Kickstarter pledge is simultaneously `/trade/swap` (buying the product), `/trade/give` (supporting the creator), and `/trade/invest` (speculating on success).
* **Recommendation:** This highlights the "Proximate/Ultimate" tension. The user likely views it as `/trade/swap` (I want the gadget), while the platform views it as `/trade/give` (no guarantee of reward).