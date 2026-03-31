# PawPal+ Project Reflection

## 1. System Design

**Core Actions:**
1. Add a pet - Allow users to enter and store pet information.
2. Schedule a task - Enable adding and editing care tasks for pets with details like time, frequency, and priority.
3. See today's tasks - Generate and display a daily schedule of tasks based on priorities and constraints.

**a. Initial design**

The initial UML design includes four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages multiple pets and provides access to all their tasks. The Pet class stores pet details and a list of tasks. The Task class represents a single activity with description, time, frequency, and completion status. The Scheduler class retrieves, organizes, and manages tasks across pets, including sorting by time, filtering, and detecting conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

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
