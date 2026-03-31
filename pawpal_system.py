from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = None

    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []

    def add_task(self, task: Task):
        pass

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self) -> List[Task]:
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_todays_schedule(self) -> List[Task]:
        pass

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        pass

    def filter_tasks(self, tasks: List[Task], criteria) -> List[Task]:
        pass

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        pass