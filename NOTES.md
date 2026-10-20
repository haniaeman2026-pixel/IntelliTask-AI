# IntelliTask AI — Assignment Notes

## 1. Project Objective

IntelliTask AI is an AI-powered task management assistant. It accepts natural-language input, extracts individual tasks, assigns priorities, and generates an organized to-do list.

## 2. Technologies Used

- **Python:** Main programming language.
- **LangGraph:** Connects and executes the workflow nodes.
- **Groq API:** Provides access to the selected language model.
- **LangChain Groq:** Integrates the Groq model with Python.
- **Pydantic:** Validates structured task data.
- **python-dotenv:** Loads environment variables from `.env`.
- **pytest:** Runs automated tests.

## 3. Workflow Explanation

### Node 1 — Task Extraction

The extraction node reads the user's input and identifies distinct actionable tasks. It preserves task meaning and any explicitly stated due-date phrases.

### Node 2 — Task Prioritization

The prioritization node assigns one of three labels: High, Medium, or Low. It must preserve the extracted task titles and due dates.

### Node 3 — Format Results

The formatting node converts structured task data into a readable to-do list. It does not require another LLM call.

## 4. Important Concepts

**LangGraph:** A framework for defining stateful workflows using nodes and edges.

**Node:** A function that performs one specific operation in the workflow.

**State:** Shared data passed between workflow nodes.

**LLM:** A large language model used to interpret natural-language input.

**Structured Output:** Data returned in a predefined format that can be validated.

**Pydantic:** A Python library for data validation and schema definition.

**API:** An interface that allows one application to communicate with another service.

**Environment Variables:** Configuration values stored separately from application code.

## 5. Why Use Three Nodes?

Separating extraction, prioritization, and formatting makes the workflow easier to understand, test, debug, and extend.

## 6. Limitations

- Priority assignments depend on model interpretation.
- Relative due dates are preserved as phrases rather than converted into calendar dates.
- Tasks are not saved permanently.
- The current version runs in the terminal; a GUI is a separate future enhancement.

## 7. Viva Questions

**Q: What is the main purpose of this project?**

A: To convert natural-language task descriptions into a prioritized to-do list.

**Q: Why is LangGraph used?**

A: To define and connect the three workflow nodes and pass state between them.

**Q: What is the role of Groq?**

A: It provides access to the language model used for task extraction and prioritization.

**Q: Why is Pydantic used?**

A: To validate the structure and types of the task data.

**Q: Does every node call the AI model?**

A: No. The extraction and prioritization nodes call the model, while the formatting node uses Python.

**Q: Is the application a complete persistent task manager?**

A: Not yet. The current version generates task lists but does not store them between sessions.
