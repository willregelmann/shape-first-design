# Intent

What a project is for: a short pitch that every other part of the map answers to. It says what the project is, what sets it apart, and the idea it's built on.

Everything else in the map serves the intent's focus. So the intent is written first and read first, and each promise in it is kept by an invariant somewhere else.

## Invariants

- **A project has exactly one intent, and it reads on its own.** It links to nothing and needs nothing else to make sense.
- It says what the project is for and what sets it apart, in the project's own words.
- When it names a focus, a question it keeps answering or a promise it keeps, or a failure that would make it pointless, the failure is an outcome someone could observe, never a quality: "if agents write code that doesn't mean what the map says", not "if quality suffers".
- It describes behaviour in broad strokes, never mechanism.
- Each promise in it is kept by at least one invariant of a [primitive](PRIMITIVE.md), [capability](CAPABILITY.md) or [interface](INTERFACE.md). This catches up by the time any change to the map is finished.
- It leads with what the primitives make distinctive. When the map shows something more interesting than the pitch says, the pitch is redrafted with the project's owner.
- Changing the intent means the project is becoming a different project, and its owner confirms that explicitly.
