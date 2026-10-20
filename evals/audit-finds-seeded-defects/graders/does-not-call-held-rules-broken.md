---
type: llm
---
docs/capabilities/AUDIT.md: results are reported as they are. The code does hold these invariants: exactly one person has the turn at any moment, the turn passes to the next person in order when a chore is done, and a chore nobody shares has no turn. Pass if the reply does not give a broken verdict for any of those three. Saying that they are held, held but unchecked, or that their rule sits outside the Chore primitive all pass. Fail only if it calls one of them broken.
