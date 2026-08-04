
from app.gemini_client import GeminiClient

class GeminiService:
    def __init__(self):
        self.service = GeminiClient()
    
    def ask_ai(self, question, students):
        prompt = f"Below is list students: \n {"\n".join([
            f"Name: {student.name}, Age: {student.age}, Score: {student.score}"
            for student in students
        ])}.\nQuestion: {question}"
        response = self.service.chat(prompt)
        if not response: 
            raise ValueError("Something error")
        else:
            return response.text