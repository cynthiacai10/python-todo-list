import json
import os
import pytest


from app.utils import load_tasks, save_tasks, add_task, list_tasks, mark_done, delete_task


'''
def test_add_task():
    tasks = []
    add_task(tasks, "Test item")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test item"
    assert tasks[0]["done"] is False
'''


def test_load_tasks_file_not_exist(tmp_path):
    todo_file = tmp_path / "non_existent.json"
    assert load_tasks(todo_file) == []


def test_load_tasks_file_exists(tmp_path):
    todo_file = tmp_path / "todo.json"
    data = [{"title": "Sample task", "done": False}]
    todo_file.write_text(json.dumps(data))
    assert load_tasks(todo_file) == data


def test_save_tasks_creates_file(tmp_path):
    todo_file = tmp_path / "todo.json"
    data = [{"title": "Write tests", "done": True}]
    save_tasks(data, todo_file)
    assert todo_file.exists()
    assert json.loads(todo_file.read_text()) == data


def test_add_task_adds_correctly():
    tasks = []
    add_task(tasks, "Buy milk")
    assert tasks == [{"title": "Buy milk", "done": False}]


def test_list_tasks_empty(capfd):
    list_tasks([])
    out, _ = capfd.readouterr()
    assert "No tasks found" in out


def test_list_tasks_nonempty(capfd):
    tasks = [{"title": "Do laundry", "done": False}, {"title": "Read book", "done": True}]
    list_tasks(tasks)
    out, _ = capfd.readouterr()
    assert "Your TODO List" in out
    assert "1. [❌] Do laundry" in out
    assert "2. [✅] Read book" in out


def test_mark_done_valid_index(capfd):
    tasks = [{"title": "Task 1", "done": False}]
    mark_done(tasks, 0)
    assert tasks[0]["done"] is True
    out, _ = capfd.readouterr()
    assert "Marked task 1 as done." in out


def test_mark_done_invalid_index(capfd):
    tasks = [{"title": "Task 1", "done": False}]
    mark_done(tasks, 5)
    assert tasks[0]["done"] is False
    out, _ = capfd.readouterr()
    assert "Invalid task number." in out


def test_delete_task_valid_index(capfd):
    tasks = [{"title": "Task A", "done": False}, {"title": "Task B", "done": False}]
    delete_task(tasks, 0)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task B"
    out, _ = capfd.readouterr()
    assert "Deleted task: Task A" in out

def test_delete_task_invalid_index(capfd):
    tasks = [{"title": "Task A", "done": False}]
    delete_task(tasks, 2)
    assert len(tasks) == 1
    out, _ = capfd.readouterr()
    assert "Invalid task number." in out
