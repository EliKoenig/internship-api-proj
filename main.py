from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Internship Tracker API")

#Initialize lists for all internship properties and information
companies = []
next_company_id = 1

applications = []
next_application_id = 1

#Create classes for information CRUD properties
class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    notes: str | None = None


class CompanyUpdate(BaseModel):
    name: str | None = None
    website: str | None = None
    notes: str | None = None

class ApplicationCreate(BaseModel):
    company_id: int
    position: str
    status: str

class ApplicationUpdate(BaseModel):
    company_id: int | None = None
    position: str | None = None
    status: str | None = None

@app.get("/")
def root():
    return {"message": "Internship Tracker API is running"}

#CRUD for "companies"
@app.get("/companies")
def get_companies():
    return companies


@app.post("/companies")
def create_company(company: CompanyCreate):
    global next_company_id

    new_company = {
        "id": next_company_id,
        "name": company.name,
        "website": company.website,
        "notes": company.notes,
    }

    companies.append(new_company)
    next_company_id += 1

    return new_company


@app.get("/companies/{company_id}")
def get_company(company_id: int):
    for company in companies:
        if company["id"] == company_id:
            return company

    raise HTTPException(status_code=404, detail="Company not found")


@app.patch("/companies/{company_id}")
def update_company(company_id: int, updates: CompanyUpdate):
    for company in companies:
        if company["id"] == company_id:
            update_data = updates.dict(exclude_unset=True)
            company.update(update_data)
            return company

    raise HTTPException(status_code=404, detail="Company not found")


@app.delete("/companies/{company_id}")
def delete_company(company_id: int):
    for index, company in enumerate(companies):
        if company["id"] == company_id:
            deleted_company = companies.pop(index)
            return {"deleted": deleted_company}

    raise HTTPException(status_code=404, detail="Company not found")

#CRUD for "applications"
@app.post("/applications")
def create_application(application: ApplicationCreate):
    global next_application_id

    for company in companies:
        if company["id"] == application.company_id:
            new_application = {
                "id": next_application_id,
                "company_id": application.company_id,
                "position": application.position,
                "status": application.status,
            }

            applications.append(new_application)
            next_application_id += 1

            return new_application
    raise HTTPException(status_code=400, detail="Company with corresponding ID not found")

@app.get("/applications")
def get_applications():
    return applications

@app.get("/applications/{application_id}")
def get_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application
        
    raise HTTPException(status_code=404, detail="Application not found")

@app.patch("/applications/{application_id}")
def update_application(application_id: int, updates: ApplicationUpdate):

    if updates.company_id is not None:

        company_exists = False

        for company in companies:
            if company["id"] == updates.company_id:
                company_exists = True
                break

        if not company_exists:
            raise HTTPException(
                status_code=400,
                detail="Company with corresponding ID not found"
            )    
        
    for application in applications:
        if application["id"] == application_id:
            update_data = updates.dict(exclude_unset=True)
            application.update(update_data)
            return application
    
    raise HTTPException(status_code=404, detail="Application not found")

@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    for index, application in enumerate(applications):
        if application["id"] == application_id:
            deleted_application = applications.pop(index)
            return {"deleted": deleted_application}

    raise HTTPException(status_code=404, detail="Application not found")