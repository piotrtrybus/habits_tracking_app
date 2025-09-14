from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        """Create a habit with a name and weekly/daily periodicity"""
        if periodicity not in ('daily', 'weekly'):
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions = [] 

    def complete(self):
        """Creates a completion with current timestamp"""
        self.completions.append(datetime.now())

    def to_dict(self):
        """Create a dict form for each habit"""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Habit":
        """Create a Habit from a dict ignoring unknown keys."""
        habit = cls(
            name=data["name"],
            periodicity=data["periodicity"],
        )
        habit.created_at = data.get("created_at", datetime.utcnow().isoformat())
        habit.completions = data.get("completions", [])
        return habit

    