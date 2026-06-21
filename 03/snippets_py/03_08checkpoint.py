## 3.8 while Iteration Statement

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

product = 7

while product <= 1000:
    product = product * 7

product

import math

def find_power_of_two_math():
    """
    Determines the first power of 2 greater than one million using logarithms.
    (Requires Python's 'math' module)
    """
    target = 1_000_000
    # We need the smallest integer exponent N such that 2^N > target
    # This is equivalent to ceil(log2(target + epsilon))
    # A simpler robust approach is to calculate log2(target) and take the next integer.
    exponent = math.ceil(math.log2(target + 1e-9)) # Add small epsilon for safety
    return 2**int(exponent)

print(find_power_of_two_math())

##########################################################################
# (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
