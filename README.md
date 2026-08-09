# Career Compass

Career Compass is a command-line application for tracking job applications throughout the job search process.

It allows users to manage applications, search and filter them, update their status, and view application statistics. The project is designed with a layered architecture and will continue to evolve into a full-stack application as new technologies are learned.

## Features

- Add new job applications
- View all applications
- Search applications by ID
- Search applications by company
- Update existing applications
- Delete applications
- Filter applications by application status
- Display application statistics
- Persistent JSON storage
- Input validation
- Automated unit tests using Pytest

## Project Structure

```
career_compass/
│
├── data/
│   └── applications.json
│
├── src/
│   ├── application.py
│   ├── storage.py
│   ├── application_service.py
│   ├── cli.py
│   └── main.py
│
├── tests/
│   ├── test_application.py
│   ├── test_storage.py
│   └── test_application_service.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Architecture

Career Compass follows a layered architecture:

```
CLI
    ↓
Application Service
    ↓
Storage
    ↓
JSON
```

Each layer has a single responsibility:

- **CLI** handles user interaction.
- **ApplicationService** contains business logic.
- **Storage** reads and writes JSON data.
- **Application** represents the domain model.

## Technologies

- Python 3
- Pytest
- JSON

## Running the application

Clone the repository:

```bash
git clone https://github.com/Ha0cH/career_compass
cd career_compass
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m src.main
```

## Running the tests

```bash
pytest
```

## Future Roadmap

This project is intentionally designed to grow as new technologies are learned.

Planned versions include:

- **Version 2**
  - Replace JSON storage with PostgreSQL

- **Version 3**
  - REST API

- **Version 4**
  - Web dashboard

- **Version 5**
  - Resume and cover letter management

- **Version 6**
  - Interview journal

- **Future**
  - AI-powered resume tailoring
  - Career memory
  - Analytics dashboard

© 2026 Hao Chen. All rights reserved