from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List


@dataclass
class HabitLog:
    habit_id: int
    completed_at: date


@dataclass
class Habit:
    id: int
    name: str
    description: str
    periodicity: str  # daily / weekly
    created_at: datetime
    logs: List[HabitLog] = field(default_factory=list)

    def add_log(self) -> bool:
        today = datetime.now().date()

        if any(log.completed_at == today for log in self.logs):
            return False

        self.logs.append(HabitLog(self.id, today))
        return True


@dataclass
class User:
    id: int
    email: str