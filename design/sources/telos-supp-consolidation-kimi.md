## A. Covered

| Input group (pass) | Existing node |
|---|---|
| justice / adjudication / dispute / adjudicate (all passes) | judge |
| security / safety / protect / public-safety / enforcement | protect |
| property / ownership / transfer / stewardship (property sense) / estate / succession / inherit / prosperity / commerce / finance / funding / transact | transfer (mostly trade; estates give) |
| wellbeing / welfare / care / caregiving / heal / grooming | care |
| knowledge / understanding / inquiry / investigation / documentation / recordkeeping / account (records sense) | know |
| communication / inform / engagement (messaging sense) | communicate |
| learning / education / educate | instruct |
| promotion (kimi-01) | promote |
| coordination / scheduling / account-administration (logistics sense) | coordinate |
| creation / produce / craftsmanship / infrastructure / continuity / upkeep / maintenance / administer / culture | provide |
| compliance / accountability / conform-filings | conform |
| family / kinship / status / participation / staffing / selection / community / belong-style connection | belong (formal bonds: unite) |
| order / regulation / govern / governance (all passes) | see C |
| recreation / performance / entertainment | provide (see B) |
| privacy (ds-01, codex-01 autonomy in part) | protect |
| autonomy (residue) | transfer + protect |

Notes on non-obvious ones: **selection/staffing** is covered by belong — hiring changes who may act within a bounded organization. **Enforcement** (kimi-00) is protect's "enforce a barrier" clause. **Privacy/redaction** installs a barrier against an identified disclosure hazard — protect. **Engagement/connection** groups split cleanly: formation of bonds → belong/unite, message traffic → communicate, scheduling → coordinate.

## B. Nearly covered — defects in existing tests

1. **provide — "artifact" is too narrow.** Roughly eight passes independently grouped acts whose end is delivering an *event or service*, not an artifact: stage a performance, operate a gaming table, hold an exhibition, run a funeral, keep a lost-and-found service functioning, manage digital accounts. These satisfy provide's create/preserve semantics exactly but fail the literal test. Narrowest fix: "Does the act bring an artifact, **event, or service** into being, or keep one in a functional and available state?" The discriminating question against transfer (no value moves) and communicate (content may be absent — roulette) is untouched.

2. **judge — "contested claim" is too narrow.** Many acts grouped as adjudication are *ex parte* determinations: probate of an unopposed will, name change, adoption decree, status registration, default remedy. No contest exists, yet the act resolves legal status through a binding procedure. Narrowest fix: "Does the act resolve a contested claim **or authoritatively determine a legal status or entitlement** through a procedure whose determination binds?" The discriminating question against conform (binding procedure vs. filing against a standard) survives.

3. **protect — hazard-barrier wording misses compelled compliance after the fact.** Sanction, custody, and penalty enforcement (kimi-00 *enforcement*, codex-00 *security* in part) protect the same barriers but operate post-breach, not by installing or monitoring. Narrowest fix: add "**or respond to a breach of**" the barrier. Discrimination against judge (judge determines; protect executes) is preserved.

4. **know vs. conform boundary — internal records.** Accountability/recordkeeping acts (ds-00, ds-04, kimi-04) that are *not* against a stated external standard land in know only if "produce a representation" reaches routine logs. It does, but the tests as written invite double-counting with conform. Narrow fix: state explicitly that conform requires the external standard; otherwise records default to know. No extension change, just disambiguation.

5. **belong — "bounded group" should be confirmed to reach employment.** Several passes separated *staffing/selection* as if distinct; the test already covers it (hiring changes who may act in the organization). No wording change needed, but the test should be read to include roles, not just membership rosters.

## C. Not covered — candidate roots

**govern**

Definition: The act issues a rule, budget, appointment, policy, or directive that binds the members or officers of a collective body by virtue of the authority under which it is issued. Its end is the collective's settled direction itself — the rule exists because the act enacted it.

Outward test: *Does the act, at the moment it is performed, create or change a rule, allocation, office, or binding decision for a collective, such that members are obligated without any further act or anyone's uptake?*

Discriminating questions: against **judge** — judge resolves a claim between parties looking backward at a dispute; govern sets forward-looking direction for a body, no claim required. Against **belong** — belong changes who is inside the boundary; govern directs what the bounded body does. Against **coordinate** — coordinate fixes times/roles among consenting parties; govern binds regardless of individual agreement. Against **conform** — conform answers to an external standard; govern *issues* the standard.

Found independently in: all 15 passes (governance, govern, order, regulation, plus half of kimi's manage). Roughly 60+ acts. Examples: X0019 (budget adoption), X0428 (rulemaking), X0229 (institutional directive).

Existing tests tried: judge fails (no contested claim — enacting a budget contests nothing); conform fails (the act *is* the standard, not a filing against one); coordinate fails (a statute binds non-consenting parties and fixes no time or place); belong fails (membership unchanged by a budget); provide fails (a rule is not an artifact kept functional). Widening any of these to reach governance dissolves its discriminating question. This is the one clear new root the corpus supports.

## D. Rejected candidates

- **influence / persuade** (codex-04 *influence*, kimi-01 *promotion* residue, X0302 lobbying): the point is a change in another party's attention or choice, which the act does not determine. Killed by the **horizon screen**. The paid-placement residue is already promote.
- **recreation / entertain** as a root (codex-02, kimi-02 *performance*, ds-02 *produce* in part): where the act stages an event, provide covers it (see B1); where the claim is "amuse," the amusement lives in the audience's head — **horizon**. Participating in play for oneself appears too rarely to test.
- **exploit / subversion / transgress** (ds-02, kimi-02, kimi-03): these name *manner* (illegality, breach) not end. Strip the violation and the telos that remains is acquisition → transfer, or evasion → protect's shadow. Killed by **ultimate purpose**.
- **matchmaking / mediation** (kimi-01, kimi-04): facilitating a bond the parties must themselves form needs another party's uptake — **horizon** as an end, and unite covers the formal bond once formed. The vetting residue is know.
- **accountability** (ds-00, ds-04): where external, it is conform; where internal, know. **Mechanism-plus-standard**, no residual end.
- **autonomy** (codex-01, codex-04): names a *condition of the actor* (self-direction), not an outcome brought about; the acts distribute to transfer, protect, belong. Killed as a **property of the actor**, like the excluded secure.
- **connection / engagement** as standalone: every act in these groups resolves to belong, communicate, or coordinate; the label is a **subject area** (social life).
- **representation**-flavored groups (ds-03, ds-04, kimi-02 unplaced): correctly excluded **standing relation**.

## E. What this corpus still cannot tell you

The corpus is overwhelmingly institutional: legal, administrative, commercial, and platform-mediated acts performed in roles. It therefore never exercises:

1. **Ritual and commemoration.** Funeral-adjacent acts were the most consistently unplaced items across passes (embalming X0518, pallbearers X0183, mortuary acts in ds-04). Passes forced them into care, provide, or left them out. Whether *commemorate* is a root, a child of belong, or communicate is undecidable here; a corpus of weddings, funerals, religious observance, and civic ceremony would exercise it.
2. **First-person subsistence and self-care** — eating, sheltering, resting, treating oneself. Care's test reads on third parties; whether self-directed bodily maintenance is the same root is untested. Needs a corpus of daily-life and survival acts.
3. **Play as participation** (not staging): games, sport, exploration undertaken by the actor. Only edges appeared (operate roulette). A recreation/leisure corpus is needed.
4. **Creation for no audience or market** — private making, hobby craft, journaling. Provide and know were only ever exercised instrumentally here.
5. **Coercion/warfare between collectives** — govern appeared only in its legitimate, interior form. Whether command under conflict is the same node is unexercised.
