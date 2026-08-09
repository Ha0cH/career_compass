from .application_service import ApplicationService
from .cli import CareerCompassCLI

def main():
    service = ApplicationService()
    cli = CareerCompassCLI(service)
    cli.run()

if __name__ == "__main__":
    main()