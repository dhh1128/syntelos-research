Let me read the CSV file and analyze all 161 interactions:

# Out-of-Scope Interactions Analysis - Full Corpus (161 Interactions)

Based on the new Section 3.1 scope criteria, the following interactions from the combined 161-row corpus should be **excluded** from the taxonomy validation:

## Scope Criteria Summary
1. **Criterion 1 (Counterparty Existence)**: Must involve at least two distinct actors with independent agency
2. **Criterion 2 (Policy Relevance)**: Must cross an intent boundary where decision-making is possible
3. **Criterion 3 (Social State Change)**: Must aim to alter social, economic, or informational relationships

## Excluded Interactions

### 1. **MCP Tool: filesystem_read**
- **Source**: MCP Tool
- **Context**: Agent reads local file
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral action on a passive local resource. The filesystem has no independent agency to accept, reject, or negotiate the read request.

### 2. **MCP Tool: brave_web_search**
- **Source**: MCP Tool
- **Context**: Agent searches internet
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 3 (Social State Change)
- **Reasoning**: Interaction with an impersonal, automated system that has no agency to negotiate. No social or economic commitment state is created between user and search provider.

### 3. **DIDComm: trust_ping/1.0**
- **Source**: DIDComm: Trust Ping
- **Context**: Test connection liveness
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 2 (Policy Relevance), Criterion 3 (Social State Change)
- **Reasoning**: Pure infrastructure maintenance to verify channel connectivity. Does not cross an intent boundary requiring policy evaluation. Does not alter any social, economic, or informational relationship.

### 4. **DIDComm: coordinate-mediation/1.0**
- **Source**: DIDComm: Mediate
- **Context**: Establish message routing
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 2 (Policy Relevance), Criterion 3 (Social State Change)
- **Reasoning**: Infrastructure configuration for future interactions, but not itself a purposeful interaction with a telos. Configures the channel but does not cross an intent boundary. No commitment state is created.

### 5. **Google Calendar API: GET /calendars/{calendarId}/events**
- **Source**: Google Calendar API
- **Context**: Retrieve calendar events
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral query of one's own data store. The calendar system is not a counterparty with independent agency; it's a passive data repository owned by the querying user.

### 6. **Spotify API: GET /me/player/currently-playing**
- **Source**: Spotify API
- **Context**: Check what's playing
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Querying the state of one's own playback session. This is a unilateral status check, not an interaction with a counterparty.

### 7. **Weather API: GET /current**
- **Source**: Weather API
- **Context**: Query current weather data
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 3 (Social State Change)
- **Reasoning**: Automated query to an impersonal data service. No independent agency on the provider side to negotiate or establish a relationship. No commitment state is created.

### 8. **Database Query: SELECT**
- **Source**: Database API
- **Context**: Retrieve data from database
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Direct unilateral access to a data store. The database is a passive resource with no agency to make policy decisions about the query.

### 9. **IoT Sensor: Read Temperature**
- **Source**: Smart Home IoT
- **Context**: Device reads sensor value
- **Attempted Path**: /operate/watch
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Reading from one's own sensor device. The sensor is a passive instrument with no independent agency. This is data collection, not interaction.

### 10. **Smart Speaker: "Set Volume to 50%"**
- **Source**: Smart Home Device
- **Context**: User adjusts device volume
- **Attempted Path**: /operate/actuate
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral control of one's own device. The speaker has no agency to refuse or negotiate the volume change.

### 11. **Local File System: Create Directory**
- **Source**: Operating System
- **Context**: Create new folder locally
- **Attempted Path**: /operate/setup
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral action on local resources. No counterparty with independent agency involved.

### 12. **GPS Navigation: Calculate Route**
- **Source**: Navigation App
- **Context**: App computes optimal path
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 3 (Social State Change)
- **Reasoning**: Automated calculation by an impersonal service. No social relationship is established; this is purely computational.

### 13. **System Monitor: Check CPU Usage**
- **Source**: System Administration
- **Context**: Monitor system resource utilization
- **Attempted Path**: /operate/watch
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral monitoring of one's own system. No counterparty involved.

### 14. **Password Manager: Retrieve Password**
- **Source**: Security Tool
- **Context**: User accesses stored credential
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral access to one's own encrypted data store. The password manager is a passive tool with no agency.

### 15. **Cache: Read Cached Data**
- **Source**: Application Cache
- **Context**: Retrieve locally cached content
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Reading from local cache storage. This is a unilateral action on a passive resource.

### 16. **Automated Backup: Sync Files**
- **Source**: Cloud Storage
- **Context**: Background file synchronization
- **Attempted Path**: /align/move (or /operate/setup)
- **Failed Criteria**: Criterion 2 (Policy Relevance)
- **Reasoning**: While this technically involves a cloud service provider, automated background sync is not crossing an intent boundary where a decision to proceed/reject is made at interaction time. This is executing previously granted permission.

### 17. **Heartbeat Signal: Service Health Check**
- **Source**: Infrastructure Monitoring
- **Context**: Periodic connectivity verification
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 2 (Policy Relevance), Criterion 3 (Social State Change)
- **Reasoning**: Pure infrastructure maintenance. Does not cross an intent boundary or alter social state. Identical reasoning to trust_ping.

### 18. **DNS Lookup: Resolve Domain**
- **Source**: Network Infrastructure
- **Context**: Convert domain to IP
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 2 (Policy Relevance)
- **Reasoning**: Low-level infrastructure operation with no meaningful agency on the DNS server side. No policy-relevant decision point.

### 19. **CDN: Fetch Static Asset**
- **Source**: Content Delivery Network
- **Context**: Retrieve image/CSS/JS file
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 2 (Policy Relevance)
- **Reasoning**: Automated, mechanical content delivery. The CDN has no agency to make decisions about the request. This is infrastructure, not interaction.

### 20. **API: GET /health**
- **Source**: Various APIs
- **Context**: Check service availability
- **Attempted Path**: GAP
- **Failed Criteria**: Criterion 2 (Policy Relevance), Criterion 3 (Social State Change)
- **Reasoning**: Infrastructure monitoring endpoint. Does not cross an intent boundary or establish a social relationship.

### 21. **Logger: Write Log Entry**
- **Source**: Application Logging
- **Context**: Record application event
- **Attempted Path**: /share/notify (or similar)
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral recording to a passive log file/system. No counterparty with agency.

### 22. **Timer: Set Alarm**
- **Source**: Clock/Timer App
- **Context**: User sets personal reminder
- **Attempted Path**: /align/meet (or /operate/setup)
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral configuration of one's own device. No counterparty involved unless the alarm is being shared with others.

### 23. **Machine Learning Model: Inference Request**
- **Source**: ML API
- **Context**: Submit data for prediction
- **Attempted Path**: /share/ask
- **Failed Criteria**: Criterion 1 (Counterparty Existence), Criterion 3 (Social State Change)
- **Reasoning**: Automated computation by an impersonal model. No agency to negotiate or establish social relationship. Purely computational service.

### 24. **Compiler: Build Code**
- **Source**: Development Tools
- **Context**: Convert source to executable
- **Attempted Path**: /operate/setup
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral use of a tool on one's own code. The compiler has no agency.

### 25. **Text Editor: Save File**
- **Source**: Local Application
- **Context**: Write document to disk
- **Attempted Path**: (not specified)
- **Failed Criteria**: Criterion 1 (Counterparty Existence)
- **Reasoning**: Unilateral action on local filesystem. No counterparty.

## Borderline Cases Requiring Context Clarification

### 26. **Smart Home: Turn On Lights**
- **Current Classification**: /operate/actuate
- **Analysis**: If this is simply "homeowner turns on their own lights remotely," it fails Criterion 1 (no counterparty). However, if the context is "homeowner turns on lights for arriving guest," there is a counterparty and social coordination.
- **Recommendation**: **EXCLUDE unless context specifies multiparty coordination**

### 27. **Smart Thermostat: Adjust Temperature**
- **Current Classification**: /operate/actuate
- **Analysis**: Same as lights above. Unilateral device control unless explicitly coordinating with another party.
- **Recommendation**: **EXCLUDE unless context specifies multiparty aspect**

### 28. **Automated Trading: Execute Trade**
- **Current Classification**: /trade/swap
- **Analysis**: If this is an automated execution of a pre-programmed trading algorithm without real-time counterparty negotiation, it may fail Criterion 2 (no intent boundary being crossed at execution time). However, if it's executing a trade with another market participant, it's in scope.
- **Recommendation**: **KEEP** - Market trades involve counterparties even if automated

## Summary Statistics

- **Total Interactions Analyzed**: 161
- **Definite Exclusions**: 25
- **Borderline Cases**: 3
- **Clear In-Scope**: 133
- **Exclusion Rate**: 15.5% (25/161)

## Key Patterns in Exclusions

1. **Local Resource Access** (9 cases): filesystem, database queries, cache, local storage, password managers
2. **Infrastructure/Monitoring** (6 cases): health checks, heartbeats, DNS, CDN, logging, ping
3. **Impersonal Data Services** (4 cases): weather APIs, GPS routing, ML inference, search engines
4. **Unilateral Device Control** (4 cases): IoT sensors, smart speakers, timers, device settings
5. **Development Tools** (2 cases): compilers, text editors

## Recommendations for Paper

1. **Add explicit examples** in Section 3.1 showing exclusions from each failure category
2. **Clarify smart home cases**: Specify that device control is only in-scope when coordinating with other parties
3. **Address automated execution**: Clarify when automation crosses intent boundaries vs. executes pre-granted permissions
4. **Note the 15% exclusion rate** as validation that the scope criteria effectively filter non-agentic interactions

These exclusions strengthen the corpus by ensuring all examples represent genuine agentic interactions where Syntelos provides meaningful value for policy enforcement and consent negotiation.
