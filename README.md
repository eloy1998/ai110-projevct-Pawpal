# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Features

PawPal+ includes the following key features:
- **Pet Management**: Add and manage multiple pets with species information.
- **Task Scheduling**: Create tasks with time, frequency (daily/weekly), and descriptions.
- **Sorting by Time**: Automatically sorts daily tasks chronologically for clear planning.
- **Conflict Detection**: Warns about tasks scheduled at the same time to prevent overlaps.
- **Recurring Tasks**: Daily tasks automatically generate the next occurrence when marked complete.
- **Filtering**: Filter tasks by completion status to focus on pending items.
- **Data Persistence**: Save and load pet and task data to/from a JSON file for persistence between sessions.

## 📸 Demo

<a href="/course_images/ai110/pawpal_screenshot.png" target="_blank"><img src='/course_images/ai110/pawpal_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>

## Testing PawPal+

Run the automated test suite with: `python -m pytest`

The tests cover core behaviors including task completion, addition, sorting by time, recurrence logic for daily tasks, and conflict detection for overlapping schedules.

**Confidence Level**: ⭐⭐⭐⭐⭐ (5 stars) - All tests pass, verifying the system's reliability for pet scheduling. 
## Extensions

### Data Persistence
Implemented data persistence using JSON serialization. The Owner class now includes `save_to_json()` and `load_from_json()` methods to store and retrieve pet and task data. The Streamlit app loads data on startup and provides a save button. This was implemented using Agent Mode to plan the serialization logic and handle complex object conversion to dictionaries for JSON compatibility.
## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
