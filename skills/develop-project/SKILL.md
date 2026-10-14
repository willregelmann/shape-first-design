---
name: develop-project
description: Develops a project that has a map under docs/ (INTENT.md, primitives, capabilities, interfaces and decisions), whether it's the first build or a feature, fix or refactor years later, keeping the core of the code in the primitives' shape and checking that the code keeps the invariants — use for any work in a repository with docs/INTENT.md and docs/primitives/, or when the user says "build this from the map", "check the invariants", "does the code still match the map", or "backfill the decisions". Records architecture decisions as MADR records. Changes to the model itself go through map-project.
tags:
  - invariants
  - development
  - architecture
  - testing
---

# Develop Project

Do a piece of work in a project that has a map: the first build, a feature, a fix or a refactor. The map in `docs/` says what the product is and what must always hold. This skill keeps the code and the map true to each other while the work gets done.

Capable models write excellent code but drift from structure, one reasonable change at a time. The map fixes the core abstractions. This skill keeps every change inside them, and makes drift visible the moment it happens rather than months later.

Each piece of work delivers:

- **the change itself**, with the core of the code in the primitives' shape;
- **a check for every invariant the change touches**, named after the invariant and shown to fail when it's broken;
- **a decision record** for each architecture decision the change makes, in `docs/decisions/`;
- **the map, changed through `map-project`**, when the work changed what the product is.

## Quick Reference

| Step | Job | Output |
|------|-----|--------|
| 1 | Read | The intent, the map files the work touches, and the records that explain them |
| 2 | Place the change | A few lines: which primitives, capabilities and surfaces, which invariants, and whether the model changes |
| 3 | Build | Code whose core is named and bounded by the primitives |
| 4 | Check | A failing-when-broken check for each touched invariant, run and reported |
| 5 | Record | MADR records for the architecture decisions the work made |
| 6 | Reconcile | Code, map, records and plans agree, in the same change |
| 7 | Report | What changed, invariant by invariant |

To check a whole project against its map rather than make a change, go to [Auditing](#auditing). To write records for a project's past decisions, go to [Backfilling Decisions](#backfilling-decisions).

## Process

### 1. Read

Read `docs/README.md` and `docs/INTENT.md`. Then read every map file the work touches: the primitives it changes or relies on, the capabilities it runs inside, the surfaces it's reached through. Then read the records in `docs/decisions/` that link to those files. For a first build, read the whole map and every record.

- **No map?** Stop. Say so, and offer `map-project`. Don't sketch a map inline to get going: a map made in passing has none of the decisions that make one worth having.
- **The map looks incomplete** (a missing README or decision templates, a capability nothing reaches)? Note it in the report. Fixing the map is `map-project`'s job.
- Where the map says nothing, the choice is yours. Don't treat silence as a constraint, and don't fill it with invariants of your own.

### 2. Place the Change

Before writing code, write down in a few lines: which primitives the work touches, which capability or surface it runs through, and which invariants are in play. Bold invariants first.

Then decide whether the work changes the model:

- **It changes the model** when it adds, removes, merges or splits a primitive, changes what an invariant says, adds or folds a capability, or adds or changes a surface. Stop and take it through `map-project`'s "Changing the Map" with the user. Continue once the map says the new thing.
- **It doesn't** when it makes the code do what the map already says, or chooses how something is built where the map is silent. A bug fix that makes the code keep an invariant is not a model change. A fix that changes what holds is.
- **A name is a signal.** If the core of the code needs a word the map doesn't have, the map is probably missing a primitive. Treat it as a model change until the user says otherwise.
- **An invariant in the way** is raised with the user, never worked around. There are two honest ways through: change the map, or find another way to build it. A quiet exception is not one of them.

### 3. Build

**The core of the code takes the primitives' shape.** Name its central types or modules after the primitives, keep their boundaries, and hold each primitive's invariants inside it: in its constructors and methods, in the store's own constraints, wherever the primitive lives. The names in the code are the map's names. A synonym in the code is the first step of drift.

- **Capabilities** are processes across primitives. They can be functions, services or jobs. They call the primitives' rules and never re-implement them.
- **Surfaces** translate. An adapter for a tool, a hook, an endpoint or a screen maps the outside onto the core and holds no rules of its own. A behaviour that differs by host or client is a bug.
- **Judgment** sits where the map says it does. Where a person or a model decides, the guarantee the map places beside the decision is enforced in code whatever the decision is.
- **Failure is visible.** Where the map says what happens when something can't do its job, build exactly that. Never a silent fallback.
- **Everything around the core is the builder's call:** stack, storage, protocols, layout. Make those choices well, and record the ones that are patterns or boundaries (Step 5).

Point from the code to the map where an invariant is enforced, for example a docstring naming `docs/primitives/MEMORY.md`. Never copy the map's reasoning into comments. The map says what, and the records say why.

### 4. Check

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

### 5. Record

When the work settles an architecture decision, write a record in `docs/decisions/` before the change is done. Follow the project's `0000` record. If `docs/decisions/` doesn't exist, copy [map-project's decision templates](../map-project/templates/decisions/) there first.

- **Record a pattern or a boundary, not a setting.** How data is stored, how processes are split, how a surface is served, which dependency the core relies on: records. A timeout, a threshold or a class name: not records. The test: if changing it leaves the record true, it isn't one.
- **Only what was weighed.** List the options actually considered, the reasons in the user's words where they gave them, and `TODO` where a reason is unknown.
- **Confirmation names the checks** that keep the decision true, and the map files it serves.
- **Reversing a recorded decision** takes a new record that supersedes the old one, and a `Superseded by ADR-NNNN.` line under the old record's title. Nothing else in an accepted record changes.
- A decision about what the product is, rather than how it's built, belongs to `map-project`.

### 6. Reconcile

Before finishing, make the code, the map, the records and any plan agree, in the same change:

- **Map changes** went through `map-project` (Step 2), and no map file names an implementation.
- **Records** for this work are written, and any decision this work reverses is superseded.
- **Plans** (`PLAN.md` or whatever the project uses) say how the code is now built. A plan may name technologies and carry architecture diagrams. It holds no reasoning that belongs in a record.
- **Diagrams** follow the rules of the file they're in. In the map, no implementation. In a plan or README, implementation is fine.

### 7. Report

Report the change in a few sentences, then, invariant by invariant, what was touched and how it's checked:

| Invariant | Map file | Check | Result |
|---|---|---|---|

Results are **passes**, **fails** (with output), or **unchecked** (with why). Then list the records written or superseded, any change made to the map, anything raised with the user, and anything in the map that looked wrong.

## Auditing

When asked whether the code still matches the map, check the whole project without changing it.

1. Read the whole map and every record.
2. For each invariant, bold ones first, find where the code holds it and which check covers it.
3. Give each one a verdict:

   | Verdict | Means |
   |---|---|
   | **Held and checked** | The code holds it, and a check fails when it's broken |
   | **Held, unchecked** | The code appears to hold it, and nothing would notice if it stopped |
   | **Broken** | The code violates it. Say where, with the specific case |
   | **Can't tell** | The code is too unclear to judge. Say what would settle it |

4. Check the core's shape: primitives with no home in the code, primitive rules held outside their primitive, and names in the code that differ from the map's.
5. Check the records: each record's Confirmation still holds, and no decision visible in the code contradicts a record without superseding it.
6. Report the verdict table and the shape findings, worst first. Propose fixes, and make them only when asked.

## Backfilling Decisions

When a project's decisions are written down somewhere other than records, in a plan, commit messages, research notes or a conversation, backfill them on request.

1. Copy the decision templates if `docs/decisions/` doesn't exist.
2. Gather candidates from every source. Keep the decisions that still stand. A reversed decision becomes a rejected option inside the record that replaced it, not a record of its own.
3. Keep to the altitude: patterns and boundaries, never settings.
4. Number records in the order the decisions were made, except where the user names a foundation to come first.
5. Draft every record from its sources. List only options the sources show were weighed, and mark every unknown reason `TODO`. End each with "Written on <date>, after the fact."
6. Ask the user about all the `TODO`s in one round. "I don't remember" is an answer, and the `TODO` stays.
7. Move the reasoning out of the plan into the records, in a separate commit, so the plan keeps only how and in what order.

## Common Mistakes

- **Rules outside their primitive.** A service or helper that checks a primitive's invariants leaves the primitive as bare data, and the next caller skips the check. Move the rule into the primitive.
- **Synonyms in the code.** Calling a memory a "record" or a namespace a "scope" in the code splits the vocabulary, and the map stops describing the code.
- **Editing the map mid-feature.** Changing a map file to make the code fit skips the user, the decision record and the walk. Route it through `map-project`.
- **A quiet exception.** Loosening an invariant in code, skipping its check, or marking it expected to fail. Raise it instead.
- **Checks named after functions.** `test_update_raises` says nothing when it fails. Name the promise.
- **A check that can't fail.** A test that passes whatever the code does. Break the code once to prove it.
- **Counting a judge's error as a pass.** A judged scenario that couldn't judge has no verdict.
- **Treating the map's silence as a rule.** Where the map says nothing, decide, and record it if it's a pattern or boundary. Don't invent invariants.
- **Recording a setting.** A record about a value goes stale the first time someone tunes it.
- **Editing a record.** Reversing a decision in place erases why it was made. Supersede it.
- **Building a deferred capability.** A capability marked deferred has guardrails, not a go-ahead. Ask first.
- **Sketching a map to get started.** Without a map, the work belongs to `map-project` first.

## Key Principles

- **The map leads, and the code follows.** When the two disagree, the code changes or the map changes through `map-project`. Never the code alone, quietly.
- **The core keeps the primitives' shape.** Same names, same boundaries, rules held where they belong. Everything around it is the builder's call.
- **An invariant without a check is a hope.** Every invariant touched gets a check that names it and has been seen to fail.
- **Judgment gets a judge.** Deterministic rules get deterministic tests. Behaviour that rests on judgment gets judged scenarios with pass rates.
- **What, why and how live apart.** The map says what holds, records say why, plans and code say how, and all of them change together.
- **Failure is visible.** Failing checks, unchecked invariants and broken promises are reported, never smoothed over.
