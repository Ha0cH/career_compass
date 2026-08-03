from datetime import date
from enum import Enum


class ApplicationStatus(Enum):
    APPLIED = "Applied"
    OA = "OA"
    PHONE_SCREEN = "Phone Screen"
    INTERVIEW = "Interview"
    REJECTED = "Rejected"
    OFFER = "Offer"
    ACCEPTED = "Accepted"
    WITHDRAWN = "Withdrawn"


class WorkMode(Enum):
    REMOTE = "Remote"
    HYBRID = "Hybrid"
    ON_SITE = "On-site"


class Application:
    def __init__(
            self, 
            application_id: int,
            company: str, 
            position: str, 
            date_applied: date,
            status: ApplicationStatus,
            location: str | None = None, 
            work_mode: WorkMode | None = None, 
            url: str | None = None,
            notes: str | None = None
    ):
        # input validation
        if isinstance(application_id, bool) or not isinstance(application_id, int) or application_id <= 0:
            raise ValueError("Application ID must be a positive integer")
        if not isinstance(company, str) or not company.strip():
            raise ValueError("Company must be a non-blank string")
        if not isinstance(position, str) or not position.strip():
            raise ValueError("Position must be a non-blank string")
        if not isinstance(date_applied, date):
            raise TypeError("Date_applied must be a date object")
        if not isinstance(status, ApplicationStatus):   
            raise TypeError("Status must be an instance of ApplicationStatus Enum")
        if work_mode is not None and not isinstance(work_mode, WorkMode):
            raise TypeError("Workmode must be an instance of WorkMode Enum or None")
        
        self.application_id = application_id
        self.company = company.strip()
        self.position = position.strip()
        self.location = location
        self.work_mode = work_mode
        self.date_applied = date_applied
        self.status = status
        self.url = url
        self.notes = notes

    def to_dict(self) -> dict:
        return {
            "application_id": self.application_id,
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "work_mode": self.work_mode.value if self.work_mode else None,
            "date_applied": self.date_applied.isoformat(),
            "status": self.status.value,
            "url": self.url,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Application":
        if not data or not isinstance(data, dict):
            raise ValueError("Data must be a non-empty dictionary")

        return cls(
            application_id = data["application_id"],
            company = data["company"],
            position = data["position"],
            location = data["location"],
            work_mode = WorkMode(data["work_mode"]) if data["work_mode"] else None,
            date_applied = date.fromisoformat(data["date_applied"]),
            status = ApplicationStatus(data["status"]),
            url = data["url"],
            notes = data["notes"]
        )

    