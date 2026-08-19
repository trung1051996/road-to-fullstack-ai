from clients.gemini_client import GeminiClient
from services.student_service import StudentService
from services.gemini_service import GeminiService
from models.embedded_document import EmbeddedDocument
from sklearn.metrics.pairwise import cosine_similarity

def format_embedding_student(student):
    return f"""
    Name: {student.name}
    Age: {student.age}
    Score: {student.score}
    """

class EmbeddingService:
    def __init__(
            self,
            student_service: StudentService,
            client: GeminiClient,
            gemini_service: GeminiService | None = None,
        ):
        self.documents = []
        self.student_service = student_service
        self.client = client
        self.gemini_service = gemini_service
    
    def embed_student(self, student):
        content = format_embedding_student(student)

        return EmbeddedDocument(
            id=student.name,
            content=content,
            embedding= self.client.embed(content)
        )

    def embed_students(self):
        students = self.student_service.load_students()
        self.documents = [
            self.embed_student(student)
            for student in students
        ]
        return self.documents
    def embed_text(self, text: str):
        return self.client.embed(text)
    def similarity_search(
            self,
            question: str,
            top_k: int = 3
        ):

        question_vector = self.embed_text(question)
        results = []
        for document in self.documents:
            score = cosine_similarity(
                [question_vector],
                [document.embedding]
            )[0][0]
            results.append((document, score))
        results.sort(
            key=lambda item: item[1],
            reverse=True
        )
        result = self.gemini_service.ask_ai_embed(question, results)
        return result

# if __name__ == "__main__":

    # embedding_service = EmbeddingService(StudentService(), GeminiClient())
    # embedding_service.embed_students()
    # print("🚀 ~ embedding_service.py:35 ~ students:", students.embed_students())

