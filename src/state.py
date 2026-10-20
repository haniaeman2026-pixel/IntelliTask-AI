from typing import Any, TypedDict


class TaskState(TypedDict):
    user_input: str
    tasks: list[dict[str, Any]]
    formatted_results: str