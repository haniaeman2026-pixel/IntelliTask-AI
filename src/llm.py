import os

from langchain_groq import ChatGroq


def get_llm() -> ChatGroq:
    """Create the configured Groq chat model."""
    api_key = os.getenv("GROQ_API_KEY")
    model_name = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-20b",
    )

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add your Groq API key to the .env file."
        )

    return ChatGroq(
        model=model_name,
        api_key=api_key,
        temperature=0,
        max_retries=2,
        timeout=60,
    )