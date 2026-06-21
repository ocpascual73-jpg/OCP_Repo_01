# # What's New: Lesson 5, Lists and Tuples
# # In This Segment
# ## Python 3.12
# * Comprehension Inlining for Better Performance
# ## Python 3.11
# * Starred Unpacking Expressions in `for` Statements
# ## Python 3.10
# * Optional Length-Checking for `zip`
# ## Python 3.8
# * Self-Documenting f-strings



# # Self-Documenting f-strings 
# > **Python 3.8**, Section 5.4  
# > Self-Documenting f-strings, documented in bug report https://github.com/python/cpython/issues/80998
# 
# * Update to an existing example
# * Can swap two variables’ values using sequence packing and unpacking

number1 = 99

number2 = 22

number1, number2 = (number2, number1)

print(f'number1={number1}; number2={number2}')


# * For cases in which you display a variable’s name and value, as above, can use self-documenting f-strings
# * When Python encounters `=` to the right of a variable name in a placeholder, it inserts into the string the variable name, and = and the value

print(f'{number1=}; {number2=}')



# # Starred Unpacking Expressions in `for` Statements
# > **Python 3.11, end of Section 5.4**  
# > Listed as a bug fix at https://github.com/python/cpython/issues/90881
# 
# * Starred unpacking expressions also can be used in `for` statements
# * As loop iterates through `data`, it upacks each tuple 
#     * `first` refers to the current tuple’s first element
#     * `the_rest` refers to a list of the current tuple’s remaining elements

data = [
    (1, 2, 3, 4),
    (5, 6),
    (7, 8, 9)
]

for first, *the_rest in data:
    print(f"first: {first}, the_rest: {the_rest}")



# # Comprehension Inlining for Better Performance
# > **Python 3.12, Section 5.12 in the comprehensions discussion**
# > PEP 709—Inlined comprehensions. https://peps.python.org/pep-0709/
#  
# * Before Python 3.12, for each comprehension, the interpreter
#     * transformed it into a function 
#     * called that function to perform task
# * Increased execution-time overhead
# * Interpreter now **inlines** each comprehension's logic where it appears in the code
# * **Eliminates overhead** of creating and calling a function, increasing performance




# # Optional Length-Checking for `zip`> **Python 3.10**, Section 5.15  
# > PEP 618, Add Optional Length-Checking To `zip`:  
# > https://peps.python.org/pep-0618/
# 
# * Number of tuples `zip` produces is limited by its shortest iterable argument

names = ['Bob', 'Sue', 'Amanda', 'Paul']

grade_point_averages = [3.5, 4.0, 3.75]

for name, gpa in zip(names, grade_point_averages):
    print(f'{name=}; {gpa=}')

# ## Requiring Iterables of the Same Length

# * Sometimes `zip` arguments of different lengths should be a logic error
# * If so, pass `strict=True` as `zip`’s last argument
# * `ValueError` occurs if arguments do not have same length

for name, gpa in zip(names, grade_point_averages, strict=True):
    print(f'{name=}; {gpa=}')


# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
