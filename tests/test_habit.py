import unittest
from habits.habit_schema import Habit

class TestHabit(unittest.TestCase):
    def test_creation(self):
        h = Habit("Test", "daily")
        self.assertEqual(h.name, "Test")
        self.assertEqual(h.periodicity, "daily")

    def test_completion(self):
        h = Habit("Test", "daily")
        h.complete()
        self.assertEqual(len(h.completions), 1)
