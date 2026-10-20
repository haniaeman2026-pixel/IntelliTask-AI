from dotenv import load_dotenv

from src.graph import task_graph


def main() -> None:
    """Run IntelliTask AI from the command line."""
    load_dotenv()

    print("\n" + "=" * 44)
    print("          INTELLITASK AI")
    print("  Intelligent Task Management Assistant")
    print("=" * 44)
    print("Describe your tasks in a single sentence.")
    print("Type 'exit' to close the application.\n")

    while True:
        try:
            user_input = input("Your tasks: ").strip()

            if user_input.lower() in {"exit", "quit"}:
                print("Thank you for using IntelliTask AI.")
                break

            if not user_input:
                print("Please enter at least one task.\n")
                continue

            result = task_graph.invoke({
                "user_input": user_input,
                "tasks": [],
                "formatted_results": "",
            })

            print("\n" + result["formatted_results"])
            print()

        except (KeyboardInterrupt, EOFError):
            print("\nApplication closed.")
            break

        except Exception as error:
            print(f"\nUnable to process your request: {error}")
            print(
                "Check your Groq API key, model ID, "
                "internet connection, and API access.\n"
            )


if __name__ == "__main__":
    main()