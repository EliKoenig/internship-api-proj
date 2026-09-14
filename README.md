# Internship Tracker API

A FastAPI backend API for tracking internship companies and applications.

## Features

- Company CRUD endpoints
- Application CRUD endpoints
- Application-to-company relationship validation
- Pydantic request validation
- Swagger/OpenAPI documentation
- Automated tests with GitHub Actions CI

## Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Open: 
```txt
http://127.0.0.1:8000/docs
```

## Running Tests
```bash
python -m pip install -r requirements.txt
python -m pytest
```
Tests also run automatically on every push and pull request via GitHub Actions (see `.github/workflows/tests.yml`).

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- pytest
