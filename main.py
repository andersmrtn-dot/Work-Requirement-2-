"""
main.py - Task List Manager
Interactively manage a task list using the tasks module.
Commands:
  add <task>     - Add a task to the list
  remove <task>  - Remove a task from the list
  done           - Exit the program
"""

import tasks  # Import the separate tasks module


def print_task_list(task_list):
    """Display the current task list in a formatted way."""
    print("\n" + "─" * 40)
    print("  📋 Current Task List:")
    print("─" * 40)
    if not task_list:
        print("  (no tasks yet)")
    else:
        for i, task in enumerate(task_list, start=1):
            print(f"  {i}. {task}")
    print("─" * 40 + "\n")


def print_banner():
    """Print a welcome banner."""
    print("=" * 40)
    print("      ✅  TASK LIST MANAGER  ✅")
    print("=" * 40)
    print("Commands:")
    print("  add <task>     → Add a new task")
    print("  remove <task>  → Remove a task")
    print("  done           → Exit")
    print("=" * 40 + "\n")


def main():
    task_list = []  # Start with an empty list
    print_banner()
    print_task_list(task_list)

    while True:
        try:
            user_input = input("Enter command: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Goodbye!")
            break

        if not user_input:
            print("  ⚠️  Please enter a command (add / remove / done).")
            continue

        # Exit condition
        if user_input.lower() == "done":
            print("\n✅ Final task list saved. Goodbye!")
            print_task_list(task_list)
            break

        # Parse command and task name
        parts = user_input.split(" ", 1)
        command = parts[0].lower()

        if command == "add":
            if len(parts) < 2 or not parts[1].strip():
                print("  ⚠️  Usage: add <task name>")
                continue
            task_list = tasks.add_task(task_list, parts[1])
            print_task_list(task_list)

        elif command == "remove":
            if len(parts) < 2 or not parts[1].strip():
                print("  ⚠️  Usage: remove <task name>")
                continue
            task_list = tasks.remove_task(task_list, parts[1])
            print_task_list(task_list)

        else:
            print(f"  ❓ Unknown command '{command}'. Use: add / remove / done")


if __name__ == "__main__":
    main()
