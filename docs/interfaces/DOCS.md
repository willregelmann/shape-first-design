# Docs

Where a project's [map](../primitives/MAP.md) lives, and where agents and people read it: the project's `docs/` folder, and a pointer to it in the instructions the project gives its agents. It's what [Map](../capabilities/MAP.md) writes, and what [Develop](../capabilities/DEVELOP.md) and [Audit](../capabilities/AUDIT.md) read.

## Layout

| Path | Holds |
|---|---|
| `docs/README.md` | How to read the map, the same in every project |
| `docs/INTENT.md` | The [intent](../primitives/INTENT.md) |
| `docs/primitives/<NOUN>.md` | One [primitive](../primitives/PRIMITIVE.md) each |
| `docs/capabilities/<VERB>.md` | One [capability](../primitives/CAPABILITY.md) each |
| `docs/interfaces/<SURFACE>.md` | One [interface](../primitives/INTERFACE.md) each |
| `AGENTS.md` or `CLAUDE.md` | A pointer to the map |

## Invariants

- **Every project's map has the same layout**, so an agent that has read one map can find its way around any other.
- The README is copied word for word and never edited per project. A copy that differs from its template is shown to the owner before it's replaced.
- Every map file except the intent is a short description followed by invariants, in plain everyday words. The intent is a short pitch.
- Every link between map files resolves.
- A diagram in the map is Mermaid, names no implementation, and never replaces an invariant. When a diagram and the text disagree, the text wins.
- A project's agent instructions point at its map.
