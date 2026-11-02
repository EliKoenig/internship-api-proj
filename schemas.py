from pydantic import BaseModel
from enum import Enum

#Create classes for information CRUD properties
class CompanyCreate(BaseModel):
    name: str
    website: str | None = None
    notes: str | None = None

class ApplicationStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"

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

