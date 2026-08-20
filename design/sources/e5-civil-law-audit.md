### **1. THE DOCTRINE OF JURIDICAL ACTS**

The civil-law tradition classifies juridical acts (*acte juridique*, *Rechtsgeschäft*, *negozio giuridico*, *rechtshandeling*) along several doctrinal axes, each with distinct legal consequences. Below are the standard classifications, with glosses and (where confident) code references:

#### **A. Core Distinctions**
1. **Unilateral / Bilateral / Plurilateral** (*unilatéral / bilatéral / plurilatéral*; *einseitiges / mehrseitiges Rechtsgeschäft*; *unilaterale / bilaterale / plurilaterale*)
   - *Unilateral*: One party’s declaration suffices (e.g., will, revocation of a power of attorney).
   - *Bilateral*: Two parties’ declarations (e.g., contract).
   - *Plurilateral*: Three or more parties (e.g., partnership agreement).
   - **Code**: French *Code civil* art. 1101 (contract as bilateral); BGB § 145 (offer as unilateral); UNCERTAIN for plurilateral.

2. **Onerous / Gratuitous** (*à titre onéreux / à titre gratuit*; *entgeltlich / unentgeltlich*; *oneroso / gratuito*)
   - *Onerous*: Each party receives a counter-performance (e.g., sale, lease).
   - *Gratuitous*: One party confers a benefit without compensation (e.g., gift, gratuitous loan).
   - **Code**: French *Code civil* art. 1107; BGB § 516 (gift).

3. **Inter vivos / Mortis causa** (*entre vifs / à cause de mort*; *unter Lebenden / von Todes wegen*; *inter vivos / mortis causa*)
   - *Inter vivos*: Takes effect during the actor’s lifetime.
   - *Mortis causa*: Takes effect upon death (e.g., will, legacy).
   - **Code**: French *Code civil* art. 893 (definition of *libéralité*); BGB § 1937 (testament).

4. **Consensual / Solemn (Formal) / Real** (*consensuel / solennel / réel*; *formlos / formbedürftig / Realakt*; *consensuale / formale / reale*)
   - *Consensual*: Valid by mere agreement (e.g., most contracts).
   - *Solemn*: Requires a specific form (e.g., notarial deed for real estate sale in France, *Code civil* art. 1589-2).
   - *Real*: Requires delivery of the object (e.g., deposit, *Code civil* art. 1915; BGB § 607 for loan).
   - **Code**: French *Code civil* art. 1108 (form requirements); BGB § 311b (real estate contracts).

5. **Commutative / Aleatory** (*commutatif / aléatoire*; *fest / aleatorisch*; *commutativo / aleatorio*)
   - *Commutative*: Performance is certain and equivalent (e.g., sale).
   - *Aleatory*: Performance depends on an uncertain event (e.g., insurance, gambling).
   - **Code**: French *Code civil* art. 1104; BGB § 762 (gambling contracts).

6. **Causal / Abstract** (*causal / abstrait*; *kausal / abstrakt*; *causale / astratto*)
   - *Causal*: Validity depends on the underlying *cause* (e.g., French law, *Code civil* art. 1128).
   - *Abstract*: Validity is independent of *cause* (e.g., German *Abstraktionsprinzip*, BGB § 929 for property transfer).
   - **Code**: French *Code civil* art. 1128; BGB § 929 (abstract transfer).

7. **Acte juridique vs. Fait juridique** (*acte juridique / fait juridique*; *Rechtsgeschäft / Realakt*; *negozio giuridico / fatto giuridico*)
   - *Acte juridique*: Voluntary act intended to produce legal effects (e.g., contract, will).
   - *Fait juridique*: Legal effects arise from events not intended to create them (e.g., tort, birth, death).
   - **Code**: French *Code civil* art. 1100-1 (post-2016 reform); BGB § 823 (tort as *Realakt*).

---

### **2. EXPRESSIBILITY AUDIT**

| **Axis**               | **Verdict**       | **Explanation**                                                                                                                                                                                                 |
|-------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unilateral/Bilateral/Plurilateral | **INEXPRESSIBLE** | No facet captures the number of parties. *Modality* (may/must/must-not) is about norms, not party structure. *Channel* (e.g., "private") might *imply* bilateral, but this is not explicit. **Add a "party-structure" facet.** |
| Onerous/Gratuitous      | **DERIVABLE**     | *Telos* could distinguish: `/trade` (onerous) vs. `/care` or `/share` (gratuitous). But this is strained—*telos* is about *purpose*, not *consideration*. **Risk of misclassification.**                          |
| Inter vivos/Mortis causa | **DERIVABLE**     | *Telos* could include `/govern/mortis-causa`, but this is not in the current roots. **Would require adding a new telos branch.**                                                                               |
| Consensual/Solemn/Real  | **INEXPRESSIBLE** | *Requisites* (e.g., "notarized") covers *solemn*, but *real* acts (e.g., delivery) are not captured. *Effect* (e.g., "modify") does not distinguish between consensual and real. **Add a "formality-type" facet.** |
| Commutative/Aleatory    | **INEXPRESSIBLE** | No facet captures risk allocation. *Telos* (`/trade` vs. `/align`) might hint at it, but this is not reliable. **Add an "uncertainty" facet (certain/aleatory).**                                                |
| Causal/Abstract         | **INEXPRESSIBLE** | *Telos* is not *cause*. *Effect* (e.g., "create commitment") does not distinguish between causal and abstract acts. **Add a "causality" facet (causal/abstract).**                                               |
| Acte juridique/Fait juridique | **INEXPRESSIBLE** | No facet distinguishes voluntary acts from involuntary events. *Modality* (e.g., "must-not") applies only to acts, not *faits*. **Add an "intentionality" facet (voluntary/involuntary).**                     |

---

### **3. THE ABSTRACTION PRINCIPLE**

The **Abstraktionsprinzip** (German law) separates:
1. **Verpflichtungsgeschäft** (obligational act, e.g., sale contract, BGB § 433).
2. **Verfügungsgeschäft** (disposition, e.g., property transfer, BGB § 929).

These are **two independent juridical acts** with separate validity conditions. French law, by contrast, merges them (*solo consensu*, *Code civil* art. 1196).

#### **Can the Proposal Represent This?**
- **No, it cannot.**
  - The proposal’s `(effect, state-kind)` vector treats a transaction as a **single act** with multiple effects (e.g., "create commitment" + "modify resource").
  - The **Abstraktionsprinzip requires two distinct acts**, each with its own `(effect, state-kind)` vector and independent validity.
  - The proposal’s **authorization gate** (strictest cell demands) assumes a single act, not two linked but independent ones.
  - **What breaks**: The proposal cannot represent that the *Verfügungsgeschäft* remains valid even if the *Verpflichtungsgeschäft* is void (e.g., a minor sells a car without capacity to contract, but the transfer itself is valid if the minor had authority to dispose).

#### **Required Fix**
- **Add a "transaction-layer" facet** (obligation/disposition) to allow multiple acts per transaction.
- **Decouple validity gates** so that one act’s invalidity does not automatically invalidate the other.

---

### **4. CAUSA AND ITS ABSENCE**

#### **Distinguishing Telos from Causa**
| **Feature**       | **Telos (Proposal)**                          | **Causa (Civil Law)**                          |
|--------------------|-----------------------------------------------|------------------------------------------------|
| **Definition**     | Subjective purpose of the act (e.g., `/trade`). | Objective legal justification for the act (e.g., consideration, donation, security). |
| **Function**       | Descriptive (why the act was done).           | Normative (whether the act is legally valid).  |
| **Example**        | A gift’s *telos* is `/care`.                  | A gift’s *causa* is *libéralité* (gratuitous transfer). |
| **Legal Effect**   | None (unless used for interpretation).        | Determines validity (e.g., French *Code civil* art. 1128: no *cause* = void). |

#### **Hazard: Conflation Risk**
- Implementers may assume that if an act has a *telos*, it has a *causa*, leading to **false validity conclusions**.
  - Example: A German abstract transfer (*Verfügungsgeschäft*) has no *causa* but may have a *telos* (`/trade`). An implementer might wrongly assume it is invalid for lacking *causa*.
- **Mitigation**: The spec must **explicitly state**:
  1. *Telos* is **not** *causa*.
  2. *Causa* is a **jurisdiction-specific validity condition**, not a facet.
  3. Some acts (e.g., German abstract transfers) are **valid without *causa***.

---

### **5. THE FIVE CHANNELS**

The proposal’s **private / registry / agency / tribunal / assembly** partition **fails to map cleanly** to civil-law institutions:

| **Civil-Law Institution**       | **Proposed Channel** | **Problem**                                                                                                                                                                                                 |
|----------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Latin Notary (*notaire*, *Notar*)** | ?                    | A *notaire* is **not a tribunal** (no adjudicative power) but **not a private party** either (public officer). Their *acte authentique* has **executory force** (French *Code civil* art. 1369). **No fit.** |
| **Land Register (*Grundbuch*)**  | Registry             | Correct, but **registration is constitutive** (BGB § 873), not just evidentiary. The proposal’s "registry" channel does not distinguish between **constitutive** and **declarative** registers.               |
| **Commercial Register (*greffe*)** | Registry             | Correct, but **administrative acts** (e.g., registration of a company) are **not just "registry"**—they may be **agency** or **tribunal** depending on the jurisdiction.                                      |
| **Administrative Act (*acte administratif*)** | Agency / Tribunal | **Misclassification risk**: An *acte administratif* (e.g., a building permit) is **not a tribunal act** (no adjudication) but **not purely "agency"** either (may be subject to *recours pour excès de pouvoir*). |
| **Legislative Assembly**         | Assembly             | Correct, but **civil-law assemblies** (e.g., *Assemblée nationale*) often delegate rulemaking to **agencies** (e.g., *décrets*), which the proposal might misclassify as "agency" rather than "assembly."      |

#### **Required Fixes**
1. **Add a sixth channel: "notarial"** for *actes authentiques*.
2. **Distinguish "constitutive registry" from "declarative registry"** in the *channel* facet.
3. **Clarify that "agency" includes administrative acts** but **not all administrative acts are "agency"** (some are quasi-judicial).

---

### **6. THE REQUISITES SET**

The proposal’s **writing, signature, witnessed, notarized, filed, recorded, published, noticed, certified** list **misses key civil-law form requirements** and **contains false friends**:

| **Civil-Law Concept**            | **Proposal’s Term** | **Problem**                                                                                                                                                                                                 |
|-----------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Forme authentique**             | Notarized           | **False friend**: "Notarized" in common law means a notary’s signature, but *forme authentique* (French *Code civil* art. 1369) requires **notarial drafting + signature + seal**, with **executory force**. |
| **Forme sous seing privé**        | Writing + Signature | Correct, but **German *Textform*** (BGB § 126b) allows electronic text without signature, which the proposal’s "writing" does not capture.                                                                  |
| **Notarielle Beurkundung**        | Notarized           | **False friend**: German *notarielle Beurkundung* (BGB § 128) is **more than "notarized"**—it requires **notarial reading + explanation + signature**, with **higher evidentiary weight** than common-law notarization. |
| **Schriftform**                   | Writing             | **False friend**: German *Schriftform* (BGB § 126) requires **handwritten signature**, not just "writing." The proposal’s "writing" is too broad.                                                           |
| **Eintragung (registration)**     | Recorded            | Correct, but **German *Grundbucheintragung*** (BGB § 873) is **constitutive**, not just evidentiary. The proposal’s "recorded" does not distinguish.                                                       |
| **Publication (e.g., *Journal Officiel*)** | Published       | Correct, but **French *publicité foncière*** (real estate publication) is **not just "published"**—it is a **constitutive formality** for some acts.                                                        |
| **Missing: *Forme électronique*** | —                   | French *Code civil* art. 1366 (electronic form) and EU eIDAS Regulation require **qualified electronic signatures**, which the proposal does not capture.                                                   |

#### **Required Fixes**
1. **Replace "notarized" with two values**:
   - `notarized-simple` (common-law notarization).
   - `notarized-authentic` (civil-law *forme authentique* / *notarielle Beurkundung*).
2. **Add**:
   - `textform` (German *Textform*).
   - `electronic-signature` (with subtypes for qualified/advanced).
   - `constitutive-registration` (distinct from declarative).
3. **Clarify that "writing" ≠ *Schriftform***.

---

### **7. MODALITY AND OMISSION**

The proposal’s **may / must / must-not** triple **fails to capture civil-law deontics** because:

1. **Nullity ≠ Prohibition**
   - An act can be **forbidden (*illicite*) but valid** (e.g., a contract to sell drugs is voidable but not automatically void in some systems).
   - An act can be **permitted but void** (e.g., a contract lacking *cause* in French law).
   - The proposal’s **modality** conflates **permission** with **validity**.

2. **Nullité absolue / relative**
   - *Nullité absolue* (e.g., violation of public order) can be invoked by anyone and is not waivable.
   - *Nullité relative* (e.g., incapacity) can only be invoked by the protected party.
   - The proposal’s **must-not** does not distinguish these.

3. **Omission as a First-Class Act**
   - Civil law recognizes **omissions as juridical acts** (e.g., failure to revoke a power of attorney, *Code civil* art. 2004).
   - The proposal’s **modality** treats omission as a norm, but **not as an act with its own (effect, state-kind)**.

#### **Required Fixes**
1. **Split "must-not" into**:
   - `prohibited` (illegal but may be valid).
   - `void` (invalid by operation of law).
   - `voidable` (valid until annulled).
2. **Add a "nullity-type" facet** (absolute/relative).
3. **Clarify that omission is an act** with its own `(effect, state-kind)` (e.g., "preserve commitment" by failing to revoke).

---

### **8. VERDICT**

**The claim of "jurisdiction-invariant closed facets" is indefensible in its current form.** The proposal’s common-law origins create **systematic mismatches** with civil-law doctrine, particularly in:
1. **The Abstraktionsprinzip** (cannot represent two independent acts).
2. **Causa vs. telos** (risk of conflation).
3. **Form requirements** (false friends like "notarized").
4. **Channel classification** (Latin notary and administrative acts break the partition).
5. **Deontics** (nullity ≠ prohibition).

#### **Required Changes (Ranked by Severity)**
1. **Add a "transaction-layer" facet** (obligation/disposition) to handle the **Abstraktionsprinzip** (critical for German law).
2. **Replace "notarized" with `notarized-simple` and `notarized-authentic`** (critical for Latin notary systems).
3. **Add a "causality" facet** (causal/abstract) and **explicitly disclaim that *telos* = *causa*** (critical for French/German validity rules).
4. **Add a "party-structure" facet** (unilateral/bilateral/plurilateral) (critical for contract theory).
5. **Add a "formality-type" facet** (consensual/solemn/real) (critical for delivery-based acts).
6. **Add a "nullity-type" facet** (absolute/relative) and **split "must-not" into `prohibited`/`void`/`voidable`** (critical for deontics).
7. **Add a sixth channel: "notarial"** (critical for *actes authentiques*).
8. **Clarify that "writing" ≠ *Schriftform* and add `textform`/`electronic-signature`** (critical for form requirements).
9. **Add "constitutive-registration" as a requisite** (critical for land registers).

#### **If These Changes Are Not Made**
The proposal **should abandon the claim of jurisdiction-invariance** and instead **publish jurisdiction-specific profiles** that override the closed facets where necessary. The current design **cannot survive contact with civil law** without fundamental revision.
