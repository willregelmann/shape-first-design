---
type: llm
---
docs/capabilities/AUDIT.md: the audit checks what agents are told as well as what the code does, because a test can teach a broken rule. Pass if the reply reports that the one test, test_the_turn_passes_when_a_chore_is_done, asserts a due date of 13 January for a chore due on 5 January and done on 6 January, which is the broken behaviour and not the 12 January the map requires, so the passing test is no evidence the invariant holds. Fail if it counts that test as a check that the due-date invariant is held, or doesn't mention it.
