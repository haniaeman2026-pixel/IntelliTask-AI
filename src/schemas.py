from typing import Literal

from pydantic import BaseModel, Field


class ExtractedTask(BaseModel):
    title: str = Field(
        min_length=1,
        description="A concise, actionable task title.",
    )
    due_date: str | None = Field(
        default=None,
        description=(
            "The due date or time phrase explicitly stated "
            "by the user. Do not invent a date."
        ),
    )


class TaskExtraction(BaseModel):
    tasks: list[ExtractedTask] = Field(
        description="All distinct actionable tasks in the input."
    )


class PrioritizedTask(BaseModel):
    title: str = Field(min_length=1)
    due_date: str | None = None
    priority: Literal["High", "Medium", "Low"]


class TaskPrioritization(BaseModel):
    tasks: list[PrioritizedTask]