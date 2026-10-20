from src.graph import task_graph
from src.nodes.format_results import format_results


def test_format_results_with_tasks():
    state = {
        "user_input": "Finish homework tomorrow",
        "tasks": [
            {
                "title": "Finish homework",
                "due_date": "tomorrow",
                "priority": "High",
            }
        ],
        "formatted_results": "",
    }

    result = format_results(state)

    assert "Finish homework" in result["formatted_results"]
    assert "Priority: High" in result["formatted_results"]
    assert "Due date: tomorrow" in result["formatted_results"]
    assert "Total tasks: 1" in result["formatted_results"]


def test_format_results_without_tasks():
    state = {
        "user_input": "Hello",
        "tasks": [],
        "formatted_results": "",
    }

    result = format_results(state)

    assert "No actionable tasks" in result["formatted_results"]


def test_graph_contains_three_nodes():
    graph = task_graph.get_graph()
    node_names = set(graph.nodes.keys())

    assert "extract_tasks" in node_names
    assert "prioritize_tasks" in node_names
    assert "format_results" in node_names