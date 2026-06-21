# # What's New: Lesson 6, Dictionaries and Sets
# # In This Segment
# ## Python 3.9
# * Dictionary Union Operators
# ## Python 3.0
# * Keyword-Only Parameters and Arbitrary Keyword Arguments



# # Dictionary Union Operators
# > **Python 3.9**, Section 6.2.8  
# > PEP 584, Add Union Operators To `dict`:  
# https://peps.python.org/pep-0584/
# 
# * Can merge dictionaries with the dictionary union operators `|` and `|=`

capitals1 = {'Belgium': 'Brussels',
             'Haiti': 'Port-au-Prince'}

capitals2 = {'Nepal': 'Kathmandu',
             'Uruguay': 'Montevideo'}


# * Following snippet merges `capitals1` and `capitals2` with `|`

capitals1 | capitals2


# * Creates new dictionary with the results 
# * Leaves original dictionaries unchanged
# * If both dictionaries have a key–value pair with same key, value for that key in
# merged dictionary will be value for that key in the right operand

capitals1

capitals2


# ## Merging a Dictionary's Key-Value Pairs into another Dictionary 
# * `|=` operator performs same task as `|` but modifies its left operand

capitals1 |= capitals2

capitals1

# * Right operand remains unchanged

capitals2



# # Keyword-Only Parameters and Arbitrary Keyword Argument Lists
# > **Python 3.0**, Lesson 6  
# > Python Tutorial Section 4.8.2, Keyword Arguments  
# https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments  
# > New section for Lesson 6 where we cover dictionaries 
# 

# ## Keyword-Only Parameters
# * Just as a function may specify positional-only parameters before a backslash (`\`) in the parameter list, a function may specify keyword-only parameters by placing an asterisk (`*`) in the parameter list
#     * Subsequent arguments must be passed as keyword arguments 

# ## Arbitrary Keyword Arguments
# * A function using parameter `*args` can receive any number of positional arguments
#     * Must place keyword arguments after positional arguments
# * If last parameter in a function’s parameter list is `**kwargs`, function may receive an arbitrary number of keyword arguments
# * Useful for
#     * Functions that receive any number of keyword arguments or
#     * Cases in which some keyword arguments are optional
# * Interpreter places extra keyword arguments in a dictionary and passes it to `kwargs`
#     * Short for “keyword arguments”
#     * You may use any valid identifier for this parameter

# ## Function That Receives Required and Optional Keyword Arguments 
# * Consider a `send_mail` function that simulates sending an email 

def send_email(*, sender, recipient, **kwargs):
    print(f'sender: {sender}\nrecipient: {recipient}')

    # display the optional keyword arguments, if any
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')
    else:
        print('\nNo additional keyword arguments.')


# * Most email systems require only the `sender`’s and `recipient`’s email addresses, so these are required
# * If `kwargs` contains data, `for` statement displays the additional key–value pairs
# * Call with just required arguments:

send_email(sender='test1@deitel.com', 
    recipient='test2@deitel.com')

# Call with required arguments as well as arguments for the email’s `subject` and `body`:

send_email(sender='test1@deitel.com',
    recipient='test2@deitel.com',
    subject='Testing send_email',
    body='Testing our email simulation function.')

# ## Expanding an Existing Dictionary’s Key-Value Pairs As Keyword Arguments
# * Can pass a dictionary of key-value pairs to `send_mail`

parameters = {
    'sender': 'test1@deitel.com',
    'recipient': 'test2@deitel.com',
    'subject': 'Testing send_email',
    'body': 'Testing our email simulation function.',
    'cc': 'test3@deitel.com',
    'bcc': 'test4@deitel.com'
}

# * Use `**` dictionary unpacking operator to extract the parameter dictionary’s key–value pairs and pass them as keyword arguments

send_email(**parameters)

# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
