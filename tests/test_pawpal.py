import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task("Test Task", "10:00", "daily")
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_task_addition():
    pet = Pet("Test Pet", "Dog")
    task = Task("Test Task", "10:00", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task

def test_sorting():
    tasks = [Task("B", "12:00", "daily"), Task("A", "08:00", "daily")]
    scheduler = Scheduler(Owner("test"))
    sorted_tasks = scheduler.sort_tasks(tasks)
    assert sorted_tasks[0].description == "A"
    assert sorted_tasks[1].description == "B"

def test_recurrence():
    owner = Owner("test")
    pet = Pet("test", "dog")
    owner.add_pet(pet)
    task = Task("test", "10:00", "daily")
    pet.add_task(task)
    scheduler = Scheduler(owner)
    scheduler.mark_task_complete(task, pet)
    assert len(pet.tasks) == 2
    assert pet.tasks[1].description == "test"
    # Check date is next day
    from datetime import datetime, timedelta
    today = datetime.now().date()
    next_day = (today + timedelta(days=1)).isoformat()
    assert pet.tasks[1].date == next_day

def test_conflict():
    tasks = [Task("A", "10:00", "daily"), Task("B", "10:00", "daily")]
    scheduler = Scheduler(Owner("test"))
    conflicts = scheduler.detect_conflicts(tasks)
    assert len(conflicts) == 1
    assert "10:00" in conflicts[0]