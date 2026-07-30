import json
from services.student_service import StudentService
from models.student import Student

student_service = StudentService()
# print(student_service.load_students())

# new_student = Student("Yenzz 1", 20, 8)

# student_service.save_students([new_student])

# student_service.add_student(new_student)

# student_service.update_student("Yenzz", "Evan")
# student_service.remove_student("Yen")
print(student_service.find_student("Hung"))