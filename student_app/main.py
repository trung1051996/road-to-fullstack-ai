from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.student_service import StudentService
from models.student import Student
app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    age: int
    score:float

@app.get("/")
def say_hello():
    return {"message": "Hello FastAPI"}


@app.get("/students/{name}/age/{age}")
def get_student(name: str, age: int):
    return {"name": name, "age": age}

@app.get("/students")
def get_students():
    return StudentService().load_students()

@app.post("/students")
def create_student(student: StudentCreate): #dict/JSON need deserialize to object
    student_obj = Student(**student.model_dump()) # deserialize to object
    new_students = StudentService().add_student(student_obj)
    return new_students

@app.put("/student/{name}")
def update_student(old_name: str, new_name: str):
    students = StudentService().update_student(old_name, new_name)
    if students is None:
        raise HTTPException(status_code = 404, detail="Student not found")
    return students

@app.delete("/student/{name}")
def delete_student(name: str):
    students = StudentService().remove_student(name)
    if students is None:
        raise HTTPException(status_code = 404, detail="Student not found")
    return students