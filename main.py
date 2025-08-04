from habits.habit_schema import Habit
from habits.storage import load_habits, load_predefined_habits, save_habits
from analytics.analytics_module import (
    list_all,
    filter_by_periodicity,
    longest_streak,
    streak
)

def print_menu():
    print("\nHABIT TRACKER")
    print("1. View custom habits")
    print("2. View predefined habits")
    print("3. Add a new habit") 
    print("4. Log existing habit")
    print("5. Analyze habits")
    print("0. Exit")

def select_habit(habits):
    habit_counter = 0
    for i, h in enumerate(habits):
        habit_counter += 1
        print(f"{habit_counter}. {h.name} ({h.periodicity})")
    #for i, h in enumerate(predefined_habits):
    #    habit_counter += 1
    #    print(f"{habit_counter}. {h.name} ({h.periodicity})")
    choice = int(input("Select a habit number: ")) - 1
    return habits[choice] if 0 <= choice < len(habits) else None


def main():
    custom_habits = load_habits()
    predefined_habits = load_predefined_habits()
    habits = custom_habits + predefined_habits

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            if habits:
                for h in habits:
                    print(f"- {h.name} ({h.periodicity}), created on {h.created_at.date()}")
            else:
                print("No habits found")


        if choice == "2":
            if predefined_habits:
                for h in predefined_habits:
                    print(f"- {h.name} ({h.periodicity})")
            else:
                print("No predefined habits found")


        elif choice == "3":
            name = input("Enter habit name: ")
            period = input("Enter periodicity (daily/weekly): ").lower()
            try:
                habit = Habit(name, period)
                habits.append(habit)
                print("Habit added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            if not habits:
                print("No habits to complete.")
                continue
            habit = select_habit(habits)
            if habit:
                habit.complete()
                print(f"Marked '{habit.name}' as completed.")
        elif choice == "5":
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
