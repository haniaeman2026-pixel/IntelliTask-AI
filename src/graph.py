from langgraph.graph import END, START, StateGraph

from src.nodes.extract_tasks import extract_tasks
from src.nodes.prioritize_tasks import prioritize_tasks
from src.nodes.format_results import format_results
from src.state import TaskState


def build_graph():
    """Build and compile the IntelliTask AI workflow."""
    workflow = StateGraph(TaskState)

    workflow.add_node("extract_tasks", extract_tasks)
    workflow.add_node("prioritize_tasks", prioritize_tasks)
    workflow.add_node("format_results", format_results)

    workflow.add_edge(START, "extract_tasks")
    workflow.add_edge("extract_tasks", "prioritize_tasks")
    workflow.add_edge("prioritize_tasks", "format_results")
    workflow.add_edge("format_results", END)

    return workflow.compile()


task_graph = build_graph()