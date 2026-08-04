from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from services.student_service import StudentService
from models.student import Student
app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    age: int
    score:float

class AskRequest(BaseModel):
    question: str

def get_student_services():
    return StudentService()
@app.get("/")
def say_hello():
    return {"message": "Hello FastAPI"}


@app.get("/students/{name}/age/{age}")
def get_student(name: str, age: int):
    return {"name": name, "age": age}

@app.get("/students")
def get_students(service: StudentService = Depends(get_student_services)):
    print("🚀 ~ main.py:27 ~ get_students ~ get_students:")
    return service.load_students()

@app.post("/students")
def create_student(student: StudentCreate, service: StudentService = Depends(get_student_services)): #dict/JSON need deserialize to object
    student_obj = Student(**student.model_dump()) # deserialize to object
    try:
        service.add_student(student_obj)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return student_obj

@app.put("/students/{old_name}")
def update_student(old_name: str, new_name: str, service: StudentService = Depends(get_student_services)):
    student = service.update_student(old_name, new_name)
    if student is None:
        raise HTTPException(status_code = 404, detail="Student not found")
    return student

@app.delete("/students/{name}")
def delete_student(name: str, service: StudentService = Depends(get_student_services)):
    students = service.remove_student(name)
    if students is None:
        raise HTTPException(status_code = 404, detail="Student not found")
    return students

@app.post("/students/ask")
def ask_ai(question: str, service: StudentService = Depends(get_student_services)): #dict/JSON need deserialize to object
    print("🚀 ~ main.py:55 ~ ask_ai ~ question:", question)
    try:
        response = service.ask_ai(question)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return response