import unittest
from models import Habit
from datetime import datetime


class TestHabit(unittest.TestCase):

    def test_add_log(self):
        h = Habit(1, "Test", "Desc", "daily", datetime.now())
        self.assertTrue(h.add_log())
        self.assertFalse(h.add_log())


if __name__ == "__main__":
    unittest.main()