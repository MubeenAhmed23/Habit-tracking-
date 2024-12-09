from datetime import datetime, timedelta
import time
import json
from werkzeug.security import generate_password_hash, check_password_hash
import unittest
#  Represents a user in the habit tracking app.
class User:
    def __init__(self, email, password):
        self.email = email
        self.password_hash = self._generate_password_hash(password)
        self.habits = []

    def _generate_password_hash(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_habit(self, habit):
        self.habits.append(habit)
        Database().create('habit', habit)  # Fixed Database instantiation

    def remove_habit(self, habit_name):
        self.habits = [habit for habit in self.habits if habit['name'] != habit_name]

    def edit_habit(self, habit_name, **kwargs):
        for habit in self.habits:
            if habit['name'] == habit_name:
                for key, value in kwargs.items():
                    habit[key] = value

""" Represents a habit that a user wants to track."""
class Habit:
    def __init__(self, name, description, periodicity):
        self.name = name
        self.description = description
        self.periodicity = periodicity

    def edit(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

"""" Tracks records of habit completion and calculates streaks"""
class HabitRecord:
    def __init__(self, habit_name):
        self.habit_name = habit_name
        self.records = []

    def add_record(self, date):
        self.records.append(date)
        self.records.sort()

    def longest_streak(self):
        if not self.records:
            return 0
        longest_streak = 1
        current_streak = 1
        for i in range(1, len(self.records)):
            if self.records[i] == self.records[i - 1] + timedelta(days=1):
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 1
        return longest_streak

    def current_streak(self):
        if not self.records or self.records[-1] != datetime.now().date():
             return 0
        current_streak = 1
        latest_record_index = len(self.records) - 1
        for i in range(latest_record_index, 0, -1):
            if self.records[i] == self.records[i - 1] + timedelta(days=1):
                current_streak += 1
            else:
                break
        return current_streak
    
"""" Manages the storage and retrieval of user, habit, and habit record data."""

class Database:
    def __init__(self, filename='database.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {
                'users': [],
                'habits': [],
                'habit_records': [],
                'reminders': []
            }

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def create(self, entity_type, entity):
        if entity_type not in self.data:
            self.data[entity_type] = []
        if not isinstance(entity, dict):
            entity = entity.__dict__
        self.data[entity_type].append(entity)
        self.save_data()

    def read(self, entity_type, entity_id=None):
        if entity_id is None:
            return self.data[entity_type]
        else:
            return next((e for e in self.data[entity_type] if e.id == entity_id), None)

    def update(self, entity_type, entity_id, **kwargs):
        entity = self.read(entity_type, entity_id)
        if entity:
            for key, value in kwargs.items():
                setattr(entity, key, value)
            self.save_data()

    def delete(self, entity_type, entity_id):
        entity = self.read(entity_type, entity_id)
        if entity:
            self.data[entity_type].remove(entity)
            self.save_data()

""" Sets reminders for habits, notifying users when it's time to complete them."""

class Reminder:
    def __init__(self, habit_name, time):
        self.habit_name = habit_name
        self.time = time

    def set_reminder(self):
        try:
            while True:
                now = datetime.now()
                if now >= self.time:
                    print(f"Reminder: time to do your '{self.habit_name}' habit!")
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            print("Reminder cancelled.")
        except Exception as e:
            print(f'Error setting reminder: {e}')


"""
Unit tests for the HabitRecord class and related functionality.
    """
class TestHabitRecord(unittest.TestCase):

    def setUp(self):
        # Set up a test database and user
        self.database = Database('test_database.json')
        self.user = User('test@example.com', 'securepassword')
        self.habit = Habit('Exercise', 'Daily workouts', 'Daily')
        self.user.add_habit(self.habit.__dict__)
        self.habit_record = HabitRecord('Exercise')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('securepassword'))

    def test_habit_creation(self):
        self.assertEqual(self.habit.name, 'Exercise')
        self.assertEqual(self.habit.description, 'Daily workouts')
        self.assertEqual(self.habit.periodicity, 'Daily')

    def test_add_habit(self):
        self.database.create('habits', self.habit.__dict__)
        habit_json = json.dumps(self.habit.__dict__, sort_keys=True)
        habits_in_db_json = json.dumps(self.database.data['habits'], sort_keys=True)
        self.assertIn(habit_json, habits_in_db_json)


    def test_remove_habit(self):
        self.user.remove_habit('Exercise')
        self.assertNotIn(self.habit.__dict__, self.user.habits)

    def test_edit_habit(self):
        self.user.edit_habit('Exercise', description='Morning workouts')
        edited_habit = next((habit for habit in self.user.habits if habit['name'] == 'Exercise'), None)
        self.assertEqual(edited_habit['description'], 'Morning workouts')

    def test_add_record(self):
        today = datetime.now().date()
        self.habit_record.add_record(today)
        self.assertIn(today, self.habit_record.records)

    def test_longest_streak(self):
        dates = [datetime.now().date() - timedelta(days=i) for i in range(3)]
        for date in dates:
            self.habit_record.add_record(date)
        self.assertEqual(self.habit_record.longest_streak(), 3)

    def test_current_streak(self):
        dates = [datetime.now().date() - timedelta(days=i) for i in range(2)]
        for date in dates:
            self.habit_record.add_record(date)
        self.assertEqual(self.habit_record.current_streak(), 2)

    def test_database_save_and_load(self):
        self.database.save_data()
        self.database.load_data()
        self.assertIn('users', self.database.data)
        self.assertIn('habits', self.database.data)
        self.assertIn('habit_records', self.database.data)

    
if __name__ == '__main__':
    unittest.main()
