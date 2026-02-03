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
                

                with open(FILENAME, "w") as file:
                    json.dump(data, file, indent=4)
                    return True

        return False


def delete_task(sid):
    with open(FILENAME, "r") as file:
        data = json.load(file)

    lists_to_check = [
        data["tasks"]["completed"],
        data["tasks"]["incomplete"],
        data["tasks"]["inProgress"]
    ]

    for task_list in lists_to_check:
        for idx, task in enumerate(task_list):
            if task['id'] == sid:
                del task_list[idx]  # ← deletes from ORIGINAL list
                with open(FILENAME, 'w') as file:
                    json.dump(data, file, indent=4)
                return True
    return False


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

def list_tasks(data) -> None:
    for index, task in enumerate(data, start=1):
        print(
            f"{index}. ID: {task['id']:<3}||"
            f"{task['description']:<65}||"
            f"{task['status']:^11}||"
            f"{task['createdAt']:^11}||"
            f"{task['updatedAt']:^11}||"
        )


def get_specific_tasks(key):
    with open(FILENAME, "r") as file:
        data = json.load(file)
        
        tasks = data['tasks'][key]

        tlist = []

        for task in tasks:
            tlist.append(task)


# Not sure what to do with this one.
def find_task(task_id: int, data: dict) -> dict:
    for item in data:
        if item["id"] == task_id:
            return item
        return False

def mark_task(task_id: int, new_status:str) -> None:
    with open(FILENAME, "r") as file:
        data = json.load(file)
        tasks = (
            data["tasks"]["incomplete"]
            + data["tasks"]["inProgress"]
            + data["tasks"]["completed"]
        )

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status


                with open(FILENAME, "w") as file:
                    json.dump(data, file, indent=4)
                    return True

        return False


def main():
    print(
        "Welcome to  Task Tracker (CLI)"
        "\nActions:"
        "\n1. Add task"  # done
        "\n2. Update task" # done
        "\n3. Delete task" # done
        "\n4. Mark task as done" #done
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
            list_tasks()

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

        case 3:
            print("Type the ID of the task you want to delete.")
            tid = int(input("Task ID: "))
            deleted = delete_task(tid)

            if deleted:
                print(f"Deleted successfully")
            else:
                print("Invalid id")

        case 4:
            print("Type the ID of the task you want to mark as done/inprogress.")
            tid = int(input("Task ID: "))
            new_status = int(input(
                'Type 1 to mark as "DONE"'
                '\nType 2 to mark as "INPROGRESS\n'
                ))

            if new_status == 1:
                new_status = "Done"
            elif new_status == 2:
                new_status = "INPROGRESS"

            if mark_task(tid, new_status):
                print(
                    f"Mark task with the ID of: {tid}"
                    f"\nNew task status: {new_status}"
                    )
            else:
                print(
                    f"Invalid ID!"
                    f"\nNo task was found with the id of {tid}"
                )

        case 5:
            list_tasks(get_tasks())

main()