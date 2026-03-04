Event Check-In and Attendance System

Overview:
This project is a simple Event Check-In and Attendance System created using Python, FastAPI, SQLAlchemy, and SQLite.

The main goal of this project is to manage events and track attendees from registration to check-in. It simulates how real events handle attendance in a structured and organized way.

The system allows users to:

Create a new event
Register attendees for an event
Check in attendees
Generate an attendance report


This project also focuses on writing clean code, separating business logic from database operations, and testing the system properly.


Technologies Used:

Python 3
FastAPI
SQLAlchemy
SQLite
Pytest
GitHub Actions


Project Structure:

event-checkin-system/

app/
  main.py
  database.py
  models.py
  repository.py
  services.py

tests/
  test_unit.py
  test_integration.py

.github/workflows/
  ci.yml

requirements.txt
pytest.ini
README.md


How the System Works
models.py defines the database tables.
database.py manages the database connection.
repository.py handles database queries.
services.py contains the main business logic and validations.
main.py defines the API endpoints using FastAPI.



This structure helps keep the code organized and easier to test.

Setup Instructions
1. Clone the repository
git clone https://github.com/SHUBHJITENDRABHAIPRAJAPATI/event-checkin-system
cd event-checkin-system
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Running the Application



Start the FastAPI server:
uvicorn app.main:app --reload


Then open your browser and go to:

http://127.0.0.1:8000/docs

You can test all the endpoints using the Swagger UI.

Running Tests

To run all tests:

pytest

The project includes:

Unit tests (for business logic)

Integration tests (for full database workflow)

All tests should pass successfully.

Continuous Integration

This project uses GitHub Actions for Continuous Integration.

The CI workflow runs automatically:

On every push

On every pull request

The pipeline:

Installs Python

Installs dependencies

Runs all tests

Fails if any test fails

This ensures that the project always works correctly before merging changes.

Functional Features:
The system includes the following features:
Create event with a unique ID
Register attendees with unique email per event
Prevent duplicate registration
Validate email format
Check-in attendees
Prevent double check-in
Generate attendance report in JSON format


What I Learned??

Through this project, I learned how to:
Build REST APIs using FastAPI
Connect and manage databases using SQLAlchemy
Write unit and integration tests using Pytest
Use GitHub Actions for automated testing
Organize a backend project in a clean and structured way


Author:

Shubh Jitendra Prajapati
Course: QUAL2000
Assignment: Event Check-In and Attendance System


Conclusion:

This project successfully implements an event check-in system with proper architecture, testing, and CI integration.

All functional and testing requirements have been completed.