from fastapi import APIRouter, HTTPException

from schemas import CompanyCreate, CompanyUpdate
from database import companies, counters

router = APIRouter()


@router.get("/companies")
def get_companies():
    return companies


@router.post("/companies")
def create_company(company: CompanyCreate):
    new_company = {
        "id": counters["company_id"],
        "name": company.name,
        "website": company.website,
        "notes": company.notes,
    }

    companies.append(new_company)
    counters["company_id"] += 1

    return new_company


@router.get("/companies/{company_id}")
def get_company(company_id: int):
    for company in companies:
        if company["id"] == company_id:
            return company

    raise HTTPException(status_code=404, detail="Company not found")


@router.patch("/companies/{company_id}")
def update_company(company_id: int, updates: CompanyUpdate):
    for company in companies:
        if company["id"] == company_id:
            update_data = updates.model_dump(exclude_unset=True)
            company.update(update_data)
            return company

    raise HTTPException(status_code=404, detail="Company not found")


@router.delete("/companies/{company_id}")
def delete_company(company_id: int):
    for index, company in enumerate(companies):
        if company["id"] == company_id:
            deleted_company = companies.pop(index)
            return {"deleted": deleted_company}

    raise HTTPException(status_code=404, detail="Company not found")