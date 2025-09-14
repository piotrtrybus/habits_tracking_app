import unittest
from datetime import date, timedelta

from habits.habit_schema import Habit
from analytics.analytics_module import (
    list_all,
    filter_by_periodicity,
    streak,
    longest_streak,
)

def mkhabit(name, periodicity, dates):
    """Build a Habit with completions for simple tests."""
    h = Habit(name, periodicity)
    h.completions = list(dates)  # your analytics expect date objects
    return h

class TestAnalyticsSimple(unittest.TestCase):
    def test_list_all_and_filter(self):
        a = mkhabit("A", "daily", [])
        b = mkhabit("B", "weekly", [])
        c = mkhabit("C", "daily", [])
        self.assertEqual(list_all([a, b, c]), ["A", "B", "C"])
        self.assertEqual([h.name for h in filter_by_periodicity([a, b, c], "daily")], ["A", "C"])
        self.assertEqual([h.name for h in filter_by_periodicity([a, b, c], "weekly")], ["B"])

    def test_streak_daily(self):
        base = date(2025, 8, 18)
        h = mkhabit("Daily", "daily", [base, base + timedelta(days=1), base + timedelta(days=2)])
        self.assertEqual(streak(h), 3)

    def test_streak_weekly(self):
        base_mon = date(2025, 8, 18)  # Monday
        h = mkhabit("Weekly", "weekly", [base_mon, base_mon + timedelta(weeks=1), base_mon + timedelta(weeks=2)])
        # simple/positive case: three weeks in a row
        self.assertEqual(streak(h), 3)

    def test_longest_streak(self):
        base = date(2025, 8, 18)
        h1 = mkhabit("D", "daily", [base, base + timedelta(days=1)])              # 2
        h2 = mkhabit("W", "weekly", [base, base + timedelta(weeks=1), base + timedelta(weeks=2)])  # 3
        self.assertEqual(longest_streak([h1, h2]), 3)
