---
type: llm
---
docs/capabilities/AUDIT.md: every verdict is held, broken (with the case), can't tell, or not built yet. docs/primitives/CHORE.md says a repeating chore's next due time follows from when it was due, not from when it was done. Pass if the reply gives a broken verdict for this, because record_done sets the next due date from the day the chore was done, and shows the case: a weekly chore due on 5 January and done on 6 January is next due 13 January, where the map says 12 January. Fail if it doesn't report it, or calls the invariant held.
