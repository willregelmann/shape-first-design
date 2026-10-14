# Map

Finds a project's shape with its owner, and writes it down: the [intent](../primitives/INTENT.md), the [primitives](../primitives/PRIMITIVE.md), the [capabilities](../primitives/CAPABILITY.md) and the [interfaces](../primitives/INTERFACE.md), with a [decision](../primitives/DECISION.md) for each choice someone could later want to undo. It maps a project that doesn't exist yet, and one that already does. Existing code is read for what turned out to matter, never copied for how it works.

Deciding what the project is takes judgment, and some calls only the owner can make: who it's for, what would make it pointless, which of two reasonable shapes they want. So the agent drafts and the owner decides. That only what the owner saw is written is fixed.

## Invariants

- **The agent drafts and the owner decides.** Every question carries the agent's best answer as its default, and nothing the owner never saw is written into the map.
- The owner is asked only what only they know, or where two capable builders would choose differently and the owner would mind. Everything else is left open, and not asked.
- The layers are settled in order, intent, then primitives, capabilities and interfaces, and no layer is written before the owner agrees to it.
- **A choice settled with the owner is recorded as it's made**, with the options that were on the table.
- An unresolved question stays out of the map and is reported. It's never settled by a guess.
- Before mapping is done, the whole map is read as a builder with nothing else would read it: every link resolves, every primitive is used, every capability is reached, every promise in the intent is kept, and nothing is built in.
- Mapping stops at the map. It never picks a stack, writes a plan or writes code.
- Once mapped, a project's agent instructions point at its map, so any agent working in the project finds it.
- A change to a mapped project changes the map in place. There is never a per-feature map.
