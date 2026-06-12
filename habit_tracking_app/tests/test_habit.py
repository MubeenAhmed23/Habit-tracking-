import unittest
from models import Habit
from datetime import datetime


class TestHabit(unittest.TestCase):


    def test_create_habit(self):

        habit = Habit(
            1,
            1,
            "Walking",
            "30 minutes walk",
            "daily",
            datetime.now()
        )


        self.assertEqual(
            habit.name,
            "Walking"
        )


        self.assertEqual(
            habit.periodicity,
            "daily"
        )



    def test_add_log(self):

        habit = Habit(

            1,
            1,
            "Exercise",
            "Workout",
            "daily",
            datetime.now()

        )


        result = habit.add_log()


        self.assertTrue(result)



    def test_duplicate_log(self):

        habit = Habit(

            1,
            1,
            "Reading",
            "Read book",
            "daily",
            datetime.now()

        )


        habit.add_log()


        result = habit.add_log()


        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()