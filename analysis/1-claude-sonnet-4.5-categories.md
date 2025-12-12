# Ground Truth Corpus: Digital Interaction Types

Below is a corpus of 56 distinct multiparty interaction types, sourced from five domains to test the breadth and MECE properties of the Syntelos taxonomy.

| Source Domain | Original Action/Verb | Context | Syntelos Path | Ambiguity Level | Rationale |
|---------------|---------------------|---------|---------------|-----------------|-----------|
| **Stripe API** | POST /v1/refunds | Merchant initiates customer refund | /trade/swap | Low | Clear reversal of a purchase transaction; same economic category as original swap. |
| **Stripe API** | POST /v1/disputes | Customer contests a charge | /govern/settle | Medium | Could be /trade/swap (reversal) or /govern/settle (formal conflict resolution); settled on latter due to formal arbitration nature. |
| **Twilio API** | POST /Messages | Send SMS to recipient | /share/notify | Low | One-way push notification; clear fit for notify. |
| **Zoom API** | POST /meetings | Schedule video conference | /align/meet | Low | Pure time synchronization for interaction. |
| **GitHub API** | POST /repos/{owner}/{repo}/pulls | Submit code for review | /share/create | Medium | Could be /share/create (co-creation) or /operate/assign (task delegation); chose create as primary telos is collaborative contribution. |
| **GitHub API** | POST /repos/{owner}/{repo}/issues | Report bug or request | /share/assist | Low | Clear support request for resolution. |
| **Slack API** | POST /chat.postMessage | Send message to channel | /relate/chat | Low | Sustaining connection through conversation. |
| **Slack API** | POST /reactions.add | React to a message | /relate/chat | Low | Social acknowledgment within existing connection. |
| **DocuSign API** | POST /envelopes | Send document for signature | /govern/process | Medium | Could be /trade/* (contract finalization) or /govern/process (legal procedure); chose process as signing is a compulsory legal step. |
| **SendGrid API** | POST /mail/send | Deliver marketing email | /share/notify | Low | One-way promotional broadcast. |
| **Uber App UI** | "Request Ride" | Passenger summons driver | /trade/swap | Low | Exchange payment for transportation service. |
| **Uber App UI** | "Split Fare" | Divide payment among riders | /trade/swap | Low | Sub-interaction of swap; multiple parties settling a shared purchase. |
| **Tinder App UI** | "Swipe Right" | Express interest in dating | /relate/seek | Low | Finding new connection explicitly. |
| **Tinder App UI** | "Super Like" | Strong interest signal | /relate/seek | Low | Intensified version of seeking connection. |
| **Duolingo App UI** | "Challenge Friend" | Compete in language learning | /relate/play | Low | Shared activity for enjoyment within learning context. |
| **Epic MyChart UI** | "Request Appointment" | Patient books medical visit | /align/meet | Medium | Could be /care/treat (medical care) or /align/meet (scheduling); chose meet as initial telos is time synchronization, with care occurring later. |
| **Epic MyChart UI** | "Share Records" | Patient authorizes provider access | /govern/permit | Low | Clear access rights management. |
| **Venmo App UI** | "Request Payment" | Ask friend to pay | /trade/lend | Medium | Could be /trade/swap (if splitting bill) or /trade/lend (if settling debt); ambiguous without context. |
| **Instagram App UI** | "Block User" | Prevent unwanted contact | /govern/permit | Low | Revoking access/interaction rights. |
| **Airbnb App UI** | "Instant Book" | Reserve accommodation immediately | /align/book | Low | Clear resource reservation. |
| **Schema.org Action** | ReserveAction | Hold resource for future | /align/book | Low | Standard booking action. |
| **Schema.org Action** | VoteAction | Cast ballot | /govern/vote | Low | Explicit collective decision-making. |
| **Schema.org Action** | EndorseAction | Publicly support entity | /govern/advocate | Low | Persuasion/debate prior to decision. |
| **MCP Tool** | filesystem_read | Agent reads local file | **GAP** | High | This is unilateral data access, not a multiparty interaction; taxonomy doesn't cover single-actor resource access. |
| **MCP Tool** | brave_web_search | Agent searches internet | **GAP** | High | Unilateral query to impersonal system; no counterparty relationship. |
| **Ethereum Smart Contract** | createProposal (DAO) | Member submits governance vote | /govern/vote | Low | Initiating collective decision process. |
| **Ethereum Smart Contract** | stake (DeFi) | Lock tokens for rewards | /trade/invest | Low | Committing assets for future gain. |
| **Ethereum Smart Contract** | swap (DEX) | Exchange cryptocurrencies | /trade/swap | Low | Direct asset exchange. |
| **Ethereum Smart Contract** | mint (NFT) | Create unique token | /share/create | Medium | Could be /trade/* if commercial, but creation is primary telos. |
| **OIDC4VC** | Credential Issuance | Authority issues verifiable credential | /govern/identify | Low | Asserting identity/credentials. |
| **OIDC4VP** | Presentation Request | Verifier requests proof | /govern/identify | Low | Verification of credentials. |
| **DIDComm: Trust Ping** | trust_ping/1.0 | Test connection liveness | **GAP** | High | This is infrastructure maintenance, not an intent-driven interaction; no clear telos in taxonomy. |
| **DIDComm: Introduction** | out-of-band/1.1/invitation | Broker introduces two parties | /relate/seek | Medium | Could be /relate/seek or a new category; facilitating new connections through intermediary. |
| **DIDComm: Issue Credential** | issue-credential/2.0 | Credential issuance flow | /govern/identify | Low | Clear identity assertion protocol. |
| **DIDComm: Present Proof** | present-proof/2.0 | Proof presentation protocol | /govern/identify | Low | Verification workflow. |
| **DIDComm: Mediate** | coordinate-mediation/1.0 | Establish message routing | **GAP** | High | Infrastructure configuration for future interactions; not itself a purposeful interaction. |
| **US Courts PACER** | File Motion | Attorney submits legal document | /govern/process | Low | Compulsory legal procedure. |
| **US Courts PACER** | Request Transcript | Party orders court record | /share/ask | Low | Retrieving specific data point. |
| **SEC EDGAR** | Submit Form 10-K | Company files annual report | /share/notify | Medium | Could be /govern/audit (compliance) or /share/notify (broadcast); chose notify as primary telos is disclosure. |
| **Online Voting (Parliament)** | Cast Vote (Proxy) | Member votes on behalf of another | /govern/vote | Low | Clear collective decision with delegation. |
| **Online Voting (Board)** | Call for Quorum | Chair verifies attendance | /govern/chair | Low | Managing procedural flow. |
| **Online Voting (Board)** | Motion to Table | Postpone decision | /govern/chair | Low | Procedural control action. |
| **Clinical Trial Portal** | Obtain Informed Consent | Researcher gets patient agreement | /govern/permit | Medium | Could be /care/* or /govern/permit; chose permit as granting rights is the telos. |
| **Clinical Trial Portal** | Randomize Participant | Assign to control/treatment group | /share/study | Low | Methodical investigation workflow. |
| **Peer Review System** | Submit Manuscript | Author proposes paper | /share/study | Low | Knowledge generation through formal process. |
| **Peer Review System** | Assign Reviewer | Editor delegates review | /operate/assign | Low | Task delegation to subordinate. |
| **Peer Review System** | Blind Review Submission | Reviewer assesses paper | /operate/evaluate | Low | Performance assessment against standard. |
| **Lab Equipment IoT** | Reserve Microscope Time | Researcher books instrument | /align/book | Low | Resource reservation. |
| **Lab Equipment IoT** | Grant Remote Access | PI authorizes team member | /govern/permit | Low | Access rights management. |
| **Smart Home (Matter)** | Unlock Door Remotely | Homeowner opens for guest | /operate/actuate | Low | State change of device. |
| **Smart Home (Matter)** | Share Thermostat Control | Grant family member access | /govern/permit | Low | Permission delegation. |
| **Medical IoT** | Transmit Vitals (Patient→Clinic) | Device sends health data | /share/notify | Medium | Could be /care/treat (part of care) or /share/notify (data push); chose notify as transmission itself is telos. |
| **Telemedicine Platform** | Request Second Opinion | Patient seeks additional diagnosis | /care/treat | Low | Medical care interaction. |
| **Conference Management** | Submit Talk Proposal | Speaker proposes session | /share/perform | Medium | Could be /share/teach or /share/perform; chose perform as broadcasting is primary telos. |
| **Academic Collaboration** | Co-author Invitation | Researcher invites collaboration | /share/create | Low | Co-creation of intellectual property. |
| **Grant Management Portal** | Submit Funding Application | Researcher requests grant | /trade/give | Medium | Could be /share/ask or /trade/give; chose give as soliciting donation. |
| **Open Source Governance** | Propose License Change | Maintainer suggests policy shift | /govern/vote | Low | Initiating collective decision on governance. |

---

## Summary of Findings

### Coverage Analysis
- **Well-covered domains**: /trade/*, /govern/*, /relate/*, /align/*, /share/* handle most multiparty interactions effectively
- **Identified gaps**: 
  1. **Infrastructure/maintenance actions** (trust ping, mediate) - these are system-level, not human-intent-level
  2. **Unilateral resource access** (filesystem read, web search) - taxonomy explicitly targets multiparty interactions, so this is expected
  3. **Hybrid consent scenarios** (informed consent in medical research) - ambiguous between /care and /govern

### Ambiguity Patterns
- **Medium ambiguity** common in:
  - Nested interactions (scheduling a doctor's appointment: /align/meet vs /care/treat)
  - Dual-purpose actions (SEC filing: compliance vs disclosure)
  - Context-dependent exchanges (Venmo request: splitting bill vs settling debt)

### Recommendations
1. **Add decomposition examples**: Show how complex interactions (e.g., "book surgery") decompose into `/align/meet` (schedule) → `/care/treat` (procedure) → `/trade/swap` (payment)
2. **Clarify infrastructure exclusion**: Explicitly state taxonomy covers *purposeful human-intent interactions*, not protocol-level handshakes
3. **Expand /govern/identify**: Strong coverage for credentials but may need subcategories for consent vs verification vs assertion
4. **Consider /operate boundaries**: IoT device control fits well, but "read sensor data" (unilateral) creates edge cases

### Validation Outcome
The taxonomy demonstrates **strong MECE properties** for its target domain (multiparty, purposeful digital interactions). Gaps identified are primarily:
- Expected exclusions (unilateral actions)
- Infrastructure concerns (out of scope)
- Decomposition needs (addressable through guidance, not new categories)

**Verdict**: The taxonomy is robust and well-suited for agentic AI policy enforcement, with minor clarifications needed for nested interaction scenarios.