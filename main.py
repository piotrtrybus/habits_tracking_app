from habits.habit_schema import Habit
from habits.storage import load_habits, save_habits
from analytics.analytics_module import (
    list_all,
    filter_by_periodicity,
    longest_streak,
    streak
)

def print_menu():
    print("\nHABIT TRACKER")
    print("1. View all habits")
    print("2. Add a new habit")
    print("3. Log existing habit")
    print("4. Analyze habits")
    print("0. Exit")

def select_habit(habits):
    for i, h in enumerate(habits):
        print(f"{i + 1}. {h.name} ({h.periodicity})")
    choice = int(input("Select a habit number: ")) - 1
    return habits[choice] if 0 <= choice < len(habits) else None


def main():
    habits = load_habits()

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            if habits:
                for h in habits:
                    print(f"- {h.name} ({h.periodicity}), created on {h.created_at.date()}")
            else:
                print("No habits found")
        elif choice == "2":
            name = input("Enter habit name: ")
            period = input("Enter periodicity (daily/weekly): ").lower()
            try:
                habit = Habit(name, period)
                habits.append(habit)
                print("Habit added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            if not habits:
                print("No habits to complete.")
                continue
            habit = select_habit(habits)
            if habit:
                habit.complete()
                print(f"Marked '{habit.name}' as completed.")
        elif choice == "4":
            print("Analytics:")
            print("1. List all habits")
            print("2. Filter by periodicity")
            print("3. Longest streak (all habits)")
            print("4. Longest streak (specific habit)")
            sub_choice = input("Choose option: ")
            if sub_choice == "1":
                for h in habits:
                    print(f"- {h.name} ({h.periodicity}), created on {h.created_at.date()}")
            elif sub_choice == "2":
                p = input("Enter periodicity (daily/weekly): ")
                print([h.name for h in filter_by_periodicity(habits, p)])
            elif sub_choice == "3":
                print("Longest streak:", longest_streak(habits))
            elif sub_choice == "4":
                habit = select_habit(habits)
                if habit:
                    print(f"{habit.name}: {streak(habit)}")
        elif choice == "0":
            save_habits(habits)
            print("Habits saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
