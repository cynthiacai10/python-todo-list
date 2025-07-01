import json
import os


TODO_FILE = "todo_list.json"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
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

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                add_task(tasks, title)
        elif choice == "3":
            list_tasks(tasks)
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(tasks, index)
        elif choice == "4":
            list_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
