Habit Tracking App:

This Habit Tracking App is a Python-based application that allows users to create, manage, and track their habits. The app provides functionalities for tracking habit completion, analyzing streaks, and setting reminders. It also includes unit tests to ensure the correctness of the core functionalities.

Features:

User Management: Create and manage user accounts with password protection.
Habit Management: Add, edit, and delete habits, with the ability to define periodicity (e.g., daily habits).
Habit Tracking: Track habit completion with automated streak analysis (longest and current streaks).
Reminders: Set reminders to notify users when it's time to complete a habit.
Data Persistence: Save and load user, habit, and habit record data using JSON files.
Unit Testing: Unit tests to validate the core functionalities of the app.
Requirements
To run the Habit Tracking App, the following requirements must be met:

Python 3.8+: Ensure Python is installed on your system. You can download it from the official Python website.

Werkzeug: This is used for password hashing to secure user credentials. Install it using pip:
Command: pip install Werkzeug

Clone the Repository: Download or clone the repository to your local machine.
Git Command:
    git clone: repository link

Run the Application: Navigate to the directory where the code is located and run the Python script.

Run Unit Tests: To ensure everything is functioning correctly, run the unit tests.

Usage:

Creating a User: Instantiate the User class with an email and password to create a new user.
Adding a Habit: Use the add_habit method to add a new habit to the user's habit list.
Tracking Habits: The HabitRecord class allows you to track habit completion by date.
Setting Reminders: Use the Reminder class to set a time-based reminder for any habit.

Files:

habit_tracking_app.py: The main application code.
test_habit_tracking_app.py: Unit tests for the habit tracking app.
database.json: The JSON file where user, habit, and habit record data is stored.

Contributing:

Feel free to fork the repository and submit pull requests if you have improvements or additional features you'd like to add.

Contact:

For any questions or issues, please reach out to mubinsoomro@gmail.com .