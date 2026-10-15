# Develop

Builds or changes a project's code by its map: the first build, a feature, a fix or a refactor, in a new project or an old one.

How the code is built is the builder's call wherever the map says nothing. That the core keeps the shape of the [primitives](../primitives/PRIMITIVE.md) is fixed.

## Invariants

- **Every change is placed against the map before it's written**: which primitives, capabilities and interfaces it touches, and which invariants are in play.
- **A change to what the project is goes through [Map](MAP.md) first.** Adding, splitting or merging a primitive, changing an invariant, or adding a capability or surface never happens in the code alone. It doesn't wait for the owner unless it touches the intent or what's deliberately out or deferred.
- **Code that fights the map is evidence about the map.** A word the code needs that the map doesn't have, a special case or flag for one kind of thing, or a rule that won't sit inside its primitive is treated as a possible flaw in the map: the map or the code is fixed, and the report says which. It's never smoothed over in the code alone.
- An invariant in the way is never worked around. The map changes, or the code finds another way, and a quiet exception is never one of the ways through.
- Where the map says nothing, the builder decides, and records a [decision](../primitives/DECISION.md) when the choice is a pattern or a boundary.
- Every change is [audited](AUDIT.md) against the invariants it touches before it's done.
- The map, the decisions and the code change together, in the same change.
- A project without a map isn't developed by this method until it's mapped.
- A deferred capability is never built without asking the owner.
