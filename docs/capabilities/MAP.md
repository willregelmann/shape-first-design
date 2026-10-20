# Map

Finds a project's shape with its owner, and writes it down as the [map](../primitives/MAP.md): the [intent](../primitives/INTENT.md), the [primitives](../primitives/PRIMITIVE.md), the [capabilities](../primitives/CAPABILITY.md) and the [interfaces](../primitives/INTERFACE.md). It maps a project that doesn't exist yet, and one that already does. Existing code is read for what turned out to matter, never copied for how it works.

Deciding what the project is takes judgment, and some calls only the owner can make: who it's for, which of two reasonable shapes they want. So while a project is first mapped, the agent drafts and the owner decides. Once it's mapped, the agent changes the map as the project needs, except for what only the owner knows. That every change it makes is reported is fixed.

## Invariants

- **While a project is first mapped, the agent drafts and the owner decides.** Every question carries the agent's best answer as its default, and nothing the owner never saw is written into the map.
- The owner is asked only what only they know, or where two capable builders would choose differently and the owner would mind. Everything else is left open, and not asked.
- The layers are settled in order, intent, then primitives, capabilities and interfaces, and no layer is written before the owner agrees to it.
- An unresolved question stays out of the map and is reported. It's never settled by a guess.
- Before mapping is done, the whole map is read as a builder with nothing else would read it: every link resolves, every primitive is used, every capability is reached, every promise in the intent is kept, and nothing is built in.
- Mapping stops at the map. It never picks a stack, writes a plan or writes code.
- **Once mapped, the map changes without waiting for the owner, and never quietly.** Each change is listed in the report of the work so the owner can reverse it. The intent, and what's deliberately out or deferred, change only with the owner.
