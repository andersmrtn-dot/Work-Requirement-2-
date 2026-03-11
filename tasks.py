"""
tasks.py - Task management module
Provides functions to add and remove tasks from a task list.
"""


def add_task(task_list, task):
    """
    Add a task to the task list.

    Args:
        task_list (list): The current list of tasks.
        task (str): The task to add.

    Returns:
        list: The updated task list.
    """
    task = task.strip()
    if not task:
        print("  ⚠️  Task cannot be empty.")
        return task_list

    if task in task_list:
        print(f"  ⚠️  Task '{task}' already exists in the list.")
        return task_list

    task_list.append(task)
    print(f"  ✅ Task '{task}' added successfully.")
    return task_list


def remove_task(task_list, task):
    """
    Remove a task from the task list.

    Args:
        task_list (list): The current list of tasks.
        task (str): The task to remove.

    Returns:
        list: The updated task list.
    """
    task = task.strip()
    if not task:
        print("  ⚠️  Task name cannot be empty.")
        return task_list

    if task not in task_list:
        print(f"  ❌ Task '{task}' not found in the list.")
        return task_list

    task_list.remove(task)
    print(f"  🗑️  Task '{task}' removed successfully.")
    return task_list
