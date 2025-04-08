# Naming Conventions

# wrong
VariableName = 5  # wrong
def MyFunction():  # wrong
    pass

# correct
variable_name = 5  # correct
def my_function():  # correct
    pass

# Indentation

# wrong
def say_hello():
print("Hello")  # wrong

# correct
def say_hello():
    print("Hello")  # correct

# Line Length

# wrong
def some_function():
    print("This is a very long line that exceeds seventy-nine characters, which is not good according to PEP8")  # wrong

# correct
def some_function():
    print(
        "This is a very long line "
        "that is split into two lines "
        "to follow PEP8 guidelines."
    )  # correct

# Spaces Around Operators

# wrong
x=5+3  # wrong

# correct
x = 5 + 3  # correct

# Blank Lines

# wrong
def function_one():
    pass
def function_two():
    pass  # wrong

# correct
def function_one():
    pass


def function_two():
    pass  # correct

# Imports

# wrong
import sys, os  # wrong

# correct
import sys
import os  # correct

# String Quotes (single or double - be consistent)

# wrong
name = "John"  # double quotes
surname = 'Doe'  # single quotes - wrong if not consistent

# correct
name = "John"
surname = "Doe"  # correct (both double quotes used)

# Comments

# wrong
#This is a comment with no space  # wrong

# correct
# This is a comment with a space  # correct
