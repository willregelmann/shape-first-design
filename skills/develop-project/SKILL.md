---
name: develop-project
description: Develops a project that has a map under docs/ (INTENT.md, primitives, capabilities and interfaces), whether it's the first build or a feature, fix or refactor years later, keeping the core of the code in the primitives' shape and checking that the code keeps the invariants — use for any work in a repository with docs/INTENT.md and docs/primitives/, or when someone says "build this from the map", "check the invariants", "does the code still match the map". Changes to what the project is go through map-project.
tags:
  - invariants
  - development
  - architecture
  - testing
---

# Develop Project

Do a piece of work in a project that has a map: the first build, a feature, a fix or a refactor. The map in `docs/` says what the project is and what must always hold. This skill keeps the code and the map true to each other while the work gets done.

Capable models write excellent code but drift from structure, one reasonable change at a time. Good code and an intuitive model go together, so the map fixes the model: the core abstractions, in words a person can hold. This skill keeps every change inside them, so someone who has read the map can still predict the code, and makes drift visible the moment it happens rather than months later. When the code fights the map, that's evidence about the map too.

**Read [the shared rules](#shared-rules) first.** They're at the end of this file: the words, the map's layout and layers, what counts as an invariant, the writing style, and the templates. They come from one source shared by both skills.

Each piece of work delivers:

- **the change itself**, with the core of the code in the primitives' shape;
- **a check for every invariant the change touches**, named after the invariant and shown to fail when it's broken;
- **the map, changed through `map-project`**, when the work changed what the project is.

## Quick Reference

| Step | Job | Output |
|------|-----|--------|
| 1 | Read | The intent and the map files the work touches |
| 2 | Place the change | A few lines: which primitives, capabilities and surfaces, which invariants, and whether the map changes |
| 3 | Build | Code whose core is named and bounded by the primitives |
| 4 | Audit | A failing-when-broken check for each touched invariant, run and reported |
| 5 | Reconcile | Code, map and plans agree, in the same change |
| 6 | Report | What changed, invariant by invariant |

To audit a whole project against its map rather than make a change, go to [Auditing a Project](#auditing-a-project).

## Process

### 1. Read

Read `docs/README.md` and `docs/INTENT.md`. Then read every map file the work touches: the primitives it changes or relies on, the capabilities it runs inside, the surfaces it's reached through. For a first build, read the whole map.

- **No map?** Stop. Say so, and offer `map-project`. Don't sketch a map inline to get going: a map made in passing hasn't been agreed with the owner.
- **The map looks incomplete** (a missing README, a capability nothing reaches)? Note it in the report. Fixing the map is `map-project`'s job.
- Where the map says nothing, the choice is yours. Don't treat silence as a constraint, and don't fill it with invariants of your own.

### 2. Place the Change

Before writing code, write down in a few lines: which primitives the work touches, which capability or surface it runs through, and which invariants are in play. Bold invariants first.

Then decide whether the work changes the map:

- **It changes the map** when it adds, removes, merges or splits a primitive, changes what an invariant says, adds or folds a capability, or adds or changes a surface. Take it through `map-project`'s "Changing the Map", and continue once the map says the new thing. It doesn't wait for the owner unless it touches the intent or what's deliberately out or deferred.
- **It doesn't** when it makes the code do what the map already says, or chooses how something is built where the map is silent. A bug fix that makes the code keep an invariant is not a map change. A fix that changes what holds is.
- **A name is a signal.** If the core of the code needs a word the map doesn't have, the map is probably missing a primitive. Treat it as a map change.
- **An invariant in the way** is never worked around. There are two honest ways through: change the map through `map-project`, or find another way to build it. A quiet exception is not one of them.

### 3. Build

**The core of the code takes the primitives' shape.** Name its central types or modules after the primitives, keep their boundaries, and hold each primitive's invariants inside it: in its constructors and methods, in the store's own constraints, wherever the primitive lives. The names in the code are the map's names. A synonym in the code is the first step of drift. **Nothing joins the core that the map doesn't name:** before adding a type, a name or a rule to the core, find the primitive it belongs to. If one fits, extend it. If none does, the map changes first.

- **Capabilities** are processes across primitives. They can be functions, services or jobs. They call the primitives' rules and never re-implement them.
- **Surfaces** translate. An adapter for a tool, a hook, an endpoint or a screen maps the outside onto the core and holds no rules of its own. A behaviour that differs by host or client is a bug.
- **Judgment** sits where the map says it does. Where a person or a model decides, the guarantee the map places beside the decision is enforced in code whatever the decision is.
- **Failure is visible.** Where the map says what happens when something can't do its job, build exactly that. Never a silent fallback.
- **When the code fights the map, suspect the map.** A special case or flag for one kind of thing, a rule that keeps wanting to live outside its primitive, a name that won't fit, or a change that needs edits in many places for one idea: each is a sign that the map has the wrong things in it, or the code has drifted from it. Say which, with the case. Fix a map flaw through `map-project`, and fix drifted code in the code. Don't smooth it over.
- **Everything around the core is the builder's call:** stack, storage, protocols, layout. Make those choices well.

Point from the code to the map where an invariant is enforced, for example a docstring naming `docs/primitives/MEMORY.md`. Never copy the map's reasoning into comments.

### 4. Audit

**Every invariant the change touches has a check that fails when the invariant is broken.**

- **Name each check after its invariant**, and point to the map file it comes from, so a failure says which promise broke: `test_memory_content_is_never_edited`, not `test_update_raises`.
- **Use the cheapest check that can actually fail:**

  | Kind of invariant | Check |
  |---|---|
  | Something the code or store can refuse outright ("content is never edited") | Enforce it by construction, then test that the refusal happens |
  | A rule about one primitive or one capability | A unit or property test against it |
  | A rule across a surface ("the same in every host") | A contract test through each real host, client or surface |
  | A quality held across many cases ("a loose fit is labelled loose", "nothing leaks from an unsearched namespace") | A measurement over fixtures, with a threshold that fails the build |
  | Behaviour that rests on judgment ("the user is not nagged", "reconfirms when it should") | A judged scenario: run the real agent or flow several times, have an isolated judge decide each run from the evidence alone, and report pass rates. A judge that errors is reported as an error, never as a pass |

- **Break it to prove it.** For each new check, break the code it guards and watch the check fail, then restore it. A check that can't fail checks nothing.
- **Timing and limits.** An invariant that catches up is checked at its deadline, not at every moment. An invariant that states a limit ("strictly limited per week") is checked for the limit, whatever value the build chose.
- **Run every check for the primitives the change touches**, not just the new ones. Report failures with their output. A failing check is never skipped, loosened or marked expected to make the work look done.
- **An invariant with no feasible check** is listed as unchecked in the report, with why. Never imply it's covered.

### 5. Reconcile

Before finishing, make the code, the map and any plan agree, in the same change:

- **Map changes** went through `map-project` (Step 2), and no map file names an implementation.
- **Plans** (`PLAN.md` or whatever the project uses) say how the code is now built. A plan may name technologies and carry architecture diagrams.
- **Diagrams** follow [the shared rules for diagrams](#diagrams): in the map, no implementation; in a plan or README, implementation is fine.

### 6. Report

Report the change in a few sentences, then, invariant by invariant, what was touched and how it's checked:

| Invariant | Map file | Check | Result |
|---|---|---|---|

Results are **passes**, **fails** (with output), or **unchecked** (with why). Then list every change made to the map, so the owner can reverse it, anything that needs the owner (the intent, or what's out or deferred), and anything in the map that looked wrong.

## Auditing a Project

When asked whether the code still matches the map, audit the whole project without changing it. A large map can be split by area across several agents, each auditing its part with the same verdicts.

1. Read the whole map.
2. For each invariant, bold ones first, find where the code holds it and which check covers it.
3. Give each one a verdict:

   | Verdict | Means |
   |---|---|
   | **Held and checked** | The code holds it, and a check fails when it's broken |
   | **Held, unchecked** | The code appears to hold it, and nothing would notice if it stopped |
   | **Broken** | The code violates it. Say where, with the specific case |
   | **Can't tell** | The code is too unclear to judge. Say what would settle it |
   | **Not built yet** | What it depends on doesn't exist yet. Say what's missing |

   A measurement that's only reported is not a check, and neither is a scenario whose pass rate fails nothing. A check counts only if crossing its threshold fails the build.
4. **Prove the important checks can fail.** For the bold invariants, break the guarding code in a copy of the project, never the project itself, and watch the check fail. Report which checks were proven this way.
5. **Audit what agents are told, not just what the code does.** Guides, prompts, skills and agent instructions can teach a rule the map doesn't hold, and a test can assert a broken behaviour. Both are findings, and neither is proof the code is right.
6. Check the core's shape: primitives with no home in the code, primitive rules held outside their primitive, names in the code that differ from the map's, and types in the core for a case a primitive already covers.
7. Report the verdict table and the shape findings, worst first, and anything in the map itself that looked wrong or can't be tested as written. Propose fixes, and make them only when asked.

## Common Mistakes

- **Rules outside their primitive.** A service or helper that checks a primitive's invariants leaves the primitive as bare data, and the next caller skips the check. Move the rule into the primitive.
- **A new type for a case a primitive covers.** A second type beside the one the map names splits one idea in two, and every rule has to be kept in both. Extend the primitive.
- **Synonyms in the code.** Calling a memory a "record" or a namespace a "scope" in the code splits the vocabulary, and the map stops describing the code.
- **Editing the map mid-feature.** Changing a map file to make the code fit skips the walk. Route it through `map-project`.
- **Forcing the code to fit.** Special cases and flags that make awkward code pass leave the map describing a project the code isn't. Awkward code is evidence: act on it, out loud.
- **A quiet exception.** Loosening an invariant in code, skipping its check, or marking it expected to fail. Raise it instead.
- **Checks named after functions.** `test_update_raises` says nothing when it fails. Name the promise.
- **A check that can't fail.** A test that passes whatever the code does. Break the code once to prove it.
- **Counting a judge's error as a pass.** A judged scenario that couldn't judge has no verdict.
- **Counting a reported number as a check.** A metric nobody fails the build on will drift unnoticed.
- **Trusting the tests and the guide.** A test can assert the broken behaviour, and a guide can teach it. Audit them against the map like the code.
- **Treating the map's silence as a rule.** Where the map says nothing, decide. Don't invent invariants.
- **Building a deferred capability.** A capability marked deferred has guardrails, not a go-ahead. Ask first.
- **Sketching a map to get started.** Without a map, the work belongs to `map-project` first.

## Key Principles

- **The map leads, and the code follows.** When the two disagree, the code changes or the map changes through `map-project`. Never the code alone, quietly. Code that's hard to write from the map is a reason to look at the map.
- **The core keeps the primitives' shape.** Same names, same boundaries, rules held where they belong. Everything around it is the builder's call.
- **An invariant without a check is a hope.** Every invariant touched gets a check that names it and has been seen to fail.
- **Judgment gets a judge.** Deterministic rules get deterministic tests. Behaviour that rests on judgment gets judged scenarios with pass rates.
- **What and how live apart.** The map says what holds, plans and code say how, and all of them change together.
- **Failure is visible.** Failing checks, unchecked invariants and broken promises are reported, never smoothed over.

<!-- shared:start (generated from skills/shared/ by checks/sync_shared.py; edit there) -->

## Shared Rules

These rules come from `skills/shared/RULES.md`, the one source both skills share.

Both skills, `map-project` and `develop-project`, follow these rules. This file is their one source: a skill links here instead of restating a rule, so the two can't drift apart.

### Words

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

### The Map

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

### What Counts as an Invariant

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

### Diagrams

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

### Writing Style

For the map:

- Plain, everyday words. Describe the project the way you'd explain it to someone who will never see the code.
- Short declarative sentences in the present tense. "Never", "always", "only", "exactly one".
- One idea per bullet. Bold the few statements in each file the project would be a different project without, and no others.
- Concrete examples in quotes beat abstractions: "is your favorite color still pink?", "wait, why?".
- Use colons and commas for asides, not dashes.
- Files are short: a description and four to ten invariants. A file that keeps growing is usually two things, or a thing still missing its idea.
- No status, no dates, no rationale, no references to the conversation that wrote it.

## Templates

Copy these into a project word for word, at the path each one names.

### `docs/README.md`

````markdown
# The Map

These files are the map of the project. Apart from the intent, each is a short description followed by statements that hold in every build of it.

- [INTENT.md](INTENT.md): what it's for. Read it first.
- `primitives/`: what it's made of, and how each thing behaves.
- `capabilities/`: what it does that no one thing does.
- `interfaces/`: where the outside touches it, and what crosses.

## Reading the Map

- **The primitives are the core of the code.** Name the core after them, keep their boundaries, and hold each primitive's rules in that primitive. Everything around the core is the builder's choice.
- Where the map says nothing, the choice is the builder's.
- Bold statements are the ones the project would be a different project without.
- An invariant that says it catches up may be held sooner, never later.
- A build that can't keep an invariant changes the map, or finds another way. It never becomes a quiet exception.
- When the project changes, these files change in place.
````

<!-- shared:end -->
