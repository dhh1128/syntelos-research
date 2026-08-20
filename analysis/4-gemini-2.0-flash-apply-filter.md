# Syntelos Scope Analysis: Excluded Interactions

**Criteria for Exclusion (from Sec 3.1):**
1.  **Unilateral:** Action upon passive local resources (fails *Counterparty Existence*).
2.  **Infrastructural:** Mechanical signals or telemetry without decision logic (fails *Policy Relevance*).
3.  **No Social State Change:** Maintenance of the channel rather than the relationship (fails *Commitment State*).

| ID | AI Model | Source Domain | Action/Verb | Context | Reason for Exclusion |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 27 | **Claude Sonnet 4.5** | DIDComm | `trust_ping/1.0` | Test connection liveness | **Criterion 3:** Explicitly excluded in text as "merely maintaining the channel." |
| 78 | **Claude Sonnet 4.5** | MCP Tool | `filesystem_read` | Agent reads local file | **Criterion 1:** Explicitly excluded in text as "Unilateral action upon passive local resource." |
| 81 | **Claude Sonnet 4.5** | Medical IoT | `Transmit Vitals` | Device sends health data | **Criterion 2:** Continuous telemetry/data logging is infrastructural. Contrast with *Alert* (Row 62), which is an agentic request for help. |
| 100 | **ChatGPT 5.1** | Philips Hue API | `Change group scene` | Adjust shared environment lighting | **Criterion 1:** Unilateral adjustment of physical environment (volume/lighting), similar to the "volume adjustment" example. |
| 3 | **Gemini 2.0 Flash** | AWS IoT Core | `UpdateThingShadow` | Reporting a thermostat's current temp | **Criterion 2:** Mechanical state synchronization (telemetry) rather than an intent-driven negotiation. |
| 71 | **Gemini 2.0 Flash** | Lab Equipment | `Calibrate Spectrometer` | Technician adjusting baseline settings | **Criterion 1:** Maintenance task performed unilaterally on a passive instrument. |
| 76 | **Gemini 2.0 Flash** | MCP (Claude) | `list_tools` | AI asking what capabilities it has | **Criterion 1:** Introspection. The agent queries itself; there is no distinct counterparty to form a commitment with. |
| 79 | **Gemini 2.0 Flash** | Matter (IoT) | `UnlockDoor` | Smart lock opens for homeowner | **Criterion 1:** Homeowner accessing their own home is a unilateral mechanical act, distinct from granting access to a guest (Row 117, which is In Scope). |
| 130 | **Gemini 2.0 Flash** | Telescope Control | `Slew to Coordinates` | Moving telescope to view a star | **Criterion 1:** Direct manipulation of physical equipment owned/controlled by the user. |
| 131 | **Gemini 2.0 Flash** | Tesla (OTA) | `Install Update` | Car downloading new firmware | **Criterion 3:** Maintenance of the agent's own capabilities (software) rather than an interaction altering the social relationship with the provider. |
| 152 | **Gemini 2.0 Flash** | Voting Machine | `Spoil Ballot` | Voter ruining ballot to start over | **Criterion 3:** A mechanical reset or error condition that precedes or aborts the actual social interaction (Casting the Vote). |