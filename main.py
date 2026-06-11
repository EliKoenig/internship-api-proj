from fastapi import FastAPI

from company_routes import router as company_router
from application_routes import router as application_router

app = FastAPI(title="Internship Tracker API")


@app.get("/")
def root():
    return {"message": "Internship Tracker API is running"}


app.include_router(company_router)
app.include_router(application_router)