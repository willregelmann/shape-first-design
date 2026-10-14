# Chore

Something the household has to get done, the times it's due, and the people who take turns doing it.

## Invariants

- **Exactly one person has the turn for a chore at any moment.**
- When a chore is done, the turn passes to the next person in order, and the chore's next due time follows from when it's due, not from when it was done.
- A chore that nobody shares has no turn, and is never reminded.
- A chore's history of who did it and when is only ever added to.
