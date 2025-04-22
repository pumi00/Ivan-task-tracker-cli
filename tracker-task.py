import sys
import json
import os
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task: 

        # This is a method to run a new instance of the task class
        # The first line is a default parameter if dont sent any valor, it wil be used task.json
        # The second line save the file name
        # The third line use method loading_task and save the result in self.task

    def __init__(self, file_json="task.json"):
        self.file_json = file_json
        self.task = self.loading_task()

        

        # Use method try and except to check if the file exists
        # If the JSON file exist open archive in read mode and save the result in f
        # Read the archive and convert to Python data type
        # return[] never is used because return json.load(f) was finished to function yet
        # If the JSON file does not exist, create a new one

    def loading_task(self):
        try:
            if os.path.exists(self.file_json):
                with open(self.file_json, 'r') as f:
                    return json.load(f)
                return[]

        except (json.JSONDecodeError, IOError):
            print("Error loading task file. Creating a new one.")
            return []