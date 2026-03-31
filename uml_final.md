classDiagram
    class Owner {
        +name: str
        +pets: List[Pet]
        +add_pet(pet: Pet)
        +get_all_tasks(): List[Task]
    }
    class Pet {
        +name: str
        +species: str
        +tasks: List[Task]
        +add_task(task: Task)
    }
    class Task {
        +description: str
        +time: str
        +frequency: str
        +completed: bool
        +date: str
        +mark_complete()
    }
    class Scheduler {
        +owner: Owner
        +get_todays_schedule(): List[Task]
        +sort_tasks(tasks: List[Task]): List[Task]
        +filter_tasks(tasks: List[Task], completed: bool = None): List[Task]
        +detect_conflicts(tasks: List[Task]): List[str]
        +mark_task_complete(task: Task, pet: Pet)
    }
    Owner ||--o{ Pet : has
    Pet ||--o{ Task : has
    Scheduler --> Owner : uses