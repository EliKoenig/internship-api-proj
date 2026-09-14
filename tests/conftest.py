from fastapi.testclient import TestClient
from database import companies, applications, counters
import pytest

from main import app
@pytest.fixture()
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_database():
    companies.clear()
    applications.clear()

    counters["company_id"] = 1
    counters["application_id"] = 1

@pytest.fixture()
def existing_company(client, reset_database):
    response = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )
    company_id = response.json()["id"]
    return company_id
