import sqlite3
from datetime import datetime
from models import Habit, HabitLog


class Database:
    def __init__(self, db_name="habits.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            periodicity TEXT,
            created_at TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS habit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            completed_at TEXT,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
        """)

        self.conn.commit()

    # ---------- HABITS ----------
    def add_habit(self, habit):
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO habits (name, description, periodicity, created_at)
        VALUES (?, ?, ?, ?)
        """, (habit.name, habit.description, habit.periodicity, habit.created_at.isoformat()))

        self.conn.commit()
        return cursor.lastrowid

    def get_habits(self):
        cursor = self.conn.cursor()
        rows = cursor.execute("SELECT * FROM habits").fetchall()

        habits = []
        for row in rows:
            habit = Habit(
                id=row[0],
                name=row[1],
                description=row[2],
                periodicity=row[3],
                created_at=datetime.fromisoformat(row[4])
            )
            habit.logs = self.get_logs(habit.id)
            habits.append(habit)

        return habits

    # ---------- LOGS ----------
    def add_log(self, habit_id):
        cursor = self.conn.cursor()
        now = datetime.now().date().isoformat()

        cursor.execute("""
        INSERT INTO habit_logs (habit_id, completed_at)
        VALUES (?, ?)
        """, (habit_id, now))

        self.conn.commit()

    def get_logs(self, habit_id):
        cursor = self.conn.cursor()

        rows = cursor.execute("""
        SELECT habit_id, completed_at
        FROM habit_logs
        WHERE habit_id=?
        ORDER BY completed_at
        """, (habit_id,)).fetchall()

        return [HabitLog(habit_id=row[0], completed_at=datetime.fromisoformat(row[1]).date()) for row in rows]