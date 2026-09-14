from pydantic import BaseModel

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