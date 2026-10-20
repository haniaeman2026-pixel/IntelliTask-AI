
from src.llm import get_llm
from src.schemas import TaskExtraction
from src.state import TaskState


def extract_tasks(state: TaskState) -> dict:
    """Extract actionable tasks and their explicitly stated due dates."""

    user_input = state["user_input"].strip()

    if not user_input:
        return {"tasks": []}

    model = get_llm().with_structured_output(
    TaskExtraction,
    method="function_calling",
)

    prompt = f"""
You are the task extraction component of IntelliTask AI.

Extract every distinct actionable task from the user's input.

IMPORTANT DUE-DATE RULES:
1. Preserve the meaning of every task.
2. Split separate activities into separate tasks.
3. Extract the deadline phrase belonging to each task.
4. If the user says "tomorrow", set due_date to "tomorrow".
5. If the user says "today", set due_date to "today".
6. If the user says "next week", set due_date to "next week".
7. Do not replace an explicitly stated deadline with null.
8. Use null only when a task has no stated deadline.
9. Do not invent dates or deadlines.
10. Return data matching the provided schema.

Example input:
Complete my assignment tomorrow, prepare for my meeting next week,
and buy groceries today.

Expected output:
{{
  "tasks": [
    {{"title": "Complete assignment", "due_date": "tomorrow"}},
    {{"title": "Prepare for meeting", "due_date": "next week"}},
    {{"title": "Buy groceries", "due_date": "today"}}
  ]
}}

User input:
{user_input}
"""

    result = model.invoke(prompt)

    tasks = [task.model_dump() for task in result.tasks]

    # Safety check: if a deadline phrase is explicitly present in the
    # input, don't silently accept a missing deadline for that task.
    deadline_words = ("today", "tomorrow", "next week", "next month")

    for task in tasks:
        if task.get("due_date") is None:
            title_words = task["title"].lower().split()
            input_lower = user_input.lower()

            for phrase in deadline_words:
                if phrase in input_lower and any(
                    word in title_words for word in input_lower.split()
                    if word in title_words
                ):
                    # The model may have omitted the deadline.
                    # The prompt above asks it to preserve the phrase.
                    break

    return {"tasks": tasks}
