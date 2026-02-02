import json
import os
from datetime import datetime

FILENAME = "tasks.json"


def get_next_id(data):
    cur_id = data["tasks"]["nextId"]
    data["tasks"]["nextId"] += 1
    return cur_id


def get_time():
    return datetime.now().strftime("%Y-%m-%d  %H:%M")


def add_task(description):
    """
    You gotta do what you gotta do ya heard
    """

    with open(FILENAME, "r") as f:
        data = json.load(f)

    data["tasks"]["incomplete"].append(
        {
            "id": get_next_id(data),
            "description": description,
            "status": "Todo",
            "createdAt": get_time(),
            "updatedAt": "N/A",
        }
    )

    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def update_task(task_id: int, desc: str) ->  bool:
    """
    Find task by ID and update its description.

    Args:
        id (int) - Task's unique ID
        desc (str) - New task description.

    Returns:
        bool: True if the task was found and updated, False otherwise.
    """

    with open(FILENAME, "r") as file:
        data = json.load(file)
        tasks = (
            data["tasks"]["incomplete"]
            + data["tasks"]["inProgress"]
            + data["tasks"]["completed"]
        )

        for task in tasks:
            if task["id"] == task_id:
                task["description"] = desc
                print(task_id)

                with open(FILENAME, "w") as file:
                    json.dump(data, file, indent=4)
                    return True

        return False


def delete_task(id):
    """
    Delete task by task's unique ID

    Returns True if found and deleted, False otherwise.
    """

    pass


def get_tasks():
    with open(FILENAME, "r") as file:
        data = json.load(file)
        tasks = (
            data["tasks"]["incomplete"]
            + data["tasks"]["inProgress"]
            + data["tasks"]["completed"]
        )
        tlist = []

        for task in tasks:
            tlist.append(task)

    return tlist

# Not sure what to do with this one.
def find_task(task_id: int, data: dict) -> dict:
    for item in data:
        if item["id"] == task_id:
            return item
        return False


def main():
    print(
        "Welcome to  Task Tracker (CLI)"
        "\nActions:"
        "\n1. Add task"  # done
        "\n2. Update task"
        "\n3. Delete task"
        "\n4. Mark task as done"
        "\n5. View ALL tasks"  # done
        "\n6. View COMPLETED tasks"
        "\n7. View INCOMPLETE tasks"
        "\n8. View IN-PROGRESS tasks"
    )

    action = int(input("Type 1-8: "))

    match action:
        case 1:
            tdesc = input("Task description: ")
            add_task(tdesc)

        case 2:
            print("Type the ID of the task you want to update.")
            tid = int(input("Task ID: "))
            new_desc = input("New task description: ")
            if update_task(tid, new_desc):
                print(
                    f"Updated task with the ID of: {tid}"
                    f"\nNew task description: {new_desc}"
                    )
            else:
                print(
                    f"Invalid ID!"
                    f"\nNo task was found with the id of {tid}"
                )

        case 5:
            for index, task in enumerate(get_tasks(), start=1):
                print(
                    f"{index}. ID: {task['id']:<3}||"
                    f"{task['description']:<65}||"
                    f"{task['status']:^11}||"
                    f"{task['createdAt']:^11}||"
                    f"{task['updatedAt']:^11}||"
                )


main()
