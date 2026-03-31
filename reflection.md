# PawPal+ Project Reflection

## 1. System Design

**Core Actions:**
1. Add a pet - Allow users to enter and store pet information.
2. Schedule a task - Enable adding and editing care tasks for pets with details like time, frequency, and priority.
3. See today's tasks - Generate and display a daily schedule of tasks based on priorities and constraints.

**a. Initial design**

The initial UML design includes four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages multiple pets and provides access to all their tasks. The Pet class stores pet details and a list of tasks. The Task class represents a single activity with description, time, frequency, and completion status. The Scheduler class retrieves, organizes, and manages tasks across pets, including sorting by time, filtering, and detecting conflicts.

**b. Design changes**

The design changed during implementation to support recurring tasks. Added a 'date' attribute to the Task class and a 'mark_task_complete' method to the Scheduler class to automatically create next-day tasks for daily frequencies.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time (for sorting), frequency (for recurring tasks), and conflicts (exact time matches). Priorities are handled through time-based ordering, where earlier tasks are prioritized. I decided on these constraints as they cover the core pet care needs: daily routines, recurring schedules, and avoiding overlaps.

**b. Tradeoffs**

The scheduler only checks for exact time matches instead of overlapping durations, which simplifies the logic and improves performance but may miss conflicts where tasks have different start times but overlap in duration.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools throughout the project for design brainstorming (generating UML diagrams), code implementation (fleshing out class methods), debugging (identifying test failures), and documentation (generating docstrings). The most helpful prompts were specific requests like "Create a Mermaid.js class diagram for these classes" and "Implement sorting logic using sorted() with lambda".

**b. Judgment and verification**

I rejected an AI suggestion for a more complex conflict detection algorithm that checked for overlapping durations, as it would complicate the code unnecessarily for this simple app. Instead, I kept the exact time match detection for clarity and simplicity. I evaluated by considering the app's scope and user needs, verifying through testing that the simple version met requirements.

---

## 4. Testing and Verification

**a. What you tested**

I tested core behaviors including task completion and addition, sorting tasks by time, recurrence logic for daily tasks, and conflict detection for duplicate times. These tests ensure the system's reliability for pet scheduling.

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
