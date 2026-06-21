## 3.7 match…case Selection Statement

### Checkpoint 1 Snippets

### Checkpoint 2 Snippets

gpa = 3

match gpa:
    case 4:
        print('A')
    case 3:
        print('B')
    case 2:
        print('C')
    case 1:
        print('D')
    case 0:
        print('F')
    case _:
        print('Invalid GPA')

def get_grade(grade: int) -> str:
    match grade:
        # Case for 90 and above (Grade A)
        case _ if grade >= 90:
            return 'A'
        # Case for 80 up to 89 (Grade B)
        case _ if grade >= 80:
            return 'B'
        # Case for 70 up to 79 (Grade C)
        case _ if grade >= 70:
            return 'C'
        # Case for 60 up to 69 (Grade D)
        case _ if grade >= 60:
            return 'D'
        # Default case (Anything less than 60, or the final else)
        case _:
            return 'F'

# Example usage:
print(f"Grade 95 -> {get_grade(95)}")
print(f"Grade 82 -> {get_grade(82)}")
print(f"Grade 70 -> {get_grade(70)}")
print(f"Grade 61 -> {get_grade(61)}")
print(f"Grade 45 -> {get_grade(45)}")

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
