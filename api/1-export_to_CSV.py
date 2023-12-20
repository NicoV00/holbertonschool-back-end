#!/usr/bin/python3
""" Task 1 """


import csv
import requests
import sys


def write_file(filename="", rows=None):
    """ Write file """
    with open(filename, mode="a", encoding="utf-8", newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(rows)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Enter a valid number")
        sys.exit()

    UserID = sys.argv[1]

    userTasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{UserID}/todos').json()
    userInfo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{UserID}').json()

    userName = userInfo.get('username')
    rows = []
    for task in userTasks:
        row = [UserID, userName, task.get('completed'), task.get('title')]
        rows.append(row)

    write_file(f"{UserID}.csv", rows)
