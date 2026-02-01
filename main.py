import json
import os
from datetime import datetime

FILENAME = "tasks.json"

data_structure = {
    "tasks": {
        "completed": [],
        "incomplete": [],
        "inProgress": []
        }
        
    }

def is_file_exist(file):
    """
    Check if file exists

    Args:
        file (str): file's name

    Returns:
        bool: True if file exists, False otherwise
    """
    return os.path.exists(file)

def is_file_empty(file):
    """
    Checks if file is empty.

    Args:
        file (str): file's namedi

    Returns:
        bool: True if file is empty, False otherwise
    """
    if not is_file_exist(file):
        return True


if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
    with open(FILENAME, "w") as f:
        json.dump(data_structure, f)

def get_next_id(data):
    cur_id = data['tasks']['nextId']
    data['tasks']['nextId'] += 1
    return cur_id

def get_time():
    now = datetime.now().strftime("%Y-%m-%d || %H:%M")
    print(now)

def add_task(description):
    """
    Create a task and 
    """

    with open(FILENAME, "r") as f:
        data = json.load(f)



    data["tasks"]["incomplete"].append(
        {
            "id": get_next_id(data),
            "description": description,
            'status': "Todo",
            'createdAt': get_time(),
            'updatedAt': None
        }  
    )
    task_id = 1
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def update_task(id, desc):
    """
    Find task by ID and update its description.
    
    Args:
        id (int) - Task's unique ID 
        desc (str) - New task description.

    Returns:
        bool: True if the task was found and updated, False otherwise.
    """
    pass

def delete_task(id):
    """
    Delete task by task's unique ID

    Returns True if found and deleted, False otherwise.
    """

    pass



add_task("Accumalte a total of 20 million php asset in 10 years")
