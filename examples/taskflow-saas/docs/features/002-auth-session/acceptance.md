# Acceptance Criteria — FEAT-002

### AC-FEAT002-01: Sign and verify valid session tokens
- **Given** a user ID and role (`lead` or `developer`)
- **When** `createSessionToken` signs the payload and `verifySessionToken` verifies it
- **Then** the decoded session matches the original user ID and role

### AC-FEAT002-02: Reject tampered or missing session tokens
- **Given** a missing, malformed, or tampered session token
- **When** `verifySessionToken` or `requireSession` evaluates it
- **Then** it returns `null` (or HTTP `401` at the API boundary)
