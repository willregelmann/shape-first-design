# Once mapped, the map changes without waiting for the owner

## Context and Problem Statement

[Map](../capabilities/MAP.md) had the owner approve every change to the map, from the first interview to rewording one invariant years later, and [Develop](../capabilities/DEVELOP.md) stopped for the owner whenever a change touched the map. Every change cost the same, so small fixes waited and the map drifted from the code, which is the failure the method exists to prevent. Which changes to the map should wait for the owner?

## Considered Options

* Every change waits for the owner
* Changes after the first mapping don't wait, except to the intent and to what's deliberately out or deferred
* Nothing waits but a change to the intent
* Nothing waits for the owner at all

## Decision Outcome

Chosen option: "Changes after the first mapping don't wait, except to the intent and to what's deliberately out or deferred", chosen by the user, who asked to "drop the owner gate entirely" and then kept the calls only the owner can make with the owner.

* The first mapping is still an interview: the agent drafts and the owner decides.
* After that, the agent changes the map itself through Map, writes a record for each change as it's made, and lists every change in its report so the owner can reverse it.
* An invariant in the way, or code that fights the map, is settled by changing the map or the code, not by stopping for the owner.

### Consequences

* Good, because the map can keep up with the project, and a wrong change is visible and easy to reverse rather than prevented.
* Good, because the owner is still asked what only they know: what the project is for, and what's out of it.
* Bad, because an agent can now reshape the primitives between the owner's looks at the map, and the owner has to read the reports to catch a change they'd mind.

### Confirmation

[Map](../capabilities/MAP.md) states that once mapped, the map changes without waiting for the owner and never quietly. The `develop-routes-a-map-change` scenario checks that a change outside the map is mapped and recorded before it's built.

## More Information

Written on 2026-10-14.
