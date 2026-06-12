# HabitFlow - Habit Tracking Application

## Description

HabitFlow is a Python-based habit tracking application developed using
Object-Oriented Programming principles.

The application allows users to create, manage, and track habits.
Each completion is stored as a habit log event in an SQLite database.
The system can analyse habit progress by calculating current and longest streaks.

## Features

- Create habits
- View existing habits
- Complete habits
- Delete habits
- Store data permanently using SQLite
- Track habit completion events
- Calculate current streaks
- Calculate longest streaks
- Predefined starter habits
- Object-Oriented design
- Automated unit testing

## Technologies

- Python 3
- SQLite3
- unittest
- Dataclasses

## Project Structure
habit_tracking_app/

│
├── Main.py
│ Command line user interface
│
├── models.py
│ Contains User, Habit and HabitLog classes
│
├── database.py
│ Handles SQLite database creation and operations
│
├── tracker.py
│ Application logic for managing habits
│
├── analytics.py
│ Calculates habit statistics and streaks
│
├── predefined.py
│ Creates predefined example habits
│
├── tests/
│ Unit tests for application components
│
└── habits.db
SQLite database file (generated automatically)


## Database Design

The application uses SQLite with two main tables:

### habits

Stores information about each habit:

- id
- name
- description
- periodicity
- created_at


### habit_logs

Stores completion events:

- id
- habit_id
- completed_at


A habit can contain multiple completion logs.

## How to Run

Install Python 3.

Run:
python Main.py


The application will start in the command line.

## Testing

Run:
python -m unittest discover -s tests


Expected result:
Ran 5 tests

OK