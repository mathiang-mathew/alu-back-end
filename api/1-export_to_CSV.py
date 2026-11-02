#!/usr/bin/python3
"""Export an employee's TODO list to CSV format.

Usage:
    python3 1-export_to_CSV.py <employee_id>
"""
import csv
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


def export_to_csv(employee_id):
    """Write the employee's TODO list to USER_ID.csv."""
    username = get_employee_name(employee_id)
    todos = get_employee_todos(employee_id)

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
