from pathlib import Path
import json

path = Path("data") / "students.json"

def load_students():
    if not path.exists():
        with path.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
    with open(path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except:
            return []


def save_students(students):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            students,
            file
        )

def add_student(student):
    students = load_students()
    students.append(student)
    save_students(students)

def update_student(old_name, new_name):
    students = load_students()
    exist_student = next(
        (student for student in students if student["name"] == old_name),
        None
    )
    if exist_student:
        students = [
            {
                **student,
                "name": new_name
            }
            if student["name"] == old_name else student
            for student in students
        ]
        print("updated successfully", students)

        save_students(students)
    else:
        print("not exist student")

def remove_student(name):
    students = load_students()
    
    students = [
        student
        for student in students
        if student["name"] != name
    ]
    print("remove successfully", students)

    save_students(students)

def find_student(name):
    students = load_students()
    return next(
        (student for student in students if student["name"] == name),
        None
    )