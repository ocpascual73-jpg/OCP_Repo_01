# What's New: Lesson 3/Chapter 3
# # In This Segment
# ## Python 3.12
# * f-string improvement
# 
# ## Python 3.10
# * Multiple selection with `match`...`case`
# 
# ## Python 3.8
# * Assignment Expressions—The `:=` Walrus Operator 
# * `statistics` Function `mode` Update and Function `multimode` 

# ---

# Format Strings (f-strings)
# > **Python 3.12, Lesson 3 and higher**
# > [PEP 701, f-strings in the grammar](https://peps.python.org/pep-0701/)
# * f-string placeholders may now contain strings that use the same delimiter as the f-string:

print(f'Face{'Frequency':>13}')

# * Interpreter recognizes quotes in placeholder are for string literal being formatted, not delimiters for the f-string
# * `SyntaxError` previously, so we would have to write as

print(f'Face{"Frequency":>13}')


# # Multiple Selection with the `match`...`case` Statement
# > **Python 3.10, Lesson 3**  
# > * PEP 634—Structural Pattern Matching: Specification  
# > https://peps.python.org/pep-0634/  
# > * PEP 635—Structural Pattern Matching: Motivation and Rationale  
# https://peps.python.org/pep-0635/  
# > * PEP 636—Structural Pattern Matching: Tutorial  
# https://peps.python.org/pep-0636/
# 
# * Similar to but more powerful than `switch` and similar in many other languages
# * Expression after `match` is the **subject expression**
# * `match`...`case` compares subject expression’s value to each `case`’s value
# * First matching `case`’s statements execute, then `match` statement terminates

grade = 'F'

match grade:
    case 'A':
        print('grade is A')
    case 'B':
        print('grade is B')
    case 'C':
        print('grade is C')
    case 'D':
        print('grade is D')
    case _:
        print('grade is F')


# ## Irrefutable `case` Block
# * `case _:` 
#     * Python’s equivalent of `default` case in other programming languages
#     * Formally called an **irrefutable `case` block** 
#     * Always matches subject expression if no other `case`s execute
#     * Must be the last `case`



# # Assignment Expressions—The `:=` Walrus Operator 
# > **Python 3.8**, Lesson 3  
# > PEP 572, Assignment Expressions: https://peps.python.org/pep-0572/
# 
# * Named “Walrus operator” because it resembles the eyes and tusks of a walrus
# * For cases in which you’d store a value in a variable, then use that variable in a control statement’s condition and possibly its body

grade = int(input('Enter grade (0-100): '))

if grade >= 60:
    print(f'{grade} is a passing grade')
else:
    print(f'{grade} is a failing grade')

# * Can perform the assignment directly in condition via `:=` assignment expression
# * Variable to left of `:=` may be used throughout control statement

if (grade := int(input('Enter grade (0-100): '))) >= 60:
    print(f'{grade} is a passing grade')
else:
    print(f'{grade} is a failing grade')


# ## Walrus Operator Use-Cases 
# * Calling a regular expression function in an `if`, `if`…`else`, or `if`…`elif`…`else` condition, then using returned match object in the suite
# * In sentinel-controlled loop conditions, reading a value then immediately testing whether it was the sentinel and, if not, processing the value in the suite
# * In the `if` clause of a comprehension, initializing a variable, then using it in the expression that inserts a value in the list, dictionary or set



# # `statistics` Function `mode` Update and Function `multimode`
# > **Python 3.8**, Section 3.17  
# > `statistics`—Mathematical statistics functions:
# > * `mode`:  
# https://docs.python.org/3/library/statistics.html#statistics.mode
# > * `multimode`:  
# https://docs.python.org/3/library/statistics.html#statistics.multimode

# ## `mode` Function
# * A dataset can have two or more “most frequent” (mode) values
# * Such a dataset is **multi-modal**
# * `statistics.mode` used to raise a `StatisticsError` for multi-modal datasets
# * Now, it returns the first mode it finds
# * Following `mode` call returns 85 because it encounters the second 85 before the second 93

import statistics
grades2 = [85, 93, 45, 89, 85, 93]
statistics.mode(grades2)

# ## `multimode` Function
# * Returns a list of the most frequent values in a multi-modal dataset

statistics.multimode(grades2)

# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
