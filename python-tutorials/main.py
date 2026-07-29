# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def introduce(self):
#         print(f"{self.brand} {self.model} ({self.year})")

# my_car = Car("Toyota", "Camry", 2024)
# my_car.introduce()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return self.area() * 2

# my_reactangle = Rectangle(2,4)
# print(my_reactangle.area())
# print(my_reactangle.perimeter())

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("deposit successfully")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("withdraw successfully")

# my_bank_account = BankAccount("Ron", 500)

# import hello
## Phan 1
# def subtract(a,b):
#     return  a - b

# print(subtract(5,3))
# def multiply(a, b):
#     return a * b

    
# print(multiply(5,3))

# def divide(a, b):
#     return a / b
    
# print(divide(6,3))

# # Phan 5
# def introduce(name, age=18):
#     print(f"My name is {name}. I am {age} years old")
    
# introduce("Ron",20)
# introduce("Ron")

# # phan 6
# def total(*numbers):
#     temp_total = 0
#     for number in numbers:
#         temp_total += number
#     return temp_total
# print(total(1, 2, 3))

# # mini project
# list_students = [
#     { "name": "Nam", "age": 15, "score": 5},
#     { "name": "Yen", "age": 15, "score": 6},
#     { "name": "Hung", "age": 15, "score": 7},
# ]

# def add_student(name, age, score):
#     list_students.append({"name": name,"age": age,"score": score})
# add_student("Trang", 15,8)
# print(list_students)

# def update_student(name, score):
#     for student in list_students:
#         if student["name"] == name:
#             student["score"] = score
    
# update_student("Hung", 8)
# print(list_students)

# def remove_student(name):
#     global list_students
#     list_students = [
#         student
#         for student in list_students
#         if student["name"] != name
#     ]

# remove_student("Hung")
# print(list_students)

# def average_score():
#     total = 0
#     for student in list_students:
#         total += student["score"]
#     return total / len(list_students)

# print(average_score())

# def top_student():
#     return max(list_students, key=lambda student: student["score"])
# print(top_student())

# def rank(score):
#     if score >= 9:
#         print("Excellent")
#     elif score >= 8:
#         print("Very Good")
#     elif score >= 6.5:
#         print("Good")
#     elif score >= 5:
#         print("Pass")
#     else:
#         print("Fail")
# rank(4)

# students = [
#     {"name": "Nam", "age": 15, "score": 5},
#     {"name": "Yen", "age": 15, "score": 6},
#     {"name": "Hung", "age": 15, "score": 7},
#     {"name": "Ron", "age": 23, "score": 10},
# ]
# #1
# def passed_students():
#     students[:] = [
#         student
#         for student in students
#         if student["score"] >=5
#     ]
#     print(students)
# passed_students()

# #2
# def student_score_map():
#     new_dic = {
#         student["name"]: student["score"]
#         for student in students
#     }
#     print(new_dic)
# student_score_map()

# #3
# def unique_ages():
#     unique = {
#         student["age"]
#         for student in students
#     }
#     print(unique)
# unique_ages()

# #4
# for index, student in enumerate(students):
#     print(f"{index + 1}. {student["name"]} - {student["score"]}")

# # 5
# subjects = [
#     "Math",
#     "English",
#     "Physics",
#     "Chemistry",
# ]

# for student, subject in zip(students, subjects):
#     print(f"{student["name"]} learns {subject}")

# #Mentor Challenge
# students = [
#     {"name": "Nam", "score": 4},
#     {"name": "Yen", "score": 6},
#     {"name": "Hung", "score": 7},
# ]
# # temp_students = []
# # for student in students:
# #     if student["score"] >= 5:
# #         temp_students.append(f"{student["name"]}: Pass")
# #     else:
# #         temp_students.append(f"{student["name"]}: Fail")

# temp_students = [
#     f"{student["name"]}: Pass" if student["score"] >= 5 else f"{student["name"]}: Fail"
#     for student in students
# ]
# print(temp_students)

# numbers = [1, 2, 3, 4, 5]

# temp_numbers = {
#     number: pow(number, 2)
#     for number in numbers
# }
# print(temp_numbers)
