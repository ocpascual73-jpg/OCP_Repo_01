# # What's New: Lesson 8, Strings: A Deeper Look
# ## Python 3.9
# * Removing String Prefixes and Suffixes
# ## Python 3.8
# * Named Unicode Characters in Regular Expressions



# # Removing String Prefixes and Suffixes> **Python 3.9**, Section 8.4+  
# > PEP 616—String methods to remove prefixes and suffixes https://peps.python.org/pep-0616/

# * String methods `removeprefix` and `removesuffix` remove substrings from the beginningand end of a string, respectively

s = '<<<$$$>>>'

s.removeprefix('<<<')

s.removesuffix('>>>')

s



# # Named Unicode Characters in Regular Expressions
# > **Python 3.8**, Section 8.12
# > `re`—Regular expression operations  
# https://docs.python.org/3/library/re.html
# 
# * Can use `\u` or `\U` escape sequences to insert a Unicode character into string literals using four-digit or eight-digit hexadecimal code
# * Such escape sequences may not be used in regular-expression pattern strings
# * Can use `\N{`_name_`}` escape sequence to insert a Unicode character with a specified name in a regular expression pattern
#     * Names at https://www.unicode.org/charts/charindex.html
# * Define string `sample_text` containing the Unicode character É
#     * LATIN CAPITAL LETTER E WITH ACUTE

import re

sample_text = 'string with É character'

# * Use `\N{`_name_`}` escape sequence to define regular expression that matches only É 

regex_pattern = r'\N{LATIN CAPITAL LETTER E WITH ACUTE}'

match = re.search(regex_pattern, sample_text)

match.group()

# ©️Copyright 2024 by Pearson Education, Inc. All Rights Reserved. 
# The content in this notebook will be incorporated as new features 
# into the Second Editions our professional book 
#    Python for Programmers https://amzn.to/2VvdnxE 
# and our textbook
#    Intro Python for Computer Science and Data Science https://amzn.to/2YU0QTJ
