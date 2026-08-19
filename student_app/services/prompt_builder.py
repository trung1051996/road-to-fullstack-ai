

def format_students(students):
    return "\n".join(
        f"Name: {s.name}, Age: {s.age}, Score: {s.score}" for s in students
    )
def format_students_embed(students):
    return "\n".join(
        f"{s[0].content}" for s in students
    )

class StudentPromptBuilder:
    def build(self, students, question):
        context = format_students(students)
        return f"""
                Below is list students:
                {context}
                Question: {question}
                """
    def build_embed(self, students, question):
        context = format_students_embed(students)
        return f"""
                Below is list students:
                {context}
                Question: {question}
                """