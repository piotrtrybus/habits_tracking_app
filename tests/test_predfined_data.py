import json
import unittest
from pathlib import Path
from habits.habit_schema import Habit

FIXTURE = Path("habits.json")

@unittest.skipUnless(FIXTURE.exists(), "habits.json not found at repo root")
class TestPredefinedFixture(unittest.TestCase):
    def test_fixture_loads_and_has_both_periodicities(self):
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data), 5, "Need at least 5 predefined habits")
        dailies = any(h["periodicity"] == "daily" for h in data)
        weeklies = any(h["periodicity"] == "weekly" for h in data)
        self.assertTrue(dailies and weeklies, "Include both daily and weekly habits")

        if Habit:
            habits = [Habit.from_dict(h) for h in data]
            self.assertTrue(all(isinstance(h, Habit) for h in habits))


