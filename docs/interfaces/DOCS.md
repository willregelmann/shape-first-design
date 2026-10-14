# Docs

Where a project's map lives, and where agents and people read it: the project's `docs/` folder, and a pointer to it in the instructions the project gives its agents. It's what [Map](../capabilities/MAP.md) writes, and what [Develop](../capabilities/DEVELOP.md) and [Audit](../capabilities/AUDIT.md) read.

## Layout

| Path | Holds |
|---|---|
| `docs/README.md` | How to read the map, the same in every project |
| `docs/INTENT.md` | The [intent](../primitives/INTENT.md) |
| `docs/primitives/<NOUN>.md` | One [primitive](../primitives/PRIMITIVE.md) each |
| `docs/capabilities/<VERB>.md` | One [capability](../primitives/CAPABILITY.md) each |
| `docs/interfaces/<SURFACE>.md` | One [interface](../primitives/INTERFACE.md) each |
| `docs/decisions/NNNN-title-with-dashes.md` | One [decision](../primitives/DECISION.md) each, in MADR's format, numbered in order. `0000` sets the conventions, and `adr-template.md` is where each record starts |
| `AGENTS.md` or `CLAUDE.md` | A pointer to the map |

## Invariants

- **Every project's map has the same layout**, so an agent that has read one map can find its way around any other.
- **The map can be read without the code.** Someone who never opens the code learns what's being built, and why it has this shape.
- The README, the `0000` record and the decision template are copied word for word and never edited per project. A copy that differs from its template is shown to the owner before it's replaced.
- Every map file is a short description followed by invariants, in plain everyday words.
- Every link between map files resolves.
- A project's agent instructions point at its map.
