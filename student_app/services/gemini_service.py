
from app.gemini_client import GeminiClient

class GeminiService:
    def __init__(self):
        self.service = GeminiClient()
    
    def ask_ai(self, question, context):
        prompt = f"Below is list students: \n {context}.\nQuestion: {question}"
        response = self.service.chat(prompt)
        if not response: 
            raise ValueError("Something error")
        else:
            return response