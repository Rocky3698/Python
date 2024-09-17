# Basic Function Definition

def greet():
    print("Hello, world!")

# Functions with Parameters

def greet(name):
    print(f"Hello, {name}!")

# Functions with Return Values
def add(a, b):
    return a + b

# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Rocky")  # Output: Hello, Rocky!

# Keyword Arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")
describe_person(name="Rocky", age=25, city="New York")


# Arbitrary Arguments (*args and **kwargs)
# *args: Used to pass a non-keyworded, variable-length argument list.
# **kwargs: Used to pass a keyworded, variable-length argument list.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Rocky", age=25, city="New York")
# Output:
# name: Rocky
# age: 25
# city: New York


# Lambda Functions (Anonymous Functions)
# A lambda function is a small anonymous function that can take any number of arguments but only contains a single expression. It’s useful for simple, short operations.

# Syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))  # Output: 25


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


# Nested Functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")

# Function Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"



# Recursive Functions
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
