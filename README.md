# IntelliTask AI

An AI-powered task management assistant built with Python,
LangGraph, and Groq.

## Overview

IntelliTask AI converts natural-language descriptions into
structured tasks, assigns priorities, and generates a readable
to-do list.

## Workflow

1. Task Extraction
   - Identifies actionable tasks from user input.
   - Preserves explicitly stated due-date phrases.

2. Task Prioritization
   - Assigns High, Medium, or Low priority.
   - Preserves extracted task titles and due dates.

3. Format Results
   - Produces an organized to-do list.
   - Displays task priorities and available due dates.

## Technology Stack

- Python
- LangGraph
- LangChain Groq
- Groq API
- Pydantic
- python-dotenv
- pytest

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

   `python -m pip install -r requirements.txt`

3. Add your Groq API key and model ID to `.env`.
4. Run the application:

   `python main.py`

## Run Tests

`python -m pytest -q`

## Security

Never commit `.env` or expose your API key.

## Current Scope

This version processes tasks in a sequential three-node workflow.
It does not persist tasks between application sessions.
A graphical interface can be added as a separate layer.