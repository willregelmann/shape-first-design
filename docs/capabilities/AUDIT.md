# Audit

Shows whether a project's code keeps its map. For one change, it covers the invariants the change touches. Across a whole project, it gives every invariant a verdict.

Whether code keeps an invariant about behaviour, such as "the user is not nagged", takes judgment, so a judge decides each case from its evidence alone. That a judge's failure is never counted as a pass is fixed.

## Invariants

- **Every invariant it covers has a check named after it, which has been seen to fail.** A check that can't fail checks nothing.
- Each invariant gets the cheapest check that can actually fail, from a refusal built into the code up to a judged run of the real flow.
- **Behaviour that rests on judgment gets a judge.** The real flow runs several times, each run is judged from its evidence alone, and the result is a pass rate.
- A measurement that's only reported is not a check. It becomes one when crossing a threshold fails.
- **Results are reported as they are.** A failing check is never skipped or loosened to make work look done, and an invariant with no feasible check is reported as unchecked.
- Every verdict is one of: held and checked, held but unchecked, broken (with the case), can't tell (with what would settle it), or not built yet.
- It checks the shape as well as the rules: primitives with no home in the code, rules held outside their primitive, names that differ from the map's, types in the core for a case a primitive already covers, and two names for one primitive.
- It checks what agents are told as well as what the code does. A guide or a test can teach a broken rule.
- A whole-project audit changes nothing. It proposes fixes, and makes them only when asked.
