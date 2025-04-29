import sys
import json
import os
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task: 

    # This is a method to run a new instance of the task class.
    # The first line is a default parameter if dont sent any valor, it wil be used task.json.
    # The second line save the file name.
    # The third line use method loading_task and save the result in self.task.

    def __init__(self, file_json="task.json"):
        self.file_json = file_json
        self.task = self.loading_task()



    # Use method try and except to check if the file exists.
    # If the JSON file exist open archive in read mode ('r') and save the result in f.
    # Here we use the read mode because in the loading_task only read the file.
    # Read the archive and convert to Python data type.
    # return[] never is used because return json.load(f) was finished to function yet.
    # If the JSON file does not exist, create a new one.

    def loading_task(self):
        try:
            if os.path.exists(self.file_json):
                with open(self.file_json, 'r') as f:
                    return json.load(f)
                return[]

        except (json.JSONDecodeError, IOError):
            print("Error loading task file. Creating a new one.")
            return []
        

        
    # Try to open the file in write mode ('w') and save the result in f.
    # If the file does exits, it will be overwritten if doesnt exist, it will be created.
    # Use the json.dump to convert the Python data type to JSON and save in f.
    # indent=2 is used to make the JSON file more readable.
    # And IOError is a error in python that occurs when an input/outpu operation fails.
    def save_task(self):
        try:
            with open(self.file_json, 'w') as f:
                json.dump(self.task, f, indent=2)

        except IOError:
            print("Error saving task file.")



    # Define a method to add a task and use one parameter description.
    # Create a new task with id, description and status.
    # The id will be added 1 to the lenght of the task list.
    # In status use a parameter for check the status that is pending.
    # Use append to add the new task in new_task.
    # Save the task.
    def add_task(self, description):
        new_task = {
            "id": len(self.task) + 1,
            "description": description,
            "status": TaskStatus.PENDING.value,
            "createdAt": now,
            "updateAt": now
        }
        self.task.append(new_task)
        self.save_task()
        print(f"Task added: {new_task['id']} - {description}") 



    # This method is used to update the especific task in the task list.
    # Later we use task_id for get the task when you want to change the description and new_decription for the new description.
    # In for loop we check and iterate the task lists in self.task.
    # Check if the task id is equal to the task_id.
    # Update the updateAt with the current date and time.
    # Save the task.
    def update_task(self, task_id, new_description):
        for task in self.task:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updateAt"] = datetime.now().isoformat()
                self.save_task()
                print(f"Task {task_id} update.")
                return
            print("Task not found.")

    
    
    
    def delete_task(self, task_id, status):
        original_task = len(self.task)
        self.task = [task for task in self.task if task[id] != task_id]
        if len(self.task) < original_task:
            self.save_task()
            

