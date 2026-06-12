from models import Habit
from datetime import datetime


class HabitTracker:


    def __init__(self,database):

        self.database=database



    def create_habit(
        self,
        user_id,
        name,
        description,
        periodicity
    ):


        habit=Habit(

            0,
            user_id,
            name,
            description,
            periodicity,
            datetime.now()

        )


        return self.database.add_habit(habit)



    def complete_habit(self,id):

        self.database.add_log(id)



    def get_habits(self):

        return self.database.get_habits()



    def delete_habit(self,id):

        self.database.delete_habit(id)