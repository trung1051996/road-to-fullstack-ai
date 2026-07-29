import json
from services.student_service import load_students, save_students, add_student, update_student,remove_student, find_student

students = load_students()

save_students([
    {
        "name": "Nam",
        "age": 15,
        "score": 5
    },
    {
        "name": "Yen",
        "age": 15,
        "score": 6
    }
])


add_student({
        "name": "Yen",
        "age": 15,
        "score": 6
    })

update_student("Yen", "Evan")
remove_student("Yen")
print(find_student("Yen"))