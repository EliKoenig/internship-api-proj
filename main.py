from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from company_routes import router as company_router
from application_routes import router as application_router

app = FastAPI(title="Internship Tracker API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Internship Tracker API is running"}


app.include_router(company_router)
app.include_router(application_router)