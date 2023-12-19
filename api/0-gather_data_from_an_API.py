#!/usr/bin/python3
""" Task 0 """


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Enter a valid number")
        sys.exit()

    taskId = sys.argv[1]

    user_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{taskId}/todos').json()
    user_info = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{taskId}').json()

    user_name = user_info.get('name')
    completed_tasks = [todo for todo in user_tasks if todo['completed']]
    print(f"Employee {user_name} is done with"
          " tasks({len(completed_tasks)}/{len(user_tasks)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
        