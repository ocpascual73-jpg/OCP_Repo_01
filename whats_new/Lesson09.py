# # What's New: Lesson 9, Files and Exceptions
# # In This Segment
# ## Python 3.11
# * Adding Notes to Exceptions
# * Exception Groups and `except*`



# # Adding Notes to Exceptions
# > **Python 3.11, Lesson 9** 
# > PEP 678, Enriching Exceptions with Notes
# > https://peps.python.org/pep-0678/.
# 
# * Can call `add_note()` on an exception object to provide additional information
# * Notes appear after the exception’s error message in tracebacks

try:
    print(10 / 0)
except ZeroDivisionError as e:
    e.add_note('Denominator must be non-zero.')
    raise # re-raise the current exception



# # Exception Groups and `except*`
# > **Python 3.11**, New Section  
# > PEP 654, Exception Groups and `except*`  
# https://peps.python.org/pep-0654/
# 
# * Enables programs to raise and handle multiple unrelated exceptions simultaneously
# * Primarily for concurrent and parallel programming
#     * Multiple tasks could raise exceptions that should be caught at the same time

# ## `ExceptionGroup`
# * Contains an error message and a list of exception objects
# * Can catch an `ExceptionGroup` using an `except` handler with an `as` clause, then use the variable name to access `ExceptionGroup`’s `exceptions` property and iterate through the exceptions
# * Also can use multiple `except*` handlers to filter the `ExceptionGroup`’s exceptions, looking for those that match a specified type
# * `ExceptionGroupDemo.py` demonstrates `ExceptionGroup` and `except*`

# In[ ]:

run ExceptionGroupDemo.py


# ## Raising an ExceptionGroup
# * Function `parallel_task_simulator` (lines 5–26) executes three `try` statements
# * Each purposely raises an exception, then
#     * catches it,
#     * displays its string representation and
#     * adds it to list `exceptions`
# * Function raises an `ExceptionGroup` (line 26) with custom error message and list of previously caught exceptions

# ## Main Part of Script—Catching and Processing an `ExceptionGroup`
# `try` statement in lines 31–39 
# * Line 32 calls `parallel_task_simulator`, which raises an `ExceptionGroup`
# * Line 33 catches the raised `ExceptionGroup` 
# * Line 34 prints the `ExceptionGroup`’s string representation
# * Lines 37–39 iterate through the `ExceptionGroup`’s exceptions list and
#     * displays each exception’s type name (obtained by the expression `type(e).__name__`) and
#     * string representation

# ## Main Part of Script—Catching and Filtering an `ExceptionGroup` with `except*`
# `try` statement in lines 43–56 
# * Line 45 catches `ExceptionGroup` object as `ex1`, but exposes only `ValueErrors` in its exceptions list 
# * Line 51, catches `ExceptionGroup` object as `ex2`, but exposes only `ZeroDivisionError` in its exceptions list
# * Python will re-raise any uncaught exceptions in `ExceptionGroup`’s exceptions list
# 

# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
