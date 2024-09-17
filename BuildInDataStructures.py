# Lists (Mutable Ordered Collection)
# Lists are one of the most commonly used data structures in Python. They allow storing an ordered collection of items (of any type) and are mutable, meaning you can change their contents after creation.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = ["apple", 2, 3.5, True]  # Lists can contain mixed types

fruits.append("orange")      # Adds 'orange' to the end of the list
fruits.insert(1, "mango")    # Inserts 'mango' at index 1
fruits.remove("banana")      # Removes 'banana' from the list
print(fruits)                # Output: ['apple', 'mango', 'cherry', 'orange']

print(len(fruits))  # Output: 3
numbers = [3, 1, 4, 1, 5]
print(sorted(numbers))  # Output: [1, 1, 3, 4, 5]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5
print(sum(numbers))  # Output: 14
print(fruits.index("banana"))  # Output: 1
print(fruits.count("apple"))  # Output: 1
# append(), insert(), pop(), remove(), reverse(), sort(),

#           ***     ***     ***



# Tuples (Immutable Ordered Collection)
# A tuple is similar to a list but immutable, meaning you cannot modify its contents after creation. Tuples are useful for storing fixed collections of items.
coordinates = (10, 20)
person = ("Rocky", 25, "New York")
print(person[0])  # Output: Rocky
person_list = list(person)  # Convert to a list
person_list[1] = 30
person = tuple(person_list)  # Convert back to tuple
print(len(coordinates))  # Output: 2
nums = (5, 3, 2)
print(sorted(nums))  # Output: [2, 3, 5]
print(min(nums))  # Output: 2 / min(tuple), max(tuple), and sum(tuple)
print(coordinates.index(20))  # Output: 1
print(coordinates.count(10))  # Output: 1

#           ***     ***     ***


# Sets (Unordered Collection of Unique Elements)
# Sets are unordered, mutable, and contain unique elements (i.e., no duplicates). They are useful when you want to ensure all items in a collection are distinct.

my_set = {1, 2, 3, 3, 4}  # Duplicate elements are automatically removed
print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(5)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)            # Output: {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)  # Output: {3}
difference_set = set1.difference(set2)  # Output: {1, 2}
print(len(my_set))  # Output: 5
print(sorted(my_set))  # Output: [1, 2, 3]
# min(set), max(set), and sum(set): Work similarly to lists and tuples.
# set.isdisjoint(): Checks if two sets have no elements in common.



#           ***     ***     ***

# Dictionaries (Key-Value Pairs)
# Dictionaries store data as key-value pairs. They are mutable, and the keys must be unique. Dictionaries are useful for storing data that has a logical relationship between keys and values.

person = {
    "name": "Rocky",
    "age": 25,
    "city": "New York"
}

print(person["name"])   # Output: Rocky

person["age"] = 26      # Update value
person["email"] = "rocky@example.com"  # Add new key-value pair

del person["city"]      # Remove key-value pair

print(person.keys())    # Output: dict_keys(['name', 'age', 'email'])
print(person.values())  # Output: dict_values(['Rocky', 26, 'rocky@example.com'])
print(person.items())   # Output: dict_items([('name', 'Rocky'), ('age', 26), ('email', 'rocky@example.com')])
print(len(person))  # Output: 3
print(person.get("name"))     # Output: Rocky
print(person.get("email", "No email found"))  # Output: No email found
person.update({"city": "New York"})
print(person)  # Output: {'name': 'Rocky', 'age': 25, 'city': 'New York'}
age = person.pop("age") # Removes and returns the value for the given key.
print(age)  # Output: 25



"""
Feature         List	               Tuple	            Set	               Dictionary

Order	       Ordered	              Ordered	         Unordered	            Ordered

Mutable	        Yes	                    No	                 Yes	              Yes

Duplicates	    Yes	                    Yes	                  No	            Keys: No

Indexing	    Yes	                    Yes	                  No	          Yes (on keys)

Use Case	General-purpose	     Fixed collections	    Unique elements	    Key-value pairs
"""