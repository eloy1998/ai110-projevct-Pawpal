from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("John Doe")

# Create pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Add tasks out of order
task1 = Task("Walk", "08:00", "daily")
task2 = Task("Feed", "12:00", "daily")
task3 = Task("Play", "18:00", "daily")
task4 = Task("Groom", "08:00", "daily")  # conflicting

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)
pet1.add_task(task4)

# Create scheduler
scheduler = Scheduler(owner)

# Get today's schedule
schedule = scheduler.get_todays_schedule()
sorted_schedule = scheduler.sort_tasks(schedule)

# Print schedule
print("Today's Schedule:")
for task in sorted_schedule:
    print(f"- {task.time}: {task.description} ({'Completed' if task.completed else 'Pending'})")

# Detect conflicts
conflicts = scheduler.detect_conflicts(sorted_schedule)
if conflicts:
    print("\nConflicts:")
    for conflict in conflicts:
        print(conflict)

# Mark a task complete to test recurring
if sorted_schedule:
    print(f"\nMarking '{sorted_schedule[0].description}' as complete...")
    scheduler.mark_task_complete(sorted_schedule[0], pet1)
    print("Recurring task created for tomorrow.")

# Show pending tasks only
pending = scheduler.filter_tasks(sorted_schedule, completed=False)
print(f"\nPending tasks: {len(pending)}")