#
# Look to see how this program works
#
# There are some deliberate errors in the program
# Can you find them and fix them?
#
# print must start with a lower case letter
print("I'm ******, pleased to meet you")
# There is a missing " before What's
name = input("What's your name? ")
happy = input("Hello " + name + " are you feeling happy today? ") 
# A comparison in a condition has double =
if happy == "yes":
    print("That's good, I'm glad you are happy")
# There must be a colon : after the condition
elif happy == "no":
    print("I am sorry to hear that")
else:
    print("I didn't understand what you said!")

