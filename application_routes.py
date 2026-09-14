from fastapi import APIRouter, HTTPException

from schemas import ApplicationCreate, ApplicationUpdate
from database import companies, applications, counters

router = APIRouter()


@router.post("/applications")
def create_application(application: ApplicationCreate):

    for company in companies:
        if company["id"] == application.company_id:

            new_application = {
                "id": counters["application_id"],
                "company_id": application.company_id,
                "position": application.position,
                "status": application.status,
            }

            applications.append(new_application)
            counters["application_id"] += 1

            return new_application

    raise HTTPException(
        status_code=400,
        detail="Company with corresponding ID not found",
    )


@router.get("/applications")
def get_applications():
    return applications


@router.get("/applications/{application_id}")
def get_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application

    raise HTTPException(status_code=404, detail="Application not found")


@router.patch("/applications/{application_id}")
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
                detail="Company with corresponding ID not found",
            )

    for application in applications:
        if application["id"] == application_id:
            update_data = updates.model_dump(exclude_unset=True)
            application.update(update_data)
            return application

    raise HTTPException(status_code=404, detail="Application not found")


@router.delete("/applications/{application_id}")
def delete_application(application_id: int):
    for index, application in enumerate(applications):
        if application["id"] == application_id:
            deleted_application = applications.pop(index)
            return {"deleted": deleted_application}

    raise HTTPException(status_code=404, detail="Application not found")