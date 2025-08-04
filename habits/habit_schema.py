from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        if periodicity not in ('daily', 'weekly'):
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions = [] 

    def complete(self):
        self.completions.append(datetime.now())

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions]
        }

    @staticmethod
    def from_dict(data):
        habit = Habit(data["name"], data["periodicity"])
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.completions = [datetime.fromisoformat(c) for c in data["completions"]]
        return habit
