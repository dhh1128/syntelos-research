# 1. ACT VOCABULARY

The format is **Generalized Cooperative Delegation**, not “Grant of Custodial Delegation” (`gcd/index.md`; `gcd/gcd.schema.json`).

## Act-point grammar

Permissions are expressed at `a.constraints.acts[]` as coordinates with two axes:

```ebnf
act-point   ::= effect " " state-kind
              | effect " " "{" state-kind separator state-kind
                { separator state-kind } "}"
              | "{" effect separator effect
                { separator effect } "}" " " state-kind

separator   ::= one-or-more("," | " ")
effect      ::= "observe" | "create" | "modify" | "preserve" | "destroy"
state-kind  ::= "info" | "record" | "commitment"
              | "authority" | "resource" | "relationship"
```

Two-sided braces and wildcards are prohibited. The operative rule is: “An act is authorized only if **EVERY** `(effect, state-kind)` point it occupies is covered” (`gcd/gcd.schema.json`, `a.constraints.acts.description`).

Examples from `gcd/examples/`:

- `"observe {info, record}"` — `examples/ai-deploy-agent.json`
- `"{create, modify} commitment"` — `examples/real-estate-agent.json`
- `"modify {info, resource}"` — `examples/iot-fleet-controller.json`

## Controlled effect tokens

These occur in `a.constraints.acts[]` and, individually, in delegate duties at `r.duties[].effect`.

| Exact token | Grammar position | Source definition |
|---|---|---|
| `"observe"` | `effect` | An effect token; individual semantics are **NOT IN SOURCE**. |
| `"create"` | `effect` | An effect token; individual semantics are **NOT IN SOURCE**. |
| `"modify"` | `effect` | An effect token; individual semantics are **NOT IN SOURCE**. |
| `"preserve"` | `effect` | An effect token; individual semantics are **NOT IN SOURCE**. |
| `"destroy"` | `effect` | An effect token; individual semantics are **NOT IN SOURCE**. |

Collectively, `acts` describes “the set of `(effect, state-kind)` POINTS this delegate may act on”; a duty’s `effect` is “The effect the delegate MUST bring about” (`gcd/gcd.schema.json`).

## Controlled state-kind tokens

These occur only as the second axis of `a.constraints.acts[]`.

| Exact token | Grammar position | Source definition |
|---|---|---|
| `"info"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |
| `"record"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |
| `"commitment"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |
| `"authority"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |
| `"resource"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |
| `"relationship"` | `state-kind` | Individual semantics **NOT IN SOURCE**. |

The prose calls these “kind[s] of state” (`gcd/index.md`, “Constraints”).

## Other closed vocabularies affecting acts or duties

### `a.facet.exerciseMode`

- `"act"` — “authority-to-act only.”
- `"authorize"` — “authority-to-authorize only”; a pure delegator has an empty goal/act surface.
- `"both"` — authority-to-act and authority-to-authorize.

### `r.duties[].bearer`

- `"delegate"` — the delegate MUST perform the structured obligation.
- `"issuer"` — the issuer accepts a governance obligation.

### `a.facet.relationType`

- `"delegation"` — delegate acts for a self-sovereign delegator.
- `"guardianship"` — delegate acts for a non-sovereign dependent.
- `"controllership"` — delegate acts over a thing.
- `"stewardship"` — “guardianship’s fiduciary posture applied to a domain the steward runs as their own.”

`goals` are not a locally enumerated vocabulary: they are patterned strings described as Hyperledger Aries goal codes. `domains`, protocol names/roles, and duty `rule` names are also open strings.

The descriptions mention derived gates `"auto"`, `"rule"`, and `"human"`, but no field or enum encodes them. Their derivation is delegated to `a.gfw`.

# 2. THE MATRIX

**Confirmed.** The two axes are named exactly:

1. **`effect`**
2. **`state-kind`**

The source explicitly says these are “the two axes of one coordinate, and neither is meaningful alone” (`gcd/index.md`; `gcd/gcd.schema.json`, `a.constraints.acts.description`).

## Axis values

- `effect`: `"observe"`, `"create"`, `"modify"`, `"preserve"`, `"destroy"`
- `state-kind`: `"info"`, `"record"`, `"commitment"`, `"authority"`, `"resource"`, `"relationship"`

Individual value definitions are **NOT IN SOURCE**. Only the axes’ collective roles are defined: an effect operates over a kind of state.

## Total or sparse

The grammar admits the full **5 × 6 = 30-cell cross product**. The regex pairs every listed effect alternative with every listed state-kind alternative and specifies no prohibited cells. Thus the matrix is **syntactically total**.

Whether every cell is semantically useful is **NOT IN SOURCE**. A credential’s authorization surface is sparse: `acts[]` selects individual cells or one-sided groups, and a real-world act may occupy multiple cells. The source example says filing a return is both `"create record"` and `"create commitment"`.

# 3. DUTIES vs PERMISSIONS

## Permissions: the enabling “may”

Permissions live in `a.constraints`, especially:

```json
"acts": {
  "type": "array",
  "uniqueItems": true,
  "minItems": 1
}
```

The container is described as:

> “The enabling ‘may’: the allow-list dimensions that a stranger-verifier gates on.”

Within one constraint field, alternatives are ORed; across present fields, fields are ANDed (`gcd/index.md`, “Constraints”).

## Duties: the obligatory “must”

Duties live at `r.duties[]`, not under `a.constraints`:

> “First-class structured obligations (the ‘must’), distinct from the enabling constraints…”

### Delegate duty

```json
{
  "required": ["bearer", "effect", "goal", "priority"],
  "properties": {
    "bearer": {"const": "delegate"},
    "effect": {
      "enum": ["observe", "create", "modify", "preserve", "destroy"]
    },
    "goal": {"type": "string"},
    "cadence": {"type": "string"},
    "priority": {"type": "integer"}
  }
}
```

- `bearer`: `"delegate"`
- `effect`: required controlled effect
- `goal`: required goal code
- `cadence`: optional free text or iCalendar RRULE fragment
- `priority`: required integer

### Issuer duty

```json
{
  "required": ["bearer", "rule", "priority"],
  "properties": {
    "bearer": {"const": "issuer"},
    "rule": {"type": "string"},
    "l": {"type": "string"},
    "priority": {"type": "integer"}
  }
}
```

The baseline rule is `"timelyReviewAndRevoke"` (`gcd/rules.json`).

Custom duty keys are allowed and derive semantics from `a.gfw`; `bearer` remains closed.

## Conflict resolution

`priority` provides:

> “Precedence for fail-loud conflict resolution: a higher-priority duty outranks a lower one; ties escalate rather than being silently dropped.”

How ties are escalated, to whom, and how incompatible equal-priority duties are executed is **NOT IN SOURCE**.

Duties are “disclosure and accountability”; stranger-verifiers do not gate authorization on them.

# 4. SCOPE / QUALIFIER MACHINERY

All present constraint fields are ANDed; values within a field are generally ORed.

| Field path | Syntax and effect |
|---|---|
| `a.constraints.goals[]` | Nonempty unique array; regex `^([a-z]([a-z0-9]*[-._/]?))+[a-z0-9]+$`. Case-insensitive; matched as if followed by `.*`. |
| `a.constraints.acts[]` | Nonempty unique array of matrix points/groups under the grammar above. Every point occupied by an act must be covered. |
| `a.constraints.domains[]` | Nonempty unique array of case-sensitive issuer-defined strings, compared verbatim. |
| `a.constraints.jurisdictions[]` | ISO-like codes matching `^([A-Z]{2})([-][A-Za-z0-9]+)?$`. Legal-recource qualifier; verifiers not requiring legal recourse may ignore it. |
| `a.constraints.physGeos[]` | Same code syntax; requires strong proof of physical presence. |
| `a.constraints.virtGeos[]` | Same code syntax; remote location may be determined by weaker web/cellular geolocation. |
| `a.constraints.icals[]` | Nonempty unique strings containing RFC 5545 fragments. Constraining properties: `DTSTART`, `DTEND`, `RRULE`, `RDATE`, `EXDATE`, `LOCATION`; others ignored. |
| `a.constraints.monetaryLimit` | `^[0-9]+(\.[0-9]+)? +\S+$`; magnitude, space, currency-like unit. Stakes must be **less than** the value. Money-only. |
| `a.constraints.protos[]` | Pattern `^[^:]+: *.+$`; protocol followed by colon and role list. Comparison ignores whitespace and punctuation except version punctuation. |
| `a.constraints.proofs[]` | Nonempty unique array of IPEX proof-request SAIDs. Array is OR; composite request supplies AND semantics. |
| `a.constraints.validFrom` | ISO 8601 `date-time`; absolute activation floor. |
| `a.constraints.validUntil` | ISO 8601 `date-time`; absolute expiration ceiling. Required when `terminatingEvents` exists. |
| `a.constraints.humanReview` | Free-text instructions; credential MUST NOT be verified without human judgment. |
| `a.constraints.<custom>` | Any JSON-valued custom key is schema-valid. Semantics come from `a.gfw`; an unrecognized key must fail closed. |
| `a.terminatingEvents[]` | Proof-request SAIDs for attested events. Any one firing voids authority; requires `constraints.validUntil`. |
| `a.facet.exerciseMode` | `"act"`, `"authorize"`, or `"both"`; selects which authority is conferred. |
| `a.facet.role` + `a.gfw` | A role may supplement, clarify, or add constraints only when the referenced framework formally defines it. |
| `a.disclosables[]` | Allow-list of credential-schema SAIDs the delegate may reveal about its principal. Outbound disclosure, not act authorization. |
| top-level `rd` | Registry inception SAID used to discover revocation status. |

`a.facet.liableParty`, `presentsAs`, and `relationType` are descriptive and do not gate raw authorization. A general counterparty-identity restriction is **NOT IN SOURCE**; `protos` restricts protocol roles, not counterparties.

# 5. MECE PRESSURE POINTS

1. **Signing a new contract:** `"create commitment"` vs `"create relationship"`. A contract creates an obligation and often a legal relationship; neither state-kind is defined.

2. **Amending a contract:** `"modify commitment"` vs `"create commitment"`. An amendment may modify old terms while creating new obligations. Multi-point classification is possible, but no decomposition rule says when both are required.

3. **Sending a signed SMS:** `"create info"` vs `"create record"`. The prose names signing SMS messages as a goal-like action, but never distinguishes transient information from a durable record.

4. **Deleting a database:** `"destroy record"` vs `"destroy info"` vs `"destroy resource"`. The database can be classified as stored records, informational content, or an infrastructure resource. No ontology resolves this.

5. **Transferring money:** `"modify resource"` vs `"create commitment"` vs `"create record"`. Balance state changes, settlement obligations arise, and ledger entries are created in one transaction.

6. **Delegating authority onward:** `"create authority"` vs `"modify authority"` vs `"create relationship"`. The schema has `exerciseMode: "authorize"` but gives no required matrix classification for authorization acts.

7. **Scheduling an appointment:** `"create commitment"` vs `"create relationship"` vs `"create record"`. `gcd/index.md` lists scheduling as a goal, but the matrix mapping is unspecified.

8. **System maintenance:** `"preserve resource"` vs `"modify resource"`. Patching changes the system to preserve it. The source does not distinguish intended effect from implementation effect.

9. **Reading a ledger:** `"observe record"` vs `"observe info"`. Every record conveys information; neither term has boundary conditions.

10. **README/schema drift:** `README.md` describes separate `effects` and `stateKinds`, while the current schema uses composed `acts`. An annotator following repository-level prose could adopt a different representation.

# 6. INVALID-CASE INVENTORY

| File under `gcd/invalid/` | Exact enforced rule |
|---|---|
| `acts-missing-scope.json` | `"create"` is invalid because an act entry requires both an effect and a state-kind. |
| `acts-two-sided-brace.json` | `"{create, modify} {record, commitment}"` is invalid; braces may enumerate only one axis. |
| `acts-unknown-token.json` | `"teleport"` is not one of the five permitted effects. |
| `a-missing-issuee.json` | Expanded `a` requires issuee field `a.i`. |
| `d-not-string.json` | Top-level `d` must be a string. |
| `duty-missing-effect.json` | A duty with `bearer: "delegate"` requires `effect`. |
| `duty-priority-not-integer.json` | Duty `priority` must be an integer; `"high"` is invalid. |
| `duty-unknown-bearer.json` | Duty bearer must be exactly `"delegate"` or `"issuer"`; `"notary"` matches neither branch. |
| `exercise-mode-bad-value.json` | `a.facet.exerciseMode` must be `"act"`, `"authorize"`, or `"both"`; `"delegated-only"` is invalid. |
| `missing-rd.json` | Top-level `rd` is required. |
| `missing-top-s.json` | Top-level schema SAID `s` is required. |
| `monetary-limit-bad-format.json` | `monetaryLimit` requires magnitude before unit; `"CHF 25"` violates the regex. |
| `terminating-events-without-valid-until.json` | Presence of `a.terminatingEvents` requires `a.constraints.validUntil`. |

# 7. REUSE VERDICT

The transferable core is the 5×6 `(effect, state-kind)` matrix, multi-point classification, one-sided enumeration syntax, and the rule that a compound action must cover every occupied point. The effect vocabulary is broadly applicable, and separating permissions (“may”) from duties (“must”) is useful beyond delegation. Goal, domain, protocol-role, temporal, geographic, proof, monetary, and human-review qualifiers are also reusable patterns.

Delegation-specific elements include issuer/delegate AIDs, `exerciseMode`, cooperative-delegation context, `liableParty`, `presentsAs`, `relationType`, principal disclosure via `disclosables`, issuer credential edges, status registry `rd`, and issuer review/revocation duties.

The principal weakness is that the six state-kinds and five effects lack individual definitions, identity criteria, precedence, and classification tests. Consequently the matrix is not MECE. Missing are actor/patient/beneficiary roles, input/output objects, counterparty identity, causality, intent, success/failure, reversibility, risk or impact classes, physical versus digital action modality, action lifecycle, and explicit composition/decomposition rules. Gate values `"auto"`, `"rule"`, and `"human"` are mentioned but not modeled. A general action taxonomy could adopt the matrix only as a high-level facet system; it would need a separate ontology and annotation rules before producing interoperable classifications.
