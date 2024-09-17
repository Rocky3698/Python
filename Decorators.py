# A decorator is a function that takes another function (or method) as an argument, adds some functionality to it, and returns a new function with the added behavior. It allows you to separate concerns and keep your code DRY (Don’t Repeat Yourself).

# Basic Syntax:
def decorator_function(original_function):
    def wrapper_function():
        # Code to execute before the original function
        result = original_function()
        # Code to execute after the original function
        return result
    return wrapper_function

# Defining a Decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the Decorator:
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# OutPut:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


