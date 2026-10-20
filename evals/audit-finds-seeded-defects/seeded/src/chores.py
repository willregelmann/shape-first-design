"""Chores and households (docs/primitives/CHORE.md, HOUSEHOLD.md)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Chore:
    name: str
    people: list[str]
    every_days: int
    due: date
    turn: int = 0
    history: list[tuple[str, date]] = field(default_factory=list)

    def whose_turn(self) -> str | None:
        return self.people[self.turn % len(self.people)] if self.people else None


@dataclass
class OneOffChore(Chore):
    """A chore that happens once."""

    finished: bool = False


@dataclass
class Household:
    people: list[str]
    chores: list[Chore] = field(default_factory=list)

    def leave(self, person: str) -> None:
        self.people.remove(person)
        for c in self.chores:
            c.history = [(who, on) for who, on in c.history if who != person]
            if person in c.people:
                had_turn = c.whose_turn() == person
                i = c.people.index(person)
                c.people.remove(person)
                if c.people and (i < c.turn or had_turn):
                    c.turn = c.turn % len(c.people) if had_turn else c.turn - 1


Family = Household
