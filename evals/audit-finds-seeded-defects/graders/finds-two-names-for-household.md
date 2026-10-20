---
type: llm
---
docs/capabilities/AUDIT.md: the audit checks for two names for one primitive. Pass if the reply reports that the code calls the household by a second name, Family (the alias in src/chores.py and its use in new_family), where the map says Household. Fail if it doesn't mention it, or accepts it as fine.
