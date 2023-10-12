from fastapi import APIRouter

import viko_services
from schema import Student

router = APIRouter(tags=["Kursai"], prefix="/api/v1")


@router.post("/students")
async def create_student(student: Student):
    await viko_services.create_student(student)
    return student


@router.get("/students")
async def display_students():
    return await viko_services.get_all_students()


@router.delete("/students/{id}")
async def delete_student(id: int):
    await viko_services.delete_student(id)
    return {"message": "Studentas ištrintas!"}
