# Invariant

A statement about a project that holds at every moment, in every build of it. [Primitives](PRIMITIVE.md), [capabilities](CAPABILITY.md) and [interfaces](INTERFACE.md) each state their invariants, and the map's promises are made of nothing else.

An invariant says what holds, never how. So it survives a rewrite, and two builders who read it expect the same thing from the code.

## Invariants

- **Every invariant holds at every moment in every build, could visibly break, leaves room for different implementations, and is one a capable builder could plausibly get wrong without being told.**
- It lives in the file of the thing it's about, and is stated there once. Another file relies on it and never restates it differently.
- An invariant that ties primitives together says whether it holds at every moment or catches up, and by when.
- It states a limit, never its value, and names a technology only when the project must meet it.
- The few a project would be a different project without are bold, and no others.
