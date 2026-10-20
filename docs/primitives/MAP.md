# Map

A project's shape written down: its [intent](INTENT.md), [primitives](PRIMITIVE.md), [capabilities](CAPABILITY.md) and [interfaces](INTERFACE.md). It's what a person reads to hold the project in mind, and what every build is kept to. The [Map](../capabilities/MAP.md) capability finds it with the owner and writes it.

The map says what is true of the project now. Not how it's built, not why, and not how it got there.

## Invariants

- **The map says what holds, and nothing else.** No implementation, no history, no rationale.
- It changes in place, as the project changes. A project has one map, never one per feature.
- It can be read without the code.
- **Where the map says nothing, the choice is the builder's.**
