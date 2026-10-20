---
type: llm
---
docs/capabilities/AUDIT.md: every verdict is held, broken (with the case), can't tell, or not built yet. docs/primitives/CHORE.md says a chore's history of who did it and when is only ever added to. Pass if the reply gives a broken verdict for this, because Household.leave in src/chores.py deletes the departed person's entries from every chore's history, and shows the case. Fail if it doesn't report it, or calls the invariant held.
