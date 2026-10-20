# Shape-First Design: Shared Rules

Both skills, `map-project` and `develop-project`, follow these rules. This file is their one source: a skill links here instead of restating a rule, so the two can't drift apart.

## Words

| Word | Means |
|---|---|
| **Project** | What gets mapped and built, new or already existing |
| **Owner** | The person whose project it is, and who decides what only they can know |
| **Shape** | The model a person holds of a project: the few things it's made of, each with one idea behind it |
| **Map** | The shape written down in a project's `docs/`: its intent, primitives, capabilities and interfaces |
| **Primitive** | A thing the project is made of. The core of the code takes its shape |
| **Capability** | A process across primitives that no one primitive owns |
| **Interface** | A surface where the outside touches the project |
| **Invariant** | A statement that holds at every moment, in every build |
| **Check** | Something that would notice an invariant breaking |
| **Audit** | Showing whether the code keeps the map, for one change or a whole project |

"User" means someone who uses the project, as in "the user is not nagged". It never means the owner.

## The Map

```
docs/
  README.md                    how to read the map, copied from templates/README.md
  INTENT.md                    what it's for
  primitives/<NOUN>.md         what it's made of, and how each thing behaves
  capabilities/<VERB>.md       what it does that no one thing does
  interfaces/<SURFACE>.md      where the outside touches it, and what crosses
```

`AGENTS.md`, or `CLAUDE.md` if the project uses that, points at the map. Every file except `INTENT.md` is a short description followed by invariants. Filenames are uppercase: a singular noun for a primitive, a verb for a capability, and the surface's common name for an interface.

| Layer | Answers | Named with | Examples |
|-------|---------|-----------|----------|
| Intent | What is this for? | The project's name | `INTENT.md` |
| Primitives | What is it made of, and how does each thing behave? | A singular noun | `MEMORY.md`, `DECK.md`, `QUESTION.md` |
| Capabilities | What does it do that no one thing does? | A verb | `CONSOLIDATE.md`, `RECALL.md`, `ANSWER.md` |
| Interfaces | Where does the outside touch it, and what crosses? | The surface's common name | `TOOLS.md`, `HOOKS.md`, `JOBS.md`, `API.md` |

**The primitives are the core of the code.** A build names its core after them, keeps their boundaries, and holds each primitive's invariants in that primitive. The abstractions are the design, and a build that dissolves them into services and helpers has lost it. Good code and an intuitive model go together: someone who has read the map can predict where each thing lives in the code and what it does, and code that's hard to explain from the map is usually a sign the map or the code has the wrong things in it. Everything around the core is the builder's call: storage, frameworks, protocols, layout, and where the rules of a capability or interface are enforced.

A primitive file still never reads as a list of fields, and a capability file never reads as a function signature. The map says what each thing is and what holds about it, not how it's stored or called.

## What Counts as an Invariant

An invariant is a statement about the project that is true at every moment, in every build of it. It passes four tests:

1. **Always.** It holds all the time, not at one step. If it describes a sequence, it's a procedure.
2. **Breakable.** A build could visibly violate it, and someone could point at the violation.
3. **Open.** Two quite different implementations could both satisfy it.
4. **Earned.** A capable builder working from the rest of the map could plausibly get it wrong without being told. What any sensible builder would do anyway is left out.

| Not an invariant | Why | Invariant |
|------------------|-----|-----------|
| "Memories are rows in a SQLite table" | Implementation | "A memory's content is never edited. When it turns out to be wrong, a new memory supersedes it." |
| "Listeners can ask questions" | Feature | "No question is dropped. Every question is answered, put off out loud, or declined out loud." |
| "Recall should be accurate" | Can't be broken visibly | "A memory that is only loosely related is labelled that way. It's never passed off as an answer." |
| "At most three questions a week" | A tuning number | "The user is not nagged. Questions to the user are strictly limited per conversation and per week." |
| "Load the slide, then start the audio" | Procedure | "What's seen and what's heard stay together." |
| "Errors are handled gracefully" | Any builder would say this | "Recall that fails says it failed. An agent is never shown 'nothing relevant' when the mind wasn't searched." |

**Naming a technology.** Name one only when the project must *meet* it: a runtime it has to live inside, a system it has to talk to, a format the owner insists on. Never name one the project is merely *built with*. The test: swap it out. If what's left is the same project built differently, it doesn't belong in the map.

**Across primitives.** An invariant that ties two or more primitives together says when it holds: at every moment, or restored after each change and by when. "A deck's slide count always matches its slides" and "a deck's slide count catches up before anyone next opens it" are different projects to someone watching. When the owner wouldn't mind which, write the one that catches up: it's the weaker promise, and a build that holds the stronger one keeps it too.

**Numbers.** State the limit, not its value. "Strictly limited per conversation" survives every build. A number is a tuning decision that a build makes and measures.

## Diagrams

Diagrams help a person who skims. Use them where they save reading, and nowhere else.

- **Mermaid only.** It renders on GitHub and in most editors, and it's text, so it diffs and reviews like the rest of the file.
- **A diagram follows the rules of the file it's in.** In the map it names no implementation: no tables, services or protocols. A relationship diagram of primitives never shows fields, for the same reason a primitive file never reads as a list of fields. In a plan or a README, implementation is fine.
- **It adds to the invariants and never replaces them.** An invariant can be broken and quoted; a box in a diagram can't. When the diagram and the text disagree, the text wins and the diagram is fixed.
- **Each layer has a natural shape:**

  | Layer | Diagram |
  |---|---|
  | Primitives | A lifecycle (state diagram), or how primitives relate (relationship diagram) |
  | Capabilities | A flow, or a decision |
  | Interfaces | A sequence: who calls what, in order |

- **One or two per file at most, and only where prose or a table is slower.** A short list doesn't need a picture.
- **A gradual change isn't a state.** Something that fades or drifts goes in a note, not a self-loop.
- **Relationship labels are a word or two:** "owns", "from", "to".
- **Render it before committing.** A diagram that doesn't parse is worse than none.

## Writing Style

For the map:

- Plain, everyday words. Describe the project the way you'd explain it to someone who will never see the code.
- Short declarative sentences in the present tense. "Never", "always", "only", "exactly one".
- One idea per bullet. Bold the few statements in each file the project would be a different project without, and no others.
- Concrete examples in quotes beat abstractions: "is your favorite color still pink?", "wait, why?".
- Use colons and commas for asides, not dashes.
- Files are short: a description and four to ten invariants. A file that keeps growing is usually two things, or a thing still missing its idea.
- No status, no dates, no rationale, no references to the conversation that wrote it.
