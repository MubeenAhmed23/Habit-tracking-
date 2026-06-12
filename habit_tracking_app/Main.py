from database import Database
from tracker import HabitTracker


def run():

    db = Database()

    tracker = HabitTracker(db)


    # create default user if database is empty
    users = db.conn.execute(
        "SELECT * FROM users"
    ).fetchall()


    if not users:

        db.add_user(
            "student@example.com"
        )


    while True:


        print("""
1 Create habit
2 Show habits
3 Complete habit
4 Delete habit
5 Exit
""")


        choice=input("Choose: ")



        if choice=="1":

            tracker.create_habit(

                1,

                input("Name: "),

                input("Description: "),

                input("daily/weekly: ")

            )

            print("Habit created!")


        elif choice=="2":

            habits=tracker.get_habits()

            for h in habits:

                print(
                    h.id,
                    h.name,
                    "-",
                    h.periodicity
                )


        elif choice=="3":

            tracker.complete_habit(

                int(input("Habit ID: "))

            )

            print("Completed!")


        elif choice=="4":

            tracker.delete_habit(

                int(input("Habit ID: "))

            )

            print("Deleted!")


        elif choice=="5":

            break



if __name__=="__main__":
    run()