#!/usr/bin/python3
"""Export an employee's TODO list to JSON format.

Usage:
    python3 2-export_to_JSON.py <employee_id>
"""
import json
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee_name(employee_id):
    """Return the username of the employee with the given id."""
    response = requests.get("{}/users/{}".format(BASE_URL, employee_id))
    user = response.json()
    return user.get("username")


def get_employee_todos(employee_id):
    """Return the full list of TODO items for the given employee id."""
    response = requests.get(
        "{}/todos".format(BASE_URL),
        params={"userId": employee_id}
    )
    return response.json()


def export_to_json(employee_id):
    """Write the employee's TODO list to USER_ID.json."""
    username = get_employee_name(employee_id)
    todos = get_employee_todos(employee_id)

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
