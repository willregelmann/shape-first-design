# Invariant is a primitive of its own

## Context and Problem Statement

[0002](0002-the-map-is-made-of-its-layers-and-decisions.md) made the method's primitives Intent, Primitive, Capability, Interface and Decision, and left out `Map`, `Invariant` and `Check`, with the reasons marked TODO. A review found that "invariant" is the word anyone would most need to explain the method, which is the method's own test for a primitive, and that [Primitive](../primitives/PRIMITIVE.md) held two ideas: what a thing is, and the tests every invariant meets. What are the method's primitives?

## Considered Options

The map:

* One `Map` primitive, with the rules for each layer inside it
* A `Map` primitive plus one kind for the things in it, with rules per layer
* No `Map`: each layer is a primitive of its own (intent, primitive, capability, interface)

Invariants:

* `Invariant` as a primitive of its own
* Invariants as part of the primitives, capabilities and interfaces that state them

Checks:

* `Check` as a primitive
* Checking as a capability

## Decision Outcome

Chosen options: "No `Map`", because one file would hold every layer's rules; "`Invariant` as a primitive of its own", because it's the word you'd need to explain the method and Primitive had two ideas in it; and "Checking as a capability", because checking is something done across primitives, not a thing a project is made of. Chosen by the user.

* [Intent](../primitives/INTENT.md), [Primitive](../primitives/PRIMITIVE.md), [Invariant](../primitives/INVARIANT.md), [Capability](../primitives/CAPABILITY.md), [Interface](../primitives/INTERFACE.md) and [Decision](../primitives/DECISION.md) are the primitives.
* The tests every invariant meets, timing across primitives, and limits rather than values are stated once, in Invariant.
* Rules about the map as a whole, such as changing in place and carrying no history, are still stated in each layer's primitive.

This supersedes 0002, keeping its choices about `Map` and checking and reversing its choice about `Invariant`.

### Consequences

* Good, because each primitive's rules follow from one idea: Primitive says what a thing is, Invariant says what a promise about it is.
* Good, because the method's central word has a file someone can read.
* Bad, because rules that hold for the whole map are still repeated in each layer's file, and have to stay the same.

### Confirmation

[Invariant](../primitives/INVARIANT.md) states the tests every invariant meets, and no other map file restates them. [Audit](../capabilities/AUDIT.md) is a capability.

## Pros and Cons of the Options

### One `Map` primitive

* Good, because it's the collapse the method teaches: the layers differ by position, not by kind.
* Bad, because one file would hold every layer's rules, past the size where a file is usually two things.

### A `Map` primitive plus one kind for the things in it

* Good, because it splits the whole from its parts.
* Bad, because the second primitive had no good name.

### Invariants as part of the files that state them

* Good, because there's one fewer primitive.
* Bad, because the tests every invariant meets had to live in Primitive, and Capability and Interface had to point there.

## More Information

Written on 2026-10-14.
