import json
import os


def load_tasks(todo_file):
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as f:
        return json.load(f)


def save_tasks(tasks, todo_file):
    with open(todo_file, "w") as f:
        json.dump(tasks, f, indent=2)


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour TODO List:")
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        print(f"{i + 1}. [{status}] {task['title']}")


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    print(f"Added task: {title}")


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked task {index + 1} as done.")
    else:
        print("Invalid task number.")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")


def show_menu():
    print("\n--- TODO Menu ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")
