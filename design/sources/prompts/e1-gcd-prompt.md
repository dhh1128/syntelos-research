You are analyzing source material for a taxonomy design effort. Read the material appended to this prompt (JSON Schema, rules, and prose docs for a credential format called GCD — "Grant of Custodial Delegation" or similar — that specifies what acts a delegate may take on behalf of a delegator).

TASK: produce a precise, compact structural extract. Do NOT summarize impressionistically. Quote exact token strings and enumerate exact enumerations.

Answer these, in this order, with headers:

1. ACT VOCABULARY. Enumerate EVERY controlled vocabulary token the schema defines for describing acts/effects/scopes/duties. Give the exact string, its position in the grammar, and its definition. If tokens compose (e.g. a two-axis code), show the grammar with an EBNF-ish sketch and 3 real examples from the examples/ files.

2. THE MATRIX. The design is believed to use a matrix: one axis = kind of effect an act has, another axis = where the effect manifests. Confirm or refute this from the source. Name the axes exactly as the schema names them. List every value on each axis with its definition. State whether the cross product is total (every cell meaningful) or sparse, and cite evidence.

3. DUTIES vs PERMISSIONS. How does the schema model duties (obligations) as distinct from permissions? Enumerate the fields, the modality vocabulary, and any priority/conflict-resolution machinery. Quote the relevant schema fragments.

4. SCOPE / QUALIFIER MACHINERY. How is an act narrowed (monetary limits, time bounds, counterparty restrictions, exercise mode, conditions)? Enumerate every qualifier mechanism with its syntax.

5. MECE PRESSURE POINTS. Where does this vocabulary risk ambiguity or overlap — i.e., where could two annotators reasonably classify the same real-world act differently? Give at least 5 concrete cases, each with the two competing classifications and why the source does not disambiguate. Be adversarial; do not be charitable.

6. INVALID-CASE INVENTORY. The invalid/ directory encodes the constraints the spec enforces. List each invalid case file and the exact rule it proves.

7. REUSE VERDICT. In <=250 words: if someone wanted to build a general taxonomy of ACTIONS (not just delegated ones) on top of this matrix, what transfers, what is delegation-specific and would not generalize, and what is missing.

Rules: cite exact filenames and field paths. Never invent a token that is not in the source. If something is not determinable from the material, say "NOT IN SOURCE" rather than guessing. Target 1200-2000 words total; density over prose.

=== SOURCE MATERIAL FOLLOWS ===
