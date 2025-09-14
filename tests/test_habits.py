import unittest
from datetime import datetime
from habits.habit_schema import Habit

class TestHabitCore(unittest.TestCase):
    def test_create(self):
        h = Habit("Workout", "daily")
        self.assertEqual(h.name, "Workout")
        self.assertEqual(h.periodicity, "daily")

    def test_complete_adds_timestamp(self):
        h = Habit("Read", "daily")
        h.complete()
        self.assertEqual(len(h.completions), 1)
        self.assertTrue(isinstance(h.completions[0], (str, datetime)))

    def test_delete_is_just_removal_from_collection(self):
        h = Habit("Temp", "weekly")
        items = [h]
        items.remove(h)
        self.assertEqual(items, [])
