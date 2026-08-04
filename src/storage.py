import os
import json
from .application import Application

DATA_FILE_PATH = "data/applications.json"

# save the updated/current list to json file
def save_applications(applications: list[Application], file_path: str = DATA_FILE_PATH) -> None:
    # the list of applications is a complete list of Application objects, so we just need to convert them to dictionaries before saving them to a file

    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    converted_list = [application.to_dict() for application in applications]

    with open(file_path, "w") as file:
        json.dump(converted_list, file, indent=4)  # indent=4 for better readability of the JSON file

# here is the stored list
def load_applications(file_path: str = DATA_FILE_PATH) -> list[Application]:
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        with open(file_path, "r") as file:
            list_of_application_dictionaries = json.load(file)
    except FileNotFoundError: #no file found/no applications yet, create a new one and return an empty list
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)
        return []

    return [Application.from_dict(app_dict) for app_dict in list_of_application_dictionaries]