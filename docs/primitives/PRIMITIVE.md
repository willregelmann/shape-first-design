# Primitive

A thing a project is made of, which would exist in any implementation of it. You'd need the word to explain the project to someone. Its file says what the thing is and what always holds about it.

The primitives are the core of the code. Everything about a thing, how it comes to exist, how it changes, how it ends and what it never does, lives in its primitive, so code that takes their shape gets its structure from them.

Deciding what a project is made of takes judgment, so the agent drafts and the project's owner decides. That every primitive meets the same tests is fixed.

## Invariants

- **The core of the code takes the primitives' shape.** The same names, the same boundaries, and each primitive's rules held inside it. Everything around the core is the builder's choice.
- **Things that differ only in how they came to be or how they're connected are one primitive.** An observation and a belief are both memories. A new primitive is never added where an existing one fits.
- One word that means different things in different parts of a project is two primitives. Each is named, and each says how it relates to the other.
- A primitive is a thing, never a view of one, a field of one, a storage structure, a screen or a person.
- A primitive's rules follow from one idea about it, and stay few. One that needs a long list of unrelated rules is the wrong abstraction.
- **Every invariant holds at every moment in every build, could visibly break, leaves room for different implementations, and is one a capable builder could plausibly get wrong without being told.**
- An invariant that ties primitives together says whether it holds at every moment or catches up, and by when.
- An invariant states a limit, never its value, and names a technology only when the project must meet it.
- It changes in place, and carries no history and no rationale.
