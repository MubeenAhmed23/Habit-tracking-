from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List


@dataclass
class User:
    id: int
    email: str


@dataclass
class HabitLog:

    id: int
    habit_id: int
    completed_at: date



@dataclass
class Habit:

    id: int
    user_id: int
    name: str
    description: str
    periodicity: str
    created_at: datetime
    logs: List[HabitLog] = field(default_factory=list)


    def add_log(self):

        today = datetime.now().date()

        for log in self.logs:
            if log.completed_at == today:
                return False

        self.logs.append(
            HabitLog(
                0,
                self.id,
                today
            )
        )

        return True