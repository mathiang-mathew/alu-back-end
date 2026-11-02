#!/usr/bin/python3
"""Export all employees' TODO lists into a single JSON file.

Usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_users():
    """Return the list of all users."""
    response = requests.get("{}/users".format(BASE_URL))
    return response.json()


def get_all_todos():
    """Return the list of all TODO items, for every user."""
    response = requests.get("{}/todos".format(BASE_URL))
    return response.json()


def export_all_to_json():
    """Write every employee's TODO list to todo_all_employees.json."""
    users = get_all_users()
    todos = get_all_todos()

    usernames = {}
    for user in users:
        usernames[str(user.get("id"))] = user.get("username")

    all_tasks = {}
    for user_id in usernames:
        all_tasks[user_id] = []

    for task in todos:
        user_id = str(task.get("userId"))
        username = usernames.get(user_id)
        all_tasks.setdefault(user_id, []).append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
