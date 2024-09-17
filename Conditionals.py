age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")


score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# Nested if Statements:

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

if age < 18:
    if is_student == 'yes':
        print("You are a minor and a student.")
    else:
        print("You are a minor but not a student.")
else:
    print("You are an adult.")


# Ternary (Conditional) Operator
age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)

# Chained Comparisons
x = 10
if 5 < x < 15:
    print("x is between 5 and 15")

# Check if any number is greater than 10
numbers = [4, 11, 15, 7, 3]
if any(num > 10 for num in numbers):
    print("There is a number greater than 10")
# Check if all numbers are positive
if all(num > 0 for num in numbers):
    print("All numbers are positive")
# any(): Returns True if any of the values are True.
# all(): Returns True only if all values are True.


x = 10
y = 20
result = x > 5 and y  # This will assign `y` to `result` if `x > 5` is `True`
print(result)  # Output: 20


vowels = 'aeiou'
char = 'a'
if char in vowels:
    print(f"{char} is a vowel")
