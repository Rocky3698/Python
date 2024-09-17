# Iterating Over a List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Using range() in a for Loop
for i in range(5):  # Loops from 0 to 4 (5 is not included)
    print(i)

for i in range(1, 10, 2):  # Loops from 1 to 9, with a step of 2
    print(i)  # Output: 1, 3, 5, 7, 9

# while Loops
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count by 1 in each iteration

# Exiting the Loop Early
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)

# Skipping to the Next Iteration
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop when i equals 2
    print(i)


numbers = [1, 2, 3, 4, 5]
print(*numbers)  # Output: 1 2 3 4 5
print(*numbers, sep=', ')  # Output: 1, 2, 3, 4, 5
