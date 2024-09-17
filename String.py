# String methods
text = "Python Programming"
name = "Rocky"
print(text.upper())  # Converts to uppercase
print(text.lower())  # Converts to lowercase
print(text.startswith("Py"))  # Checks if starts with
print(text.replace("Python", "Java"))  # Replace text

# String formatting
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)

s = "new string"

print(s.title())

text = "Hello, World!"

# String Length
print(len(text))  # Output: 13

# String Slicing (access parts of the string)
print(text[0:5])  # Output: 'Hello'
print(text[-1])   # Output: '!' (last character)
print(text[::2])  # Output: 'Hlo ol!' (every second character)

# String Case Conversion
print(text.upper())  # Output: 'HELLO, WORLD!'
print(text.lower())  # Output: 'hello, world!'
print(text.capitalize())  # Output: 'Hello, world!'
print(text.title())  # Output: 'Hello, World!'

# Searching in Strings
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))  # Output: True
print(text.find("World"))  # Output: 7 (position of "World" in text)

# Modifying Strings
print(text.replace("World", "Python"))  # Output: 'Hello, Python!'

# Removing Whitespace
text_with_spaces = "   Python   "
print(text_with_spaces.strip())  # Output: 'Python'
print(text_with_spaces.lstrip())  # Output: 'Python   '
print(text_with_spaces.rstrip())  # Output: '   Python'

# Splitting and Joining Strings
sentence = "Python is great"
words = sentence.split()  # Splits into a list of words
print(words)  # Output: ['Python', 'is', 'great']
joined_sentence = " ".join(words)  # Joins list into a string
print(joined_sentence)  # Output: 'Python is great'

# Checking for Substrings
print("Python" in sentence)  # Output: True
print("Java" in sentence)    # Output: False
