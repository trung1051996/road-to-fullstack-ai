
from clients.gemini_client import GeminiClient
from typing import Type
from services.student_service import StudentService
from services.prompt_builder import StudentPromptBuilder
from models.ai_response import StudentAnswer
class GeminiService:
    def __init__(self):
        self.client = GeminiClient()
        self.student_service = StudentService()
        self.builder = StudentPromptBuilder()
    
    def ask_ai(self, question: str):
        students = self.student_service.load_students()

        prompt = self.builder.build(
            students,
            question,
        )

        return self.client.chat(
            prompt,
            response_schema=StudentAnswer,
        )