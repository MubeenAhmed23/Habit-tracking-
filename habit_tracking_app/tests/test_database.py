import unittest

from database import Database
from models import Habit
from datetime import datetime



class TestDatabase(unittest.TestCase):


    def test_add_habit(self):

        db = Database(":memory:")


        db.add_user(
            "test@email.com"
        )


        habit = Habit(

            0,
            1,
            "Running",
            "Run daily",
            "daily",
            datetime.now()

        )


        habit_id = db.add_habit(habit)


        self.assertIsNotNone(
            habit_id
        )



if __name__ == "__main__":
    unittest.main()