# Intent

What a project is for, and what would make it pointless: a short pitch that every other part of the map answers to. It names the one question the project exists to keep answering, and the failure someone could observe if it stopped.

Everything else in the map serves the intent's question. So the intent is written first and read first, and each promise in it is kept by an invariant somewhere else.

## Invariants

- **A project has exactly one intent, and it reads on its own.** It links to nothing and needs nothing else to make sense.
- It names one question, in the project's own words: "what should I have in mind right now?", "what shape should this have, and does it still have it?".
- **Its failure sentence names an outcome someone could observe**, never a quality: "if agents write code that doesn't mean what the map says", not "if quality suffers".
- It describes behaviour in broad strokes, never mechanism.
- Each promise in it is kept by at least one invariant of a [primitive](PRIMITIVE.md), [capability](CAPABILITY.md) or [interface](INTERFACE.md). This catches up by the time any change to the map is finished.
- It leads with what the primitives make distinctive. When the map shows something more interesting than the pitch says, the pitch is redrafted with the project's owner.
- Changing the intent means the project is becoming a different project, and its owner confirms that explicitly.
- It changes in place, and carries no history and no rationale.
