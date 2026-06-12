import unittest

from models import Habit, HabitLog
from analytics import longest_streak
from datetime import datetime, date, timedelta



class TestAnalytics(unittest.TestCase):


    def test_longest_streak(self):


        habit = Habit(

            1,
            1,
            "Exercise",
            "Workout",
            "daily",
            datetime.now()

        )


        habit.logs = [

            HabitLog(
                1,
                1,
                date.today()-timedelta(days=2)
            ),

            HabitLog(
                2,
                1,
                date.today()-timedelta(days=1)
            ),

            HabitLog(
                3,
                1,
                date.today()
            )

        ]


        result = longest_streak(habit)


        self.assertEqual(
            result,
            3
        )



if __name__ == "__main__":
    unittest.main()