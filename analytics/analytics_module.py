def list_all(habits):
    return [h.name for h in habits]

def filter_by_periodicity(habits, period):
    return list(filter(lambda h: h.periodicity == period, habits))

def longest_streak(habits):
    return max([streak(h) for h in habits], default=0)

def streak(habit):
    # Bas1ic example for daily habits
    sorted_dates = sorted(habit.completions, reverse=True)
    if not sorted_dates:
        return 0
    streak = 1
    for i in range(1, len(sorted_dates)):
        delta = sorted_dates[i-1] - sorted_dates[i]
        if habit.periodicity == 'daily' and delta.days == 1:
            streak += 1
        elif habit.periodicity == 'weekly' and delta.days <= 7:
            streak += 1
        else:
            break
    return streak

