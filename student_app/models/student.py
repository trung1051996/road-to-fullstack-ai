from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    score: float
    # def __init__(self, name, age, score):
    #     self.name = name
    #     self.age = age
    #     self.score = score

    # def to_dict(self):
    #     return {
    #         "name": self.name,
    #         "age": self.age,
    #         "score": self.score
    #     }
        
    # def update_name(self, name=None):
    #     if name is not None:
    #         self.name = name
    #     return self
    