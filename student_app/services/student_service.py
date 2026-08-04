from pathlib import Path
import json
from models.student import Student
from dataclasses import asdict
 
DATA_FILE = Path("data") / "students.json"

class StudentService:
    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = data_file
    def load_students(self):
        # make sure the exist data
        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        if not self.data_file.exists():
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
        with open(self.data_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return [
                    Student(**item)
                    for item in data
                ]
            except json.JSONDecodeError:
                return []
    def save_students(self, students):
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(
                [
                    asdict(student)
                    for student in students
                ],
                file,
                indent=4,
                ensure_ascii=False
            )
    def add_student(self, student):
        students = self.load_students()
        existing  = next(
            (s for s in students if s.name == student.name),
            None
        )
        if existing:
            raise ValueError("Student already exists")
        students.append(student)
        self.save_students(students)
        return student
    def update_student(self, old_name, new_name):
        students = self.load_students()
        student = next(
            (s for s in students if s.name == old_name),
            None
        )
        if student:
            student.name = new_name
            self.save_students(students)
            return student
        else:
            return None
    def remove_student(self, name):
        students = self.load_students()
        student = next(
            (s for s in students if s.name == name),
            None
        )
        if student:
            students = [
                student
                for student in students
                if student.name != name
            ]
            self.save_students(students)
            return student
        else:
            return None
    def find_student(self, name):
        students = self.load_students()
        return next(
            (student for student in students if student.name == name),
            None
        )