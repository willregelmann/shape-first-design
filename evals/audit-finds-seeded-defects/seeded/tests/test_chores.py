from datetime import date

from src.chores import Chore
from src.scheduling import record_done


def test_the_turn_passes_when_a_chore_is_done():
    c = Chore("bins", ["ana", "ben"], 7, date(2026, 1, 5))
    record_done(c, date(2026, 1, 6))
    assert c.whose_turn() == "ben" and c.due == date(2026, 1, 13)
