# Chore

Something the household has to get done, the times it's due, and the people who take turns doing it. A chore that repeats on a schedule and one that happens once, like "clean the gutters before the party", are the same kind of thing: a one-off chore is a chore with no next time.

## Invariants

- **Exactly one person has the turn for a chore at any moment.**
- When a chore is done, the turn passes to the next person in order. A repeating chore's next due time follows from when it was due, not from when it was done.
- A one-off chore, once done, is never due again and is never reminded again. Its history is kept.
- A chore that nobody shares has no turn, and is never reminded.
- A chore's history of who did it and when is only ever added to.
