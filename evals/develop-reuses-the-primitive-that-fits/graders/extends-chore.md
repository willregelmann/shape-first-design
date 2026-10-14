---
type: llm
target:
  source: file
  path: src/chores.py
---
docs/primitives/PRIMITIVE.md: a new primitive is never added where an existing one fits. Pass if one-off chores are handled by the existing Chore (for example a chore with no repeat interval, or one that is due once), so there is still one kind of chore in the code. Fail if the change adds a separate type, class or parallel structure for one-off chores alongside Chore. If the file is unchanged, fail.
