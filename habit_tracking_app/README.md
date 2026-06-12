# HabitFlow - Habit Tracking Application

## Description

HabitFlow is a Python based habit tracking application.
It allows users to create habits, track completion events,
store data using SQLite and calculate habit analytics.

## Features

- Create habits
- Complete habits
- Delete habits
- SQLite database storage
- Habit completion logs
- Streak calculation
- Object oriented design

## Technologies

- Python 3
- SQLite
- unittest

## Project Structure

models.py
- Contains User, Habit and HabitLog classes

database.py
- Handles SQLite operations

tracker.py
- Controls habit operations

analytics.py
- Calculates streaks

main.py
- Command line interface


## How to Run

Install Python 3.

Run:

python Main.py


## Database

The application automatically creates:

habits.db

which stores:

Users
Habits
Habit completion logs