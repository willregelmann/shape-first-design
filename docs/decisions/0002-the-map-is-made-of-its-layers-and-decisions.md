# The method is made of intents, primitives, capabilities, interfaces and decisions

## Context and Problem Statement

Shape-First Design has its own map, so it has to say what the method itself is made of. The first proposal had four primitives: a map holding all its layers, the invariants in it, the decisions that explain it, and the checks that keep it true. What are the method's primitives?

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

Chosen options: "No `Map`: each layer is a primitive of its own", "Invariants as part of the primitives, capabilities and interfaces that state them", and "Checking as a capability", chosen by the user.

* [Intent](../primitives/INTENT.md), [Primitive](../primitives/PRIMITIVE.md), [Capability](../primitives/CAPABILITY.md), [Interface](../primitives/INTERFACE.md) and [Decision](../primitives/DECISION.md) are the primitives.
* The tests every invariant meets are stated once, in Primitive, and Capability and Interface refer to them.
* Rules about the map as a whole, such as changing in place and carrying no history, are stated in each layer's primitive.

### Consequences

* Good, because each layer's very different rules have a home of their own, and no file has to hold all of them.
* Bad, because rules that hold for the whole map are repeated in each layer's file, and have to stay the same.
* TODO: record the reasons for leaving out `Map` and `Invariant`, and for making checking a capability.

### Confirmation

[Primitive](../primitives/PRIMITIVE.md) states the tests every invariant meets, and [Capability](../primitives/CAPABILITY.md) and [Interface](../primitives/INTERFACE.md) hold their invariants to the same tests. [Audit](../capabilities/AUDIT.md) is a capability.

## Pros and Cons of the Options

### One `Map` primitive

* Good, because it's the collapse the method teaches: the layers differ by position, not by kind.
* Bad, because one file would hold every layer's rules, past the size where a file is usually two things.

### A `Map` primitive plus one kind for the things in it

* Good, because it splits the whole from its parts.
* Bad, because the second primitive had no good name.

## More Information

Written on 2026-10-14.
