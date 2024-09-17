name = input("Enter your name: ")
print(name, type(name))  # Output: string

age = int(input("Enter your age: "))
print(age, type(age))  # Output: integer

height = float(input("Enter your height (in meters): "))
print(height, type(height))  # Output: float


is_student = input("Are you a student? (True/False): ")
is_student = is_student.lower() == "true"  # Convert input to lowercase and check if it's "true"
print(is_student, type(is_student))  # Output: boolean


# Input a list of integers
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # Convert each element to an integer
print(numbers, type(numbers))  # Output: list of integers

# Input a list of integers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(numbers)  # Output: [1, 2, 3, 4]


# Input a tuple of floats
numbers = input("Enter floating-point numbers separated by spaces: ").split()
numbers = tuple(float(num) for num in numbers)  # Convert each element to a float and cast to a tuple
print(numbers, type(numbers))  # Output: tuple of floats
