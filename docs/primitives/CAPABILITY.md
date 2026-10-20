# Capability

A process a project carries out across several [primitives](PRIMITIVE.md), which isn't the natural job of any one of them. It's named with a verb. Most behaviour lives in the primitives, so a project has few capabilities.

Where a person or a model decides something inside a capability, its file names who decides, and then what holds whatever they decide.

## Invariants

- **A capability spans primitives.** One whose rules are all about one primitive is part of that primitive, and has no file of its own.
- **Wherever judgment sits, a guarantee sits beside it.** "The agent decides when to ask" is always followed by what is fixed whatever the agent decides.
- It relies on the primitives' [invariants](INVARIANT.md) and never restates them differently.
- It says what happens when it can't do its job, and never fails silently.
- Every capability is started and observed through at least one [interface](INTERFACE.md).
- A deferred capability records only the guardrails already settled, and nothing is built for it until it's no longer deferred.
