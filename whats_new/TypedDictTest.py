from typing import TypedDict

class StudentData(TypedDict):
    name: str # name is a string
    grades: list[int] # grades is a list of ints

student: StudentData = {'name': 100, 'grades': ['A', 'B+', 'A-']}
