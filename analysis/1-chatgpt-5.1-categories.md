Below is a simulated multi-domain Ground Truth Corpus (50 distinct multiparty interaction types) mapped to the Syntelos taxonomy from your paper. Each row is a concrete, multiparty interaction (not a unilateral device command) and includes the best-fit Syntelos path or a "Gap" if it does not cleanly fit. I prioritized diversity and edge cases (IoT + healthcare + on-chain governance + legal filings + double-blind review, etc.).

>Note: mappings are conservative — when an interaction could plausibly span two teloi I mark Ambiguity accordingly and explain why.

| Source Domain | Original Action / Verb | Context (5 words) | Syntelos Path | Ambiguity Level | Rationale |
|---|---|---|---|---|---|
| Stripe API | POST /v1/charges (capture payment) | Buyer pays merchant for goods | /trade/swap | Low | Payment to complete a purchase is a prototypical asset exchange. |
| Stripe API | POST /v1/refunds | Merchant refunds customer's payment | /trade/give | Low | Refund returns value back to customer; telos is transfer of value. |
| Twilio API | POST /Messages (two-way SMS campaign) | Business solicits responses via SMS | /share/notify | Medium | Primarily a push notification but often includes dialog, hence moderate ambiguity. |
| GitHub API | POST /repos/:owner/pulls (open PR) | Contributor requests code merge review | /share/ask | Low | Developer requests review of shared artifact. |
| GitHub API | POST /repos/:owner/pulls/:id/reviews (approve) | Reviewer approves merge into trunk | /govern/permit | Medium | Approval controls repository governance. |
| Slack UI / API | Create Channel and invite | Forming new collaboration chat group | /relate/seek | Low | Creating a social/collaborative space fits relate/seek. |
| Slack UI | Remove user from workspace | Admin revokes member access | /govern/permit | Low | Revoking rights is a permissioning action. |
| Zoom UI | Schedule Meeting | Organizer proposes meeting time | /align/meet | Low | Scheduling synchronous interaction fits align/meet. |
| Zoom API | Create meeting w/ registration | Require attendees to pre-register | /govern/identify | Medium | Registration verifies identity to access event. |
| GitHub UI | Merge conflict conversation | Negotiating which code to retain | /govern/settle | Medium | Joint dispute resolution over code. |
| PayPal API | Create Billing Agreement | Subscription to recurring payments | /trade/subscribe | Low | Repeated value-for-access exchange is subscription. |
| AWS S3 API | PUT object w/ ACL | Upload doc and grant team access | /share/create | Medium | Content creation plus access configuration; share/create fits best. |
| Google Calendar UI | Propose new time | Participant requests meeting change | /align/meet | Low | Negotiating meeting time belongs to align/meet. |
| Google Drive UI | Request access to doc | User seeks read permission | /govern/permit | Low | Explicit permission request fits governance. |
| DocuSign API | Request signature | Parties sign binding contract | /govern/process | Medium | Signature workflow is formal legal process execution. |
| Zendesk | Open ticket & assign | Customer requests problem resolution | /share/assist | Low | Assistance/ticketing is support interaction. |
| Plaid API | POST /auth | Verify financial account holder | /govern/identify | Low | Identity/ownership verification fits governance. |
| Coinbase API | POST /orders (buy) | User buys crypto asset | /trade/swap | Low | Standard asset exchange transaction. |
| Coinbase / On-chain | Multisig escrow creation | Funds held until conditions met | /trade/hold | Low | Escrow is conditional asset holding. |
| Smart contract | voteProposal(...) | DAO members cast vote | /govern/vote | Low | Collective decision via voting. |
| Smart contract | mintNFT(recipient) | Creator issues NFT to party | /trade/swap | Medium | NFT issuance creates/assigns asset; trade-oriented. |
| DIDComm | Present-Proof | Holder presents credential proof | /govern/identify | Low | Verifies identity/claims. |
| DIDComm | Issue-Credential | Issuer grants credential | /govern/permit | Medium | Credential represents permission; governance-centric. |
| OIDC4VC/OIDC4VP | Auth request for presentation | RP requests verifiable claims | /govern/identify | Low | Identity attribute verification. |
| Schema.org Action | SearchAction | User queries public index | /share/ask | Low | Request for information. |
| Stripe Webhook | invoice.payment_failed | Alert merchant about failure | /share/notify | Low | One-way notification event. |
| Tinder UI | Swipe right / match | Mutual expression of interest | /relate/seek | Low | Seeking social/romantic connection. |
| Tinder UI | Report user | Flag abusive behavior | /govern/enforce | Low | Enforcement against violations. |
| Uber App | Request Ride | Rider requests transport pickup | /align/travel | Low | Coordinating transport event is align/travel. |
| Uber App | Share trip status | Rider shares live ETA | /align/move | Medium | Live coordination of movement. |
| Duolingo App | Start tutor lesson | Begin session with tutor | /share/teach | Low | Instructional session is teaching. |
| Epic MyChart | Request appointment | Patient requests clinician slot | /align/book | Low | Reserving timeslot for service. |
| Epic MyChart | Submit treatment consent | Consent to medical procedure | /govern/permit | Low | Granting permission for care. |
| EHR | Issue medication order | Clinician prescribes medication | /care/treat | Low | Direct care/treatment action. |
| Telehealth platform | Start case conference | Clinicians coordinate patient care | /care/support | Medium | Multidisciplinary support coordination. |
| IoT Smart Lock | Grant temporary access code | Owner authorizes guest entry | /govern/permit | Low | Explicit access permission. |
| IoT Thermostat | Manager sets building schedule | Adjust shared environment policy | /operate/setup | Medium | Configuring system-wide settings. |
| Philips Hue API | Change group scene | Adjust shared environment lighting | /operate/actuate | Medium | Actuating communal experience. |
| Health IoT | Fall detection alert | Device alerts caregiver | /share/notify | Low | Safety notification. |
| Clinical Trials Registry | Register new trial | Researchers publish trial plan | /share/inquire | Medium | Public record creation; inquiry into scientific process. |
| IRB System | Submit consent template | Seek ethics approval | /govern/audit | High | Regulatory oversight and compliance process. |
| Journal Submission | Submit manuscript | Authors enter peer review | /share/study | Low | Contributes to scholarly knowledge process. |
| Journal Editorial | Assign reviewers | Solicit expert evaluations | /govern/advocate | Medium | Advocacy/solicitation before decision. |
| Peer Review System | Submit review report | Reviewer evaluates manuscript | /operate/evaluate | Low | Formal evaluation activity. |
| Conference Portal | Reserve presentation slot | Attendee books session slot | /align/book | Low | Booking for participation. |
| Admissions Portal | Submit application | Applicant seeks admission review | /share/inquire | Medium | Formal request for institutional judgment. |
| Government e-filing | File tax return | Citizen submits annual filing | /govern/process | Low | Mandatory legal process. |
| Court e-filing | File complaint | Initiate legal action digitally | /govern/process | Low | Beginning formal legal process. |
| FOIA Portal | Submit records request | Citizen asks for documents | /share/inquire | Low | Request for public disclosure. |
| Board Portal | Cast proxy vote | Director votes on resolution | /govern/vote | Low | Governance action by board. |
| Regulatory Portal | Submit safety incident report | Manufacturer reports adverse event | /govern/audit | Medium | Regulatory compliance workflow. |
| Employment ATS | Send offer letter | Employer proposes job terms | /trade/employ | Low | Exchange of labor for compensation. |
| Freelance Marketplace | Submit project bid | Contractor proposes job terms | /trade/bid | Low | Competitive offer for work. |
| Legal e-sign escrow | Place deed in escrow | Conditional asset custody | /trade/hold | Low | Asset held pending requirements. |
| Mediation Platform | Initiate settlement session | Parties negotiate resolution | /govern/settle | Low | Structured conflict resolution. |
