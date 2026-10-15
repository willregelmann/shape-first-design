# Shape-First Design asks "what shape should this have, and does it still have it?"

Superseded by ADR-0007.

## Context and Problem Statement

Every other choice in the method serves one question, and the question decides which choices matter. Two skills share it: one finds a project's shape with the person who has the idea, the other keeps every later change true to it. Which question should Shape-First Design exist to answer?

## Considered Options

* "What is this made of, and does the code still say so?"
* "What shape should this have, and does it still have it?"

## Decision Outcome

Chosen option: "What shape should this have, and does it still have it?", chosen by the user. TODO: record the reason.

* The first half is what map-project answers when a map is made or changed. The second half is what develop-project answers on every change and every audit.
* The failure sentence in [INTENT.md](../INTENT.md) makes it observable: code that doesn't mean what the map says, or a new kind of thing invented where one the map already names was the right fit.

### Consequences

* Good, because the question uses the word the method is named after.
* Bad, because "shape" is soft until someone reads what the map means by it: the few things a project is made of, chosen so its behaviour follows from them.

### Confirmation

[INTENT.md](../INTENT.md) states the question and the failure sentence.

## Pros and Cons of the Options

### "What is this made of, and does the code still say so?"

* Good, because it names the primitives and the code directly.
* Bad, because it doesn't use the method's own word.

## More Information

Written on 2026-10-14.
