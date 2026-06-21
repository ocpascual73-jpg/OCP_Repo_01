# ExceptionGroupDemo.py
# Demonstrating raising and filtering ExceptionGroups.
from exceptiongroup import ExceptionGroup

def parallel_task_simulator():
    exceptions = [] # store exceptions for an ExceptionGroup

    try:
        10 / 0 # force ZeroDivisionError
    except ZeroDivisionError as ex:
        print(f'   1. {ex}')
        exceptions.append(ex)

    try:
        int('hello') # force ValueError
    except ValueError as ex:
        print(f'   2. {ex}')
        exceptions.append(ex)

    try:
        float('hello') # force ValueError
    except ValueError as ex:
        print(f'   3. {ex}')
        exceptions.append(ex)

    raise ExceptionGroup('Several exceptions raised', exceptions)
    
# main part of script
print('Call parallel_task_simulator and catch ExceptionGroup')

try:
    parallel_task_simulator()
except ExceptionGroup as ex:
    print(f'\nString representation of ExceptionGroup:\n   {ex}')
    print('\nIndividual exceptions in ExceptionGroup:')

    for e in ex.exceptions:
        exception_type = type(e).__name__
        print(f'   {exception_type}: {e}')

print('\nUse except* to filter specific exception types')

try:
    parallel_task_simulator()
except* ValueError as ex1:
    print('\nCaught ValueError(s)')

    for e in ex1.exceptions:
        exception_type = type(e).__name__
        print(f'   {exception_type}: {e}')
except* ZeroDivisionError as ex2:
    print('\nCaught ZeroDivisionError(s)')

    for e in ex2.exceptions:
        exception_type = type(e).__name__
        print(f'   {exception_type}: {e}')
