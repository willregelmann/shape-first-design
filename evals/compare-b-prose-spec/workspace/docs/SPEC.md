# Chores: requirements

## Overview

A chore tracker for a shared household of four, so nobody has to remember whose turn it is. A command-line tool tells the household whose turn it is for each chore, and reminds that person when it's due. If a chore comes due and the person whose turn it is wasn't told, the tool has failed.

## Requirements

### Chores

- A chore has a name, the people who share it, and when it is next due.
- A chore either repeats on a schedule or happens once, like "clean the gutters before the party on the 20th".
- Exactly one person has the turn for a chore at any moment.
- When a chore is done, the turn passes to the next person in order.
- A repeating chore's next due date follows from when it was due, not from when it was done.
- A one-off chore, once done, is never due again and is never reminded again. Its history is kept.
- A chore that nobody shares has no turn, and is never reminded.
- The history of who did a chore and when is only ever added to.

### Household

- A household is the people who live together and share chores.
- Every chore belongs to exactly one household, and only people in that household take its turns.
- When someone leaves the household, they are taken out of every chore's turns, and each chore they had the turn for passes to the next person.

### Reminders

- Whoever has the turn when a chore comes due is reminded exactly once for that due time.
- A reminder that can't be delivered says so, and is tried again.

### Command line

| Command | Does |
|---|---|
| `add` | Adds a chore with the people who share it and how often it's due |
| `done` | Marks a chore done, and passes the turn |
| `due` | Lists what's due, and whose turn it is |

- Every command says what it changed, or that it changed nothing.
