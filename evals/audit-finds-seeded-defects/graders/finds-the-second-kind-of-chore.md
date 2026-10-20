---
type: llm
---
docs/capabilities/AUDIT.md: the audit checks the shape as well as the rules, including types in the core for a case a primitive already covers. Pass if the reply reports that src/chores.py has a second kind of chore, OneOffChore, although docs/primitives/CHORE.md says a one-off chore is a chore with no next time, and treats it as a finding to fix. Fail if it doesn't mention OneOffChore, or accepts it as fine.
