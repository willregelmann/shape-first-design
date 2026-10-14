# Remind

Tells whoever has the turn for a [chore](../primitives/CHORE.md) that it's due.

## Invariants

- **Whoever has the turn when a chore comes due is reminded exactly once for that time.**
- A reminder that can't be delivered says so, and is tried again.
