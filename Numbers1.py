# Numbers1.py
#
# Extend this program so that it deals with all operations
# Can you make it print an error message if the op is not recognised?
#

print("**** Calculator ****")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
op = input("Enter +, -, * or / :")
if op == "+":
    print("Answer = ", number1 + number2)

# Extension
#
# Use the shell window to investigate what %, **, and // do.
# [for example type in 7 % 3, 11 % 3, etc and look at the answers]
# Extend your program to work for %, **, and //.
#
# Can you make the program repeat forever, rather than you
# having to re-run it each time?
#
