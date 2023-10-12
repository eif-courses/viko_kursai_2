from db import db_connection
from schema import Student


async def get_all_students():
    query = "select * from students"
    result = await db_connection.fetch_all(query=query)
    return result


async def get_student_by_id(id: int):
    query = "SELECT * FROM students WHERE student_id=:student_id"
    result = await db_connection.fetch_one(query=query, values={"student_id": id})
    return result


async def create_student(student: Student):
    query = "INSERT INTO students (first_name, last_name, date_of_birth, email) VALUES (:first_name, :last_name, :date_of_birth, :email)"
    values = {"first_name": student.first_name, "last_name": student.last_name, "date_of_birth": student.date_of_birth,
              "email": student.email}
    result = await db_connection.execute(query=query, values=values)
    return result


async def delete_student(stud_id: int):
    query = "DELETE FROM students WHERE student_id=:student_id"
    values = {"student_id": stud_id}
    await db_connection.execute(query=query, values=values)
