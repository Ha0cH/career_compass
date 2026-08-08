from src.application_service import ApplicationService
from datetime import date
from src.application import ApplicationStatus, WorkMode
import os

def test_add_application():
    service = ApplicationService(data_file_path="test_applications.json")
    
    new_app = service.add_application(
        company="Test Company",
        position="Test Position",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED,
        location="Test Location",
        work_mode=WorkMode.REMOTE,
        url="http://testurl.com",
        notes="Test notes"
    )
    
    assert new_app.application_id == 1
    assert new_app.company == "Test Company"
    assert new_app.position == "Test Position"
    assert new_app.location == "Test Location"
    assert new_app.work_mode == WorkMode.REMOTE
    assert new_app.status == ApplicationStatus.APPLIED
    assert new_app.url == "http://testurl.com"
    assert new_app.notes == "Test notes"

    assert service.applications[-1] == new_app 

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_add_multiple_applications():
    service = ApplicationService(data_file_path="test_applications.json")
    
    app1 = service.add_application(
        company="Company 1",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    app2 = service.add_application(
        company="Company 2",
        position="Position 2",
        date_applied=date.today(),
        status=ApplicationStatus.INTERVIEW
    )
    
    assert app1.application_id == 1
    assert app2.application_id == 2
    assert len(service.applications) == 2

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_get_all_applications():
    service = ApplicationService(data_file_path="test_applications.json")
    
    service.add_application(
        company="Company 1",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    service.add_application(
        company="Company 2",
        position="Position 2",
        date_applied=date.today(),
        status=ApplicationStatus.INTERVIEW
    )
    
    all_apps = service.get_all_applications()
    assert len(all_apps) == 2

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_find_application_by_id():
    service = ApplicationService(data_file_path="test_applications.json")
    
    app1 = service.add_application(
        company="Company 1",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    found_app = service.find_application_by_id(app1.application_id)
    assert found_app is not None
    assert found_app.application_id == app1.application_id

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_delete_application():
    service = ApplicationService(data_file_path="test_applications.json")
    
    app1 = service.add_application(
        company="Company 1",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    deleted = service.delete_application(app1.application_id)
    assert deleted is True
    assert service.find_application_by_id(app1.application_id) is None

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_delete_nonexistent_application():
    service = ApplicationService(data_file_path="test_applications.json")
    
    deleted = service.delete_application(999)  # Assuming 999 is a non-existent ID
    assert deleted is False

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_update_application():
    service = ApplicationService(data_file_path="test_applications.json")
    
    app1 = service.add_application(
        company="Company 1",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    updated_app_success = service.update_application(
        application_id=app1.application_id,
        company="Updated Company",
        position="Updated Position",
        status=ApplicationStatus.INTERVIEW,
        notes="Updated notes"
    )
    
    assert updated_app_success == True
    assert app1.company == "Updated Company"
    assert app1.position == "Updated Position"
    assert app1.status == ApplicationStatus.INTERVIEW
    assert app1.notes == "Updated notes"

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_update_nonexistent_application():
    service = ApplicationService(data_file_path="test_applications.json")
    
    updated_app_success = service.update_application(
        application_id=999,  # Assuming 999 is a non-existent ID
        company="Updated Company"
    )
    
    assert updated_app_success == False

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_search_by_company():
    service = ApplicationService(data_file_path="test_applications.json")
    
    service.add_application(
        company="Company A",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    service.add_application(
        company="Company B",
        position="Position 2",
        date_applied=date.today(),
        status=ApplicationStatus.INTERVIEW
    )
    
    service.add_application(
        company="Company A",
        position="Position 3",
        date_applied=date.today(),
        status=ApplicationStatus.OFFER
    )
    
    results = service.search_by_company("Company A")
    assert len(results) == 2
    for app in results:
        assert app.company == "Company A"

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_search_nonexistent_company():
    service = ApplicationService(data_file_path="test_applications.json")
    
    service.add_application(
        company="Company A",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    results = service.search_by_company("Nonexistent Company")
    assert len(results) == 0

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")


def test_filter_by_status():
    service = ApplicationService(data_file_path="test_applications.json")
    
    service.add_application(
        company="Company A",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    service.add_application(
        company="Company B",
        position="Position 2",
        date_applied=date.today(),
        status=ApplicationStatus.INTERVIEW
    )
    
    service.add_application(
        company="Company C",
        position="Position 3",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    results = service.filter_by_status(ApplicationStatus.APPLIED)
    assert len(results) == 2
    for app in results:
        assert app.status == ApplicationStatus.APPLIED

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_get_statistics():
    service = ApplicationService(data_file_path="test_applications.json")
    
    service.add_application(
        company="Company A",
        position="Position 1",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    service.add_application(
        company="Company B",
        position="Position 2",
        date_applied=date.today(),
        status=ApplicationStatus.INTERVIEW
    )
    
    service.add_application(
        company="Company C",
        position="Position 3",
        date_applied=date.today(),
        status=ApplicationStatus.APPLIED
    )
    
    stats = service.get_statistics()
    assert stats["total_applications"] == 3
    assert stats["status_counts"][ApplicationStatus.APPLIED.value] == 2
    assert stats["status_counts"][ApplicationStatus.INTERVIEW.value] == 1

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")

def test_get_statistics_empty():
    service = ApplicationService(data_file_path="test_applications.json")
    
    stats = service.get_statistics()
    assert stats["total_applications"] == 0
    for status in ApplicationStatus:
        assert stats["status_counts"][status.value] == 0

    # Clean up the test data file after the test
    if os.path.exists("test_applications.json"):
        os.remove("test_applications.json")