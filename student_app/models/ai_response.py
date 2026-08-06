from pydantic import BaseModel

class StudentAnswer(BaseModel):
    student_name: str
    score: float