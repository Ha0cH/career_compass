from datetime import date
import pytest
from src.application import Application, ApplicationStatus, WorkMode

def test_create_valid_application():
    application = Application(
        application_id=1,
        company="Shopify",
        position="Software Developer Intern",
        date_applied=date(2026, 8, 3),
        status=ApplicationStatus.APPLIED,
        location="Calgary",
        work_mode=WorkMode.REMOTE,
    )

    assert application.application_id == 1
    assert application.company == "Shopify"
    assert application.position == "Software Developer Intern"
    assert application.date_applied == date(2026, 8, 3)
    assert application.status is ApplicationStatus.APPLIED
    assert application.location == "Calgary"
    assert application.work_mode is WorkMode.REMOTE
    assert application.url is None
    assert application.notes is None

def test_invalid_application_id_raises_value_error():
    with pytest.raises(ValueError):
        Application(
            application_id=-1,
            company="Shopify",
            position="Software Developer Intern",
            date_applied=date(2026, 8, 3),
            status=ApplicationStatus.APPLIED,
            location="Calgary",
            work_mode=WorkMode.REMOTE,
        )

def test_blank_company_raises_value_error():
    with pytest.raises(ValueError):
        Application(
            application_id=1,
            company="",
            position="Software Developer Intern",
            date_applied=date(2026, 8, 3),
            status=ApplicationStatus.APPLIED,
            location="Calgary",
            work_mode=WorkMode.REMOTE,
        )

def test_blank_position_raises_value_error():
    with pytest.raises(ValueError):
        Application(
            application_id=1,
            company="Shopify",
            position="",
            date_applied=date(2026, 8, 3),
            status=ApplicationStatus.APPLIED,
            location="Calgary",
            work_mode=WorkMode.REMOTE,
        )

def test_invalid_date_raises_type_error():
    with pytest.raises(TypeError):
        Application(
            application_id=2,
            company="Apple",
            position="Junior Software Developer",
            date_applied="2026-08-03",
            status=ApplicationStatus.APPLIED,
            work_mode=WorkMode.REMOTE,
        )

def test_invalid_status_raises_type_error():
    with pytest.raises(TypeError):
        Application(
            application_id=3,
            company="Apple",
            position="Junior Software Developer",
            date_applied=date(2026, 8, 3),
            status="Applied",
            work_mode=WorkMode.REMOTE,
        )

def test_invalid_work_mode_raises_type_error():
    with pytest.raises(TypeError):
        Application(
            application_id=4,
            company="Apple",
            position="Junior Software Developer",
            date_applied=date(2026, 8, 3),
            status=ApplicationStatus.APPLIED,
            work_mode="Remote",
        )

def test_to_dict():
    application = Application(
        application_id=3,
        company="Netflix",
        position="Senior Software Developer",
        date_applied=date(2026, 8, 3),
        status=ApplicationStatus.APPLIED,
        work_mode=WorkMode.ON_SITE,
        location="Vancouver"
    )

    result = application.to_dict()

    assert result == {
        "application_id": 3,
        "company": "Netflix",
        "position": "Senior Software Developer",
        "location": "Vancouver",
        "work_mode": "On-site",
        "date_applied": "2026-08-03",
        "status": "Applied",
        "url": None,
        "notes": None 
    }

def test_from_dict():
    data = {
        "application_id": 4,
        "company": "Google",
        "position": "Software Engineer",
        "location": "Toronto",
        "work_mode": "Hybrid",
        "date_applied": "2026-08-03",
        "status": "Applied",
        "url": None,
        "notes": None
    }

    application = Application.from_dict(data)

    assert application.application_id == 4
    assert application.company == "Google"
    assert application.position == "Software Engineer"
    assert application.location == "Toronto"
    assert application.work_mode == WorkMode.HYBRID
    assert application.date_applied == date(2026, 8, 3)
    assert application.status == ApplicationStatus.APPLIED
    assert application.url == None
    assert application.notes == None

def test_from_dict_and_to_dict_roundtrip():
    data = {
        "application_id": 6,
        "company": "Amazon",
        "position": "Backend Developer",
        "location": "Seattle",
        "work_mode": "Remote",
        "date_applied": "2026-08-03",
        "status": "Applied",
        "url": None,
        "notes": None
    }

    application = Application.from_dict(data)
    result = application.to_dict()

    assert result == data

def test_to_dict_and_from_dict_roundtrip():
    original = Application(
        application_id=7,
        company="Microsoft",
        position="Frontend Developer",
        date_applied=date(2026, 8, 3),
        status=ApplicationStatus.APPLIED,
        work_mode=WorkMode.HYBRID,
        location="Seattle"
    )
    new_application = Application.from_dict(original.to_dict())

    assert new_application.application_id == original.application_id
    assert new_application.company == original.company
    assert new_application.position == original.position
    assert new_application.location == original.location
    assert new_application.work_mode == original.work_mode
    assert new_application.date_applied == original.date_applied
    assert new_application.status == original.status
    assert new_application.url == original.url
    assert new_application.notes == original.notes
    