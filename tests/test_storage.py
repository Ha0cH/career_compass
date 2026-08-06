from src.storage import save_applications, load_applications, DATA_FILE_PATH
from src.application import Application, ApplicationStatus, WorkMode
from datetime import date
import os
import shutil

def test_save_applications_and_load_applications():
    applications = [
        Application(
            application_id=1,
            company="Company A",
            position="Position A",
            date_applied=date(2023, 1, 1),
            status=ApplicationStatus.APPLIED,
        ),
        Application(
            application_id=2,
            company="Company B",
            position="Position B",
            date_applied=date(2023, 2, 1),
            status=ApplicationStatus.INTERVIEW,
            location = "Location B",
            work_mode = WorkMode.REMOTE,
        ),
    ]
    save_applications(applications)

    loaded_applications = load_applications()
    assert len(loaded_applications) == 2
    assert loaded_applications[0].application_id == 1
    assert loaded_applications[0].company == "Company A"
    assert loaded_applications[0].position == "Position A"
    assert loaded_applications[0].date_applied == date(2023, 1, 1)
    assert loaded_applications[0].status == ApplicationStatus.APPLIED

    assert loaded_applications[1].application_id == 2
    assert loaded_applications[1].company == "Company B"
    assert loaded_applications[1].position == "Position B"
    assert loaded_applications[1].date_applied == date(2023, 2, 1)
    assert loaded_applications[1].status == ApplicationStatus.INTERVIEW
    assert loaded_applications[1].location == "Location B"
    assert loaded_applications[1].work_mode == WorkMode.REMOTE

    #clean up the data file after the test
    save_applications([]) # Reset the file to an empty list

def test_load_applications_file_not_found():
    # Ensure that the function returns an empty list when the file does not exist
    loaded_applications = load_applications("non_existent_file.json")
    assert loaded_applications == []

    #clean up the test file after the test
    if os.path.exists("non_existent_file.json"):
        os.remove("non_existent_file.json")

def test_save_applications_creates_file():
    applications = [
        Application(
            application_id=1,
            company="Company C",
            position="Position C",
            date_applied=date(2023, 3, 1),
            status=ApplicationStatus.OFFER,
        )
    ]
    file_path = "test_data/applications_test.json"
    save_applications(applications, file_path)

    # Check if the file was created
    assert os.path.exists(file_path)

    # Clean up the test file after the test
    if os.path.exists("test_data"):
        shutil.rmtree("test_data")

def test_save_empty_applications_file():
    # Save an empty list of applications to the default file path
    save_applications([])

    loaded = load_applications()
    assert loaded == []  # The loaded list should be empty
