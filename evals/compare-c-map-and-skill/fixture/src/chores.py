"""Chores and households (docs/primitives/CHORE.md, HOUSEHOLD.md)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta


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

    def done(self, on: date) -> None:
        who = self.whose_turn()
        if who is None:
            raise ValueError(f"nobody shares {self.name}")
        self.history.append((who, on))
        self.turn = (self.turn + 1) % len(self.people)
        self.due = self.due + timedelta(days=self.every_days)


@dataclass
class Household:
    people: list[str]
    chores: list[Chore] = field(default_factory=list)

    def leave(self, person: str) -> None:
        self.people.remove(person)
        for c in self.chores:
            if person in c.people:
                had_turn = c.whose_turn() == person
                i = c.people.index(person)
                c.people.remove(person)
                if c.people and (i < c.turn or had_turn):
                    c.turn = c.turn % len(c.people) if had_turn else c.turn - 1
