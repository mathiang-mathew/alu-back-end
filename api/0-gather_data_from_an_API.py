#!/usr/bin/python3
"""Gather data from a REST API and display an employee's TODO progress.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee_name(employee_id):
    """Return the name of the employee with the given id."""
    response = requests.get("{}/users/{}".format(BASE_URL, employee_id))
    user = response.json()
    return user.get("name")


def get_employee_todos(employee_id):
    """Return the full list of TODO items for the given employee id."""
    response = requests.get(
        "{}/todos".format(BASE_URL),
        params={"userId": employee_id}
    )
    return response.json()


def display_progress(employee_id):
    """Print the employee's TODO progress in the required format."""
    name = get_employee_name(employee_id)
    todos = get_employee_todos(employee_id)

    done_tasks = [task for task in todos if task.get("completed")]
    total = len(todos)
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_progress(employee_id)
