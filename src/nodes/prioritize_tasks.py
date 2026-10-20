
import json

from src.llm import get_llm
from src.schemas import TaskPrioritization
from src.state import TaskState


def prioritize_tasks(state: TaskState) -> dict:
    """Assign a priority to every extracted task."""
    tasks = state["tasks"]

    if not tasks:
        return {"tasks": []}

    prompt = f"""
You are the task prioritization component of IntelliTask AI.

Prioritize the supplied tasks.

Rules:
1. Return exactly the same tasks, in the same order.
2. Preserve every title and due_date exactly.
3. Assign one priority: High, Medium, or Low.
4. High means urgent or time-sensitive.
5. Medium means important but not immediately urgent.
6. Low means routine or less urgent.
7. Never invent deadlines.
8. Return ONLY valid JSON in this exact format:
{{
  "tasks": [
    {{
      "title": "Complete assignment",
      "due_date": "tomorrow",
      "priority": "High"
    }}
  ]
}}

Use null for a missing due_date.

Input tasks:
{json.dumps(tasks, ensure_ascii=False)}
"""

    response = get_llm().invoke(prompt)
    content = response.content

    if isinstance(content, list):
        content = "".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict)
        )

    content = content.strip()

    # Remove Markdown code fences if the model includes them.
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        content = content.rsplit("```", 1)[0].strip()

    parsed = json.loads(content)

    # Handle a model that returns a list instead of {"tasks": [...]}.
    if isinstance(parsed, list):
        parsed = {"tasks": parsed}

    result = TaskPrioritization.model_validate(parsed)
    prioritized = [task.model_dump() for task in result.tasks]

    if len(prioritized) != len(tasks):
        raise ValueError(
            "Prioritization returned a different number of tasks."
        )

    for original, updated in zip(tasks, prioritized):
        if (
            original["title"] != updated["title"]
            or original.get("due_date") != updated.get("due_date")
        ):
            raise ValueError(
                "Prioritization changed a task title or due date."
            )

    return {"tasks": prioritized}
