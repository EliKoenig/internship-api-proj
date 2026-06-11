# Internship Tracker API

A FastAPI backend API for tracking internship companies and applications.

## Features

- Company CRUD endpoints
- Application CRUD endpoints
- Application-to-company relationship validation
- Pydantic request Validation
- Swagger/OpenAPI documentation

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

## Tech Stack

- Pyhton
- FastAPI
- Pydantic
- Uvicorn
