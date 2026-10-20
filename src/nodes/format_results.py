from src.state import TaskState


def format_results(state: TaskState) -> dict:
    """Format prioritized tasks into a readable to-do list."""
    tasks = state["tasks"]

    if not tasks:
        return {
            "formatted_results": (
                "INTELLITASK AI\n"
                "No actionable tasks were found in your input."
            )
        }

    lines = [
        "INTELLITASK AI",
        "AI-POWERED TASK MANAGEMENT ASSISTANT",
        "=" * 42,
        "",
    ]

    for index, task in enumerate(tasks, start=1):
        lines.append(f"{index}. {task['title']}")
        lines.append(f"   Priority: {task['priority']}")

        due_date = task.get("due_date")
        if due_date:
            lines.append(f"   Due date: {due_date}")

        lines.append("")

    lines.append(f"Total tasks: {len(tasks)}")

    return {
        "formatted_results": "\n".join(lines)
    }