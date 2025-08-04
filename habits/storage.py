import json
from habits.habit_schema import Habit

def save_habits(habits, filepath='habits.json'):
    with open(filepath, 'w') as f:
        json.dump([h.to_dict() for h in habits], f)

def load_habits(filepath='habits.json'):
    try:
        with open(filepath) as f:
            data = json.load(f)
        return [Habit.from_dict(d) for d in data]
    except FileNotFoundError:
        return []


def load_predefined_habits(filepath='predefined_habits.json'):
    try:
        with open(filepath) as f:
            data = json.load(f)
        return [Habit.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
