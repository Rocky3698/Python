"""
Common Python Exceptions:
ZeroDivisionError: Raised when dividing by zero.
ValueError: Raised when a function gets an argument of the correct type but an invalid value.
IndexError: Raised when accessing an invalid index of a list or tuple.
KeyError: Raised when trying to access a dictionary with a key that doesn't exist.
FileNotFoundError: Raised when trying to open a file that does not exist.
"""

# Basic Exception Handling with try and except:

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the exception occurs
    print("You can't divide by zero!")

# Example
try:
    result = int(input("Enter a number: "))
    print(10 / result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a number.")


# else and finally Clauses:

try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("The division was successful.")
finally:
    print("This will always execute.")

# Example

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print(content)
finally:
    file.close()
    print("File closed.")


# Raising Exceptions:
age=-1
if age < 0:
    raise ValueError("Age cannot be negative")

# Example

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    print(check_age(-5))
except ValueError as e:
    print(f"Error: {e}")



# Custom Exceptions:

class NegativeNumberError(Exception):
    def __init__(self, message="Negative number entered"):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise NegativeNumberError()
    return number

try:
    print(check_positive(-10))
except NegativeNumberError as e:
    print(f"Error: {e}")