from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///internship_tracker.db")
SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
#Initialize lists for all internship properties and information
companies = []
applications = []

counters = {
    "company_id": 1,
    "application_id": 1,
}