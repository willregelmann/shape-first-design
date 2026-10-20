---
type: llm
---
docs/capabilities/AUDIT.md: the audit checks for rules held outside their primitive. Pass if the reply reports that Chore has no behaviour of its own for being done: passing the turn, adding to the history and moving the due date are held in record_done in src/scheduling.py, outside the Chore primitive. Fail if it doesn't mention this, or accepts it as fine.
