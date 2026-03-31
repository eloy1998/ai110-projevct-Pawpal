from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False
    date: str = None

    def __post_init__(self):
        if self.date is None:
            from datetime import date
            self.date = date.today().isoformat()

    def mark_complete(self):
        self.completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = None

    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        return [task for pet in self.pets for task in pet.tasks]

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_schedule(self) -> List[Task]:
        from datetime import date
        today = date.today().isoformat()
        return [t for t in self.owner.get_all_tasks() if t.date == today]

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by time in ascending order."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, tasks: List[Task], completed: bool = None) -> List[Task]:
        """Filter tasks by completion status. If completed is None, return all tasks."""
        if completed is not None:
            return [t for t in tasks if t.completed == completed]
        return tasks

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Detect tasks scheduled at the same time and return conflict messages."""
        from collections import defaultdict
        time_dict = defaultdict(list)
        for task in tasks:
            time_dict[task.time].append(task)
        conflicts = []
        for time, tsks in time_dict.items():
            if len(tsks) > 1:
                conflicts.append(f"Conflict at {time}: {[t.description for t in tsks]}")
        return conflicts

    def mark_task_complete(self, task: Task, pet: Pet):
        """Mark a task as complete and create a recurring task if applicable."""
        task.mark_complete()
        if task.frequency == "daily":
            from datetime import datetime, timedelta
            next_date = (datetime.fromisoformat(task.date).date() + timedelta(days=1)).isoformat()
            new_task = Task(task.description, task.time, task.frequency, date=next_date)
            pet.add_task(new_task)