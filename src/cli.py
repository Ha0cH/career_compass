from .application_service import ApplicationService
from .application import ApplicationStatus, WorkMode
from datetime import date

class CareerCompassCLI:
    def __init__(self, service: ApplicationService):
        self.service = service

    def run(self):
        while True:
            print("\nCareer Compass - Job Application Tracker")
            print("1. Add a new application")
            print("2. View all applications")
            print("3. Find an application by ID")
            print("4. Delete an application by ID")
            print("5. Update an application by ID")
            print("6. Find applications by company")
            print("7. Filter applications by status")
            print("8. Show statistics")
            print("9. Exit")

            choice = input("Enter your choice (1-9): ").strip()

            if choice == "1":
                self._add_application()
            elif choice == "2":
                self._view_all_applications()
            elif choice == "3":
                self._find_application_by_id()
            elif choice == "4":
                self._delete_application_by_id()
            elif choice == "5":
                self._update_application_by_id()
            elif choice == "6":
                self._find_applications_by_company()
            elif choice == "7":
                self._filter_applications_by_status()
            elif choice == "8":
                self._show_statistics()
            elif choice == "9":
                print("Bye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def _add_application(self):
        company = self._get_required_string_input("Enter company name: ")
        position = self._get_required_string_input("Enter position: ")
        date_applied = self._get_date("Enter date applied (YYYY-MM-DD): ")
        status = self._get_status("Enter status (APPLIED, OA, PHONE_SCREEN, INTERVIEW, OFFER, REJECTED, ACCEPTED, WITHDRAWN): ")
        location = self._get_optional_string_input("Enter location (optional): ")
        work_mode = self._get_work_mode_optional("Enter work mode (REMOTE, HYBRID, ON_SITE) (optional): ")
        url = self._get_optional_string_input("Enter URL (optional): ")
        notes = self._get_optional_string_input("Enter notes (optional): ")

        application = self.service.add_application(
            company=company,
            position=position,
            date_applied=date_applied,
            status=status,
            location=location,
            work_mode=work_mode,
            url=url,
            notes=notes
        )
        print(f"Application added with ID: {application.application_id}")

    def _view_all_applications(self):
        applications = self.service.get_all_applications()
        if applications:
            for app in applications:
                print("*******************")
                print(app)
            print("*******************")
        else:
            print("No applications found.")

    def _find_application_by_id(self):
        application_id = self._get_integer("Enter application ID: ")
        application = self.service.find_application_by_id(application_id)
        if application:
            print(application)
        else:
            print("Application not found.")

    def _delete_application_by_id(self):
        application_id = self._get_integer("Enter application ID to delete: ")
        application = self.service.find_application_by_id(application_id)
        if not application:
            print("Application ID invalid")
            return
        while True:
            print(application)
            confirmation = input("Are you sure? (y/n) ").strip().lower()
            if confirmation == "y":
                self.service.delete_application(application_id)
                print(f"Application with ID [{application_id}] deleted")
                return
            elif confirmation == "n":
                return
            else:
                print("Invalid input. Please enter y or n")


    def _update_application_by_id(self):
        application_id = self._get_integer("Enter application ID to update: ")
        application = self.service.find_application_by_id(application_id)
        if not application:
            print("Application not found.")
            return

        print(application)
        company = self._get_optional_string_input("Enter new company name (leave blank to keep current): ")
        position = self._get_optional_string_input("Enter new position (leave blank to keep current): ")
        date_applied = self._get_date_optional("Enter new date applied (YYYY-MM-DD) (leave blank to keep current): ")
        status = self._get_status_optional("Enter new status (APPLIED, OA, PHONE_SCREEN, INTERVIEW, OFFER, REJECTED, ACCEPTED, WITHDRAWN) (leave blank to keep current): ")
        location = self._get_optional_string_input("Enter new location (leave blank to keep current): ")
        work_mode = self._get_work_mode_optional("Enter new work mode (REMOTE, HYBRID, ON_SITE) (leave blank to keep current): ")
        url = self._get_optional_string_input("Enter new URL (leave blank to keep current): ")
        notes = self._get_optional_string_input("Enter new notes (leave blank to keep current): ")

        # only update the fields that are provided (not None)
        success = self.service.update_application(
            application_id=application_id,
            company=company,
            position=position,
            date_applied=date_applied,
            status=status,
            location=location,
            work_mode=work_mode,
            url=url,
            notes=notes
        )
        if success:
            print("Application updated.")
        else:
            print("Application not found.")

    def _find_applications_by_company(self):
        company_name = self._get_required_string_input("Enter company name to search: ")
        applications = self.service.search_by_company(company_name)
        if applications:
            for app in applications:
                print("*******************")
                print(app)
        else:
            print("No applications found for this company.")

    def _filter_applications_by_status(self):
        status = self._get_status("Enter status to filter by (APPLIED, OA, PHONE_SCREEN, INTERVIEW, OFFER, REJECTED, ACCEPTED, WITHDRAWN): ")
        applications = self.service.filter_by_status(status)
        if applications:
            for app in applications:
                print("*******************")
                print(app)
        else:
            print("No applications found with this status.")

    def _show_statistics(self):
        stats = self.service.get_statistics()
        print("Application Statistics:")
        print("-----------------------")
        print(f"Total applications: {stats['total_applications']}")
        for status, count in stats['status_counts'].items():
            print(f"    {status}: {count}")

    # helper methods
    def _get_optional_string_input(self, prompt: str) -> str | None:
        value = input(prompt).strip()
        return value if value else None

    def _get_required_string_input(self, prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This field is required. Please enter a valid value.")

    def _get_date(self, prompt: str) -> date:
        while True:
            value = input(prompt).strip()
            try:
                return date.fromisoformat(value)
            except ValueError:
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")

    def _get_date_optional(self, prompt: str) -> date | None:
        while True:
            value = input(prompt).strip()
            if not value:  # if the input is empty, return None
                return None
            try:
                return date.fromisoformat(value)
            except ValueError:
                print("Invalid date format. Please enter a date in YYYY-MM-DD format or leave blank to keep current.")

    def _get_status(self, prompt: str) -> ApplicationStatus:
        while True:
            value = input(prompt).strip().upper().replace(" ", "_")
            try:
                return ApplicationStatus[value]
            except KeyError:
                print("Invalid status. Please enter a valid status.")

    def _get_status_optional(self, prompt: str) -> ApplicationStatus | None:
        while True:
            value = input(prompt).strip()
            if not value:  # if the input is empty, return None
                return None
            try:
                return ApplicationStatus[value.upper().replace(" ", "_")]
            except KeyError:
                print("Invalid status. Please enter a valid status or leave blank to keep current.")

    def _get_work_mode_optional(self, prompt: str) -> WorkMode | None:
        while True:
            value = input(prompt).strip()
            if not value:  # if the input is empty, return None
                return None
            try:
                return WorkMode[value.upper().replace(" ", "_")]
            except KeyError:
                print("Invalid work mode. Please enter a valid work mode or leave blank.")

    def _get_integer(self, prompt: str) -> int:
        while True:
            value = input(prompt).strip()
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Invalid ID. Please enter a positive integer.")