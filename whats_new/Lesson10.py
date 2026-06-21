# # What's New: Lesson 10, Object-Oriented Programming
# # In This Segment
# ## Python 3.12
# * Type Annotations for `**kwargs`
# * `@override` Decorator for Overridden Methods in Subclasses
# ## Python 3.10
# * Type Union Operator for Type Hints
# ## Python 3.9
# * Built-in Collection Types in Type Hints



# # Type Annotations for `**kwargs`
# > **Python 3.12, After Lesson 10's Data Classes example**  
# > PEP 692, Using `TypedDict` for more precise `**kwargs` typing> https://peps.python.org/pep-0692/
# * A function's **`**kwargs`** parameter can receive as arguments
#     * a dictionary preceded by **`**` unpacking operator** to pass a dictionary’s key–value pairs as keyword arguments
#     * an arbitrary number of keyword arguments
# * In Python 3.12, a **`TypedDict`** subclass can document keyword arguments' names and corresponding values' types 
#     * Each keyword argument’s name is an attribute 
#     * Corresponding value’s type is a type hint

# ## `TypedDict` Subclass `StudentData`
# * `StudentData` class indicates that a dictionary representing student data should have
# * `'name'` key with a string (`str`) as its corresponding value
# * `'grades'` key with a list of `int`s (`list[int]`) as its corresponding value  

from typing import TypedDict

class StudentData(TypedDict):
    name: str # name is a string
    grades: list[int] # grades is a list of ints


# ## `calculate_gpa` Function with Keyword Arguments Specified By Class `StudentData`
# * `calculate_gpa` function uses `StudentData` as a type hint 
# * `**kwargs` should keyword arguments with the names and types specified by `StudentData`
#     * otherwise, function might not work correctly
# * Return type's hint indicates function returns a tuple containing a string (`str`) and a `float`
# * These type hints serve as documentation to programmers calling your function
#     * Ignored at execution time 

def calculate_gpa(**kwargs: StudentData) -> (str, float):
    name = kwargs.get('name', 'Name not specified')
    grades = kwargs.get('grades', [])
    average = sum(grades) / len(grades) if grades else 0
    return (name, average)


# ## Calling `calculate_gpa` with a Dictionary

student: StudentData = {'name': 'Paul', 'grades': [97, 84, 88]}


# * `**student` in the following call expands `student` dictionary’s key–value pairs into the keyword arguments
# > `name='Paul', grades=[97, 84, 88]`
# * Function receives them in the `kwargs` parameter

name, average = calculate_gpa(**student)

print(f"{name}'s average is {average:.2f}")


# ## Calling `calculate_gpa` with Keyword Arguments

name, average = calculate_gpa(name='Paul', grades=[97, 84, 88])

print(f"{name}'s average is {average:.2f}")


# ## Verifying Types Via Static Code Analysis with `mypy`
# * Static code analysis tools like `pyright` (https://github.com/microsoft/pyright) and `mypy` (https://mypy-lang.org/) can check type hints to ensure you’re using types correctly in your code
# * To demonstrate this with `StudentData`, we created the following `TypedDictTest.py` in which `student`'s argument types are incorrect

# ```python
# from typing import TypedDict
# 
# class StudentData(TypedDict):
#     name: str # name is a string
#     grades: list[int] # grades is a list of ints
# 
# student: StudentData = {'name': 100, 'grades': ['A', 'B+', 'A-']}
# ```

get_ipython().system('mypy TypedDictTest.py')

student: StudentData = {'name': 100, 'grades': ['A', 'B+', 'A-']}

name, average = calculate_gpa(**student)



# # Type Union Operator for Type Hints 
# > **Python 3.10**, Section 4.2  
# > PEP 604, New Type Union Operator https://peps.python.org/pep-0604/
# 
# * Enables the syntax `X | Y` in type hints to say that a type can be either `X` or `Y`
# * `square` function with type hints for parameter `number` and the function’s return type
#     * function receives an `int` or `float` and returns an `int` or `float`
# ```python
# def square(number: int | float) -> int | float:
#     """Returns the square of number."""
#     return number ** 2
# ```



# # Built-in Collection Types in Type Hints
# > **Python 3.9**, Section 10.13  
# > PEP 585, Type Hinting Generics In Standard Collections  
# https://peps.python.org/pep-0585/
# 
# * Type hints can use built-in collection types such as `list` and `dict` rather than importing the corresponding types (e.g., `List` and `Dict`) from the `typing` module
# * Our Card data class currently declares the faces and suits lists as
# 
# > ```python
# > faces: ClassVar[List[str]]
# > suits: ClassVar[List[str]]
# > ```
# 
# * Can now write these as 
# 
# > ```python
# > faces: ClassVar[list[str]]
# > suits: ClassVar[list[str]]
# > ```



# # `@override` Decorator for Overridden Methods in Subclasses
# > **Python 3.12, Chapter 10** 
# > PEP 698: Override Decorator for Static Typing https://peps.python.org/pep-0698/* **Always declare overridden methods with `@override` to help static code analysis tools and IDEs ensure you define overridden method names and parameter lists correctly**
# * Place `@override` decorator before an overridden method definition to indicate that the subclass method overrides a base-class method with same name and parameter list

# > ```python
# > @override
# > def earnings(self):
# >     """Calculate earnings."""   
# >     return super().earnings() + self.base_salary
# > ```

# * Can then use static code analysis tools like `pyright` (https://github.com/microsoft/pyright) and `mypy` (https://mypy-lang.org/) to check for common method-override errors:
#     * misspelling the subclass method name or 
#     * specifying a different number of parameters from the base-class method.

# ## Checking for Bad Overrides―Misspelled Name
# * In `salariedcommissionemployee2.py`, accidentally misspelled `SalariedCommissionEmployee`’s `earnings` method as `earning`
# * Static analysis with `pyright` for Python 3.12


!pyright --pythonversion 3.12 salariedcommissionemployee2.py


# * Without `@override` and static code analysis, `earning` would be an entirely different method that would not be called if you invoke earnings on a `SalariedCommissionEmployee` object

# ## Checking for Bad Overrides―Wrong Number of Parameters
# * Creates an unintentional overload of base-class method 
# * Calling on subclass object using base-class method's expected signature invokes base class’s version 
#     * Leads to subtle logic errors
# * Static analysis can compare method’s signature with base-class method signatures
#     * If no exact match, tool issues an error
# * `salariedcommissionemployee3.py` defines `earnings` with an extra parameter 


!pyright --pythonversion 3.12 salariedcommissionemployee3.py


# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
