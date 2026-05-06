from database import Database
from models import Habit
from analytics import get_longest_streak, get_current_streak
from predefined import load_predefined_habits
from datetime import datetime


def run():
    db = Database()

    if not db.get_habits():
        load_predefined_habits(db)

    while True:
        print("\n1. Add Habit")
        print("2. Complete Habit")
        print("3. Show Habits")
        print("4. Analytics")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            desc = input("Description: ")
            per = input("daily/weekly: ")

            habit = Habit(0, name, desc, per, datetime.now())
            db.add_habit(habit)

        elif choice == "2":
            habits = db.get_habits()
            for h in habits:
                print(h.id, h.name)

            habit_ids = input("Habit IDs (space separated): ").split()

            for hid in habit_ids:
                try:
                    db.add_log(int(hid))
                    print(f"Habit {hid} completed!")
                except ValueError:
                    print(f"Invalid ID: {hid}")

        elif choice == "3": 
            for h in db.get_habits():
                print(h.id, h.name, "-", h.periodicity)

        elif choice == "4":
            for h in db.get_habits():
                print(f"\n{h.name}")
                print("Longest:", get_longest_streak(h))
                print("Current:", get_current_streak(h))

        elif choice == "5":
            break


if __name__ == "__main__":
    run()