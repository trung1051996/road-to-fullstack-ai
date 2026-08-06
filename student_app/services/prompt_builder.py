

def format_students(students):
    return "\n".join(
        f"Name: {s.name}, Age: {s.age}, Score: {s.score}" for s in students
    )

class StudentPromptBuilder:
    def build(self, students, question):
        context = format_students(students)
        return f"""
                Below is list students:
                {context}
                Question: {question}
                """