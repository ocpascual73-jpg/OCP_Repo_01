# What's New: Lesson 4, Functions
# # In This Segment
# ## Python 3.10
# * Pattern matching with `match`...`case`
# 
# ## Python 3.8
# * Positional-only parameters
# 
# ## Python 3.4
# * `Enum`s for creating named constants


# # Pattern Matching with `match`...`case`
# > **Python 3.10, Lesson 4+**  
# > * PEP 634—Structural Pattern Matching: Specification  
# https://peps.python.org/pep-0634/  
# > * PEP 635—Structural Pattern Matching: Motivation and Rationale  
# https://peps.python.org/pep-0635/  
# > * PEP 636—Structural Pattern Matching: Tutorial  
# https://peps.python.org/pep-0636/
# 
# * Can match **patterns**, such as number of elements in a data structure
# * Can specify **guard conditions** that help determine whether there is a match
# * Function `calculate` receives an arbitrary list of arguments representing various arithmetic operations and their numeric operands
#     * `*args` gathers the arguments’ values into a tuple
#     * Based on the number of elements in `args`—and sometimes an item's value—`match`…`case` performs the appropriate calculation and returns its result
# * e.g., `calculate(10, '+', 7)`

def calculate(*args):
    match args: # list of arguments
        case [value]: # no operation specified; just return value
            return value
        case [op, value] if op in ('+', '-'): # unary op
            return value if op == '+' else -value
        case [value1, '+', value2]: # addition
            return value1 + value2
        case [value1, '-', value2]: # subtraction
            return value1 - value2
        case [value1, '*', value2]: # multiplication
            return value1 * value2
        case [value1, '/', value2]: # division
            return value1 / value2
        case [value1, '%', value2]: # remainder
            return value1 % value2
        case [value1, '**', value2]: # exponentiation
            return value1 ** value2
        case _: # "default" case that matches any pattern
            return None

# ## Matching a Pattern of One Numeric Value
# * Next snippet matches the case in which `args` contains one value (`7`)
# > ```case [value]: # no operation specified; just return value``` 

calculate(7) # When no operation specified, returns argument

# * Case pattern uses list syntax (`[]`), but `match`…`case` **can match patterns in collections that have similar structures**
#     * Thus, the name “structural pattern matching”
# * Here, the `args` tuple and the case’s list are each sequences containing one element
# * Python assigns `7` to the variable `value`
# * Did not specify an operation in the function call, so this `case` simply returns the value

# ## Matching a Pattern of an Operator and a Numeric Value
# * Next snippet matches a `case` in which the list args contains two elements
# > ```case [op, value] if op == '+' or op == '-': # unary op```
calculate('-', 5) # unary minus

# * Match is **guarded** by an `if` clause
# * First element—represented by `op`—must be either `'+'` or `'-'`
#     * Representing unary plus and minus operations
# * Python assigns `'-'` to `op` and `5` to `value`
# * `case` returns `-value` (that is, `-5`)

# ## Matching a Pattern of an Operator and a Numeric Value
# * Next several snippets handle binary arithmetic operations—addition, subtraction,
# multiplication, division and exponentiation

calculate(4, '+', 3) # 4 + 3

calculate(7, '-', 2) # 7 - 2

calculate(3, '*', 4) # 3 * 4

calculate(10, '/', 2) # 10 / 2

calculate(7, '%', 3) # 7 % 3

calculate(10, '**', 2) # 10 ** 2


# * Each corresponding case matches a three-element `args`
# * Middle element must explicitly match a literal string

# ## Matching the Irrefutable `case` 
# * Snippet that does not represent a valid operation
# * `calculate` returns `None` 

if calculate(10, '+') == None: # error: missing right operand 
    print('calculate did not return a value')



# # Positional-Only Parameters 
# > **Python 3.8**, Section 4.10  
# > PEP 570 – Python Positional-Only Parameters: https://peps.python.org/pep-0570/
# 
# * Consider the following `average` function

def average(number1, number2, number3):
    return (number1 + number2 + number3) / 3;

# * Can call this with positional arguments that are assigned left-to-right to the corresponding parameters

average(7, 20, 15) # positional arguments

# * Also can call with keyword arguments where each argument is assigned to the specifically named parameter—order of the arguments does not matter

average(number3=15, number1=7, number2=20) # keyword arguments

# * Using keyword arguments here actually makes the function call less clear
#     * Listed the parameter names out of order from function’s definition 
# * To prevent calls like this, can specify **positional-only parameters**
# * Parameters before a `/` in a parameter list are positional-only and do not allow keyword arguments
# * Can specify both positional-only and keyword arguments by listing the parameters that accept keyword arguments after the `/` in the parameter list.

def average(number1, number2, number3, /):
    return (number1 + number2 + number3) / 3;

average(number3=15, number1=7, number2=20) # keyword arguments



# # `Enum`s for Creating Named Constants 
# > **Python 3.4**, Section 4.5, Fig. 4.2  
# > `enum`—Support for enumerations  
# > * https://docs.python.org/3/library/enum.html
# > 
# > Note: This is an item we should have covered in 1/e.
# 
# ## Defining a Simple `Enum` with Underlying Integer Values
# * `Enum` can be used to define sets of named constants
# * Following code uses `Enum` to define the type `GameStatus` with constants `WON`, `LOST` and `CONTINUE`: 

from enum import Enum

GameStatus = Enum('GameStatus', ['WON', 'LOST', 'CONTINUE'])

# * Access in code as `GameStatus.WON`, `GameStatus.LOST` and `GameStatus.CONTINUE`
# * By default, constants have underlying integer values starting at 1 and incrementing by 1

GameStatus.WON

GameStatus.LOST

GameStatus.CONTINUE


# ## Defining an `Enum` with Specific Integer Values
# * Can supply
#     * Sequence of tuples representing names and values of each constant or
#     * Dictionary of key–value pairs from which the keys will be used as the constant names and the key’s corresponding values are the constants’ values
# * `RollValues` enumeration defines named constants representing specific sums of rolling two dice in our Craps dice-game simulation:

RollValues = Enum('RollValues', [('SNAKE_EYES', 2), ('TREY', 3),
    ('SEVEN', 7), ('YO_LEVEN', 11), ('BOX_CARS', 12)])

RollValues.SNAKE_EYES

RollValues.BOX_CARS

# ## Getting an `Enum` Constant’s Name and Value 
# Each `Enum` constant has `name` and `value` attributes

RollValues.BOX_CARS.name

RollValues.BOX_CARS.value


# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
