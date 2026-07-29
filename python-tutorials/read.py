# phone_book = open("phone_book.txt", "r")
# # print(phone_book.readlines())

# for person in phone_book.readlines():
#     print(person)
# phone_book.close()

# with open("notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)

# with open("hello.txt", "w", encoding="utf-8") as file:
#     file.write("Hello World 22")

# with open("hello.txt", "a", encoding="utf-8") as file:
#     file.write("\nPython")

# import json

# student = {
#     "name": "Ron"
# }
# text = json.dumps(student)

# print(type(text))

# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(
#         [
#             {
#                 "name": "Nga",
#                 "score": 10
#             }
#         ],
#         file,
#         indent=4,
#         ensure_ascii=False
#     )

# try:
#     with open("abc.txt") as file:
#             print(file.read())
# except FileNotFoundError:
#     print("File not found")
import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

print(students)