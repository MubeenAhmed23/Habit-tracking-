from models import Habit
from datetime import datetime, timedelta


def load_predefined_habits(db):
    habits = [
        ("Exercise", "Daily workout", "daily"),
        ("Read", "Read books", "daily"),
        ("Meditate", "Mindfulness", "daily"),
        ("Clean", "House cleaning", "weekly"),
        ("Call Family", "Stay connected", "weekly"),
    ]

    for name, desc, per in habits:
        habit = Habit(
            id=0,
            name=name,
            description=desc,
            periodicity=per,
            created_at=datetime.now()
        )

        habit_id = db.add_habit(habit)

        # 4 weeks logs
        for i in range(28):
            if per == "daily":
                db.add_log(habit_id)
            elif per == "weekly" and i % 7 == 0:
                db.add_log(habit_id)