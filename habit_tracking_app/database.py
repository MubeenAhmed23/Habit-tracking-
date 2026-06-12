import sqlite3
from datetime import datetime

from models import Habit, HabitLog


class Database:


    def __init__(self, name="habits.db"):

        self.conn = sqlite3.connect(name)

        self.conn.execute(
            "PRAGMA foreign_keys = ON"
        )

        self.create_tables()



    def create_tables(self):

        cur = self.conn.cursor()


        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT
        )
        """)


        cur.execute("""
        CREATE TABLE IF NOT EXISTS habits(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            name TEXT,

            description TEXT,

            periodicity TEXT,

            created_at TEXT,

            FOREIGN KEY(user_id)
            REFERENCES users(id)

        )
        """)



        cur.execute("""
        CREATE TABLE IF NOT EXISTS logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            habit_id INTEGER,

            completed_at TEXT,

            FOREIGN KEY(habit_id)
            REFERENCES habits(id)

        )
        """)



        self.conn.commit()



    def add_user(self,email):

        cur=self.conn.cursor()

        cur.execute(
            "INSERT INTO users(email) VALUES(?)",
            (email,)
        )

        self.conn.commit()

        return cur.lastrowid



    def add_habit(self,habit):

        cur=self.conn.cursor()


        cur.execute("""

        INSERT INTO habits
        (user_id,name,description,periodicity,created_at)

        VALUES(?,?,?,?,?)

        """,

        (
            habit.user_id,
            habit.name,
            habit.description,
            habit.periodicity,
            habit.created_at.isoformat()
        ))


        self.conn.commit()

        return cur.lastrowid



    def add_log(self,habit_id):

        today=datetime.now().date().isoformat()

        self.conn.execute(
            """
            INSERT INTO logs
            (habit_id,completed_at)

            VALUES(?,?)
            """,

            (habit_id,today)
        )

        self.conn.commit()



    def get_habits(self):

        rows=self.conn.execute(
            "SELECT * FROM habits"
        ).fetchall()


        result=[]


        for row in rows:

            habit=Habit(

                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                datetime.fromisoformat(row[5]),
                []

            )


            habit.logs=self.get_logs(
                habit.id
            )


            result.append(habit)


        return result



    def get_logs(self,habit_id):

        rows=self.conn.execute(

        """
        SELECT * FROM logs
        WHERE habit_id=?

        """,

        (habit_id,)

        ).fetchall()


        return [

            HabitLog(
                r[0],
                r[1],
                datetime.fromisoformat(
                    r[2]
                ).date()

            )

            for r in rows

        ]



    def delete_habit(self,id):

        self.conn.execute(
            "DELETE FROM logs WHERE habit_id=?",
            (id,)
        )


        self.conn.execute(
            "DELETE FROM habits WHERE id=?",
            (id,)
        )


        self.conn.commit()