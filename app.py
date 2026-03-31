import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

if 'owner' not in st.session_state:
    st.session_state.owner = Owner("Jordan")

owner = st.session_state.owner
scheduler = Scheduler(owner)

st.divider()

st.subheader("Manage Pets and Tasks")

with st.form("add_pet"):
    st.write("Add a Pet")
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    submitted_pet = st.form_submit_button("Add Pet")
    if submitted_pet:
        pet = Pet(pet_name, species)
        owner.add_pet(pet)
        st.success(f"Added pet {pet_name}")

st.subheader("Current Pets")
for pet in owner.pets:
    st.write(f"- {pet.name} ({pet.species})")

if owner.pets:
    with st.form("add_task"):
        st.write("Add a Task")
        pet_options = [pet.name for pet in owner.pets]
        selected_pet = st.selectbox("Select Pet", pet_options)
        description = st.text_input("Task Description", value="Morning walk")
        time = st.text_input("Time (HH:MM)", value="08:00")
        frequency = st.selectbox("Frequency", ["daily", "weekly"])
        submitted_task = st.form_submit_button("Add Task")
        if submitted_task:
            task = Task(description, time, frequency)
            pet = next(p for p in owner.pets if p.name == selected_pet)
            pet.add_task(task)
            st.success(f"Added task {description} for {selected_pet}")

st.divider()

st.subheader("Today's Schedule")

if st.button("Generate Schedule"):
    schedule = scheduler.get_todays_schedule()
    sorted_schedule = scheduler.sort_tasks(schedule)
    conflicts = scheduler.detect_conflicts(sorted_schedule)
    if conflicts:
        for conflict in conflicts:
            st.warning(conflict)
    if sorted_schedule:
        st.table([{"Time": t.time, "Description": t.description, "Status": "Completed" if t.completed else "Pending"} for t in sorted_schedule])
    else:
        st.info("No tasks scheduled for today.")
