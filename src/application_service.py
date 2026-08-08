from src.application import Application, ApplicationStatus, WorkMode
from src.storage import save_applications, load_applications, DATA_FILE_PATH
from datetime import date

class ApplicationService:
    def __init__(self, data_file_path: str = DATA_FILE_PATH):
        self.data_file_path = data_file_path
        self.applications = load_applications(self.data_file_path)
        self.next_id = self._generate_next_id()

    def _generate_next_id(self) -> int:
        if not self.applications:
            return 1
        else:
            return max(app.application_id for app in self.applications) + 1

    def add_application(
        self, 
        company: str, 
        position: str, 
        date_applied: date, 
        status: ApplicationStatus, 
        location: str | None = None, 
        work_mode: WorkMode | None = None, 
        url: str | None = None, 
        notes: str | None = None
    ) -> Application:
        new_application = Application(
            application_id=self.next_id,
            company=company,
            position=position,
            date_applied=date_applied,
            status=status,
            location=location,
            work_mode=work_mode,
            url=url,
            notes=notes
        )
        self.applications.append(new_application)
        self.next_id += 1
        save_applications(self.applications, self.data_file_path)
        return new_application

    def get_all_applications(self) -> list[Application]:
        return self.applications.copy()

    def find_application_by_id(self, application_id: int) -> Application | None:
        for app in self.applications:
            if app.application_id == application_id:
                return app
        return None

    def delete_application(self, application_id: int) -> bool:
        application = self.find_application_by_id(application_id)
        if application:
            self.applications.remove(application)
            save_applications(self.applications, self.data_file_path)
            return True
        return False

    def update_application(
        self,
        # only the fields that are provided (not None) will be updated
        application_id: int, 
        company: str | None = None, 
        position: str | None = None, 
        date_applied: date | None = None, 
        status: ApplicationStatus | None = None, 
        location: str | None = None, 
        work_mode: WorkMode | None = None, 
        url: str | None = None, 
        notes: str | None = None
    ) -> bool:
        application = self.find_application_by_id(application_id)
        if not application: #the application with the given ID does not exist
            return False

        if company is not None:
            application.company = company
        if position is not None:
            application.position = position
        if date_applied is not None:
            application.date_applied = date_applied
        if status is not None:
            application.status = status
        if location is not None:
            application.location = location
        if work_mode is not None:
            application.work_mode = work_mode
        if url is not None:
            application.url = url
        if notes is not None:
            application.notes = notes

        save_applications(self.applications, self.data_file_path)
        return True

    def search_by_company(self, company_name: str) -> list[Application]:
        return [app for app in self.applications if app.company.lower() == company_name.lower()]

    def filter_by_status(self, status: ApplicationStatus) -> list[Application]:
        return [app for app in self.applications if app.status == status]

    def get_statistics(self) -> dict:
        stats = {
            "total_applications": len(self.applications),
            "status_counts": {status.value: 0 for status in ApplicationStatus}
        }
        for app in self.applications:
            stats["status_counts"][app.status.value] += 1
        return stats