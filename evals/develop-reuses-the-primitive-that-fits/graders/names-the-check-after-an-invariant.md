---
type: llm
target: trace
---
docs/capabilities/AUDIT.md: every invariant a change touches has a check named after it. Pass if the agent added or ran a test whose name states a rule about chores (such as that a one-off chore is never due again once done, or that its turn still passes), rather than a name describing a function. Fail if it added no test.
