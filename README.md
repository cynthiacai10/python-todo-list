# CLI Todo List App

**Version:** 0.1.0  
**Author:** Cynthia

A simple command-line todo list program written in Python to help you manage your tasks easily.

## Features

The features include:

1. Add new tasks
2. List all tasks
3. Mark tasks as done
4. Delete tasks
5. Save tasks in a JSON file (persistent)


## Requirements

- Python 3.9
- [Poetry](https://python-poetry.org/) for dependency and environment management

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/cynthiacai10/python-todo-list
   cd python-todo-list
   ```

2. Install dependencies and create a virtual environment with Poetry:
   
    ```poetry install```


## Usage

1. Run the program inside the Poetry environment:

    ```poetry run python -m app.cli```

2. The program will display a menu that has five options.
3. Enter your choice and follow the prompts to manage your todo list.


## Example

1. List tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit

Enter your choice: 2

Enter task title: Buy groceries

Task added.

----

Enter your choice: 1
1. [ ] Buy groceries

Enter your choice: 3

Enter task number to mark as done: 1

Task marked as done.

---

Enter your choice: 5

Goodbye!


## Notes

Tasks are saved in data/todo_list.json.

The program automatically creates the data directory and JSON file if they don’t exist.

## Roadmap / TODO

- Add new feature: editing tasks
- Use Black for automatic code formatting
- Use Flake8 for linting and style checks
- Implement a database backend for better task storage and scalability
- Develop a web frontend to manage tasks through a browser interface