import json
import os

from .utils import load_tasks, save_tasks, list_tasks
from .utils import add_task, mark_done, delete_task, show_menu


def main():
    # Define data folder path
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)

    # Define todo json file path
    todo_file = os.path.join(data_dir, "todo_list.json")
    if not os.path.exists(todo_file):
        with open(todo_file, "w") as f:
            json.dump([], f)

    tasks = load_tasks(todo_file)
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
            save_tasks(tasks, todo_file)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()