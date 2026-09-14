
def test_root(client):
    response = client.get("/")

    assert response.status_code == 200

def test_create_company(client):
    response = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Lit internship",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "NVIDIA"
    assert data["website"] == "https://www.nvidia.com"
    assert data["notes"] == "Lit internship"

def test_get_companies(client):
    client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Lit internship",
        },
    )

    response = client.get("/companies")

    assert response.status_code == 200
    
    data = response.json()

    assert len(data) == 1

    assert data[0]["name"] == "NVIDIA"
    assert data[0]["website"] == "https://www.nvidia.com"
    assert data[0]["notes"] == "Lit internship"

def test_get_company(client, existing_company):
    company_id = existing_company

    response = client.get(f"/companies/{company_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "NVIDIA"
    assert data["website"] == "https://www.nvidia.com"
    assert data["notes"] == "Dream internship"


def test_update_company(client):
    create_response = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Lit internship",
        },
    )

    company_id = create_response.json()["id"]

    response = client.patch(
        f"/companies/{company_id}",
        json={
            "notes": "Updated internship notes"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == company_id
    assert data["name"] == "NVIDIA"
    assert data["website"] == "https://www.nvidia.com"
    assert data["notes"] == "Updated internship notes"

def test_delete_company(client):
    create_response = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Lit internship",
        },
    )

    company_id = create_response.json()["id"]

    response = client.delete(f"/companies/{company_id}")

    assert response.status_code == 200

    response = client.get(f"/companies/{company_id}")

    assert response.status_code == 404

def test_create_application(client):
    create_company = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )

    company_id = create_company.json()["id"]

    response = client.post(
        "/applications",
        json={
            "company_id": company_id,
            "position": "Software Engineer Intern",
            "status": "Applied",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["company_id"] == company_id
    assert data["position"] == "Software Engineer Intern"
    assert data["status"] == "Applied"

def test_get_applications(client):
    create_company = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )

    company_id = create_company.json()["id"]

    client.post(
        "/applications",
        json={
            "company_id": company_id,
            "position": "Software Engineer Intern",
            "status": "Applied",
        },
    )

    response = client.get("/applications")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["company_id"] == company_id
    assert data[0]["position"] == "Software Engineer Intern"
    assert data[0]["status"] == "Applied"

def test_get_application(client):
    create_company = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )

    company_id = create_company.json()["id"]

    create_application = client.post(
        "/applications",
        json={
            "company_id": company_id,
            "position": "Software Engineer Intern",
            "status": "Applied",
        },
    )

    application_id = create_application.json()["id"]

    response = client.get(f"/applications/{application_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == application_id
    assert data["company_id"] == company_id
    assert data["position"] == "Software Engineer Intern"
    assert data["status"] == "Applied"

def test_update_application(client):
    create_company = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )

    company_id = create_company.json()["id"]

    create_application = client.post(
        "/applications",
        json={
            "company_id": company_id,
            "position": "Software Engineer Intern",
            "status": "Applied",
        },
    )

    application_id = create_application.json()["id"]

    response = client.patch(
        f"/applications/{application_id}",
        json={
            "status": "Interview"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == application_id
    assert data["company_id"] == company_id
    assert data["position"] == "Software Engineer Intern"
    assert data["status"] == "Interview"

def test_delete_application(client):
    create_company = client.post(
        "/companies",
        json={
            "name": "NVIDIA",
            "website": "https://www.nvidia.com",
            "notes": "Dream internship",
        },
    )

    company_id = create_company.json()["id"]

    create_application = client.post(
        "/applications",
        json={
            "company_id": company_id,
            "position": "Software Engineer Intern",
            "status": "Applied",
        },
    )

    application_id = create_application.json()["id"]

    response = client.delete(f"/applications/{application_id}")

    assert response.status_code == 200

    response = client.get(f"/applications/{application_id}")

    assert response.status_code == 404

def test_create_application_invalid_company(client):
    response = client.post(
        "/applications",
        json={
            "company_id":  999,
            "position":  "Software Engineer Intern",
            "status": "Applied",
        },
    )


    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Company with corresponding ID not found"
