from pydantic import BaseModel
from enum import Enum

#Create classes for information CRUD properties
class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    notes: str | None = None

class ApplicationStatus(str, Enum):
    applied = "Applied"
    interview = "Interviewing"
    offer = "Offer"
    rejected = "Rejected"

class CompanyUpdate(BaseModel):
    name: str | None = None
    website: str | None = None
    notes: str | None = None

class ApplicationCreate(BaseModel):
    company_id: int
    position: str
    status: ApplicationStatus

class ApplicationUpdate(BaseModel):
    company_id: int | None = None
    position: str | None = None
    status: ApplicationStatus | None = None

