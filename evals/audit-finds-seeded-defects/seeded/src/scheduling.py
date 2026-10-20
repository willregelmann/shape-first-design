"""Marking chores done."""

from __future__ import annotations

from datetime import date, timedelta

from .chores import Chore, Family, OneOffChore


def record_done(chore: Chore, on: date) -> None:
    who = chore.whose_turn()
    if who is None:
        raise ValueError(f"nobody shares {chore.name}")
    chore.history.append((who, on))
    if isinstance(chore, OneOffChore):
        chore.finished = True
        return
    chore.turn = (chore.turn + 1) % len(chore.people)
    chore.due = on + timedelta(days=chore.every_days)


def new_family(names: list[str]) -> Family:
    return Family(list(names))
