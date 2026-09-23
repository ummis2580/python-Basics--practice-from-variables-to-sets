"""
PYTHON BASICS — PRACTICE FROM VARIABLES TO SETS
===============================================

Author: Umme
Topics: Variables, Data Types, Strings, Conditionals,
Lists, Tuples, Dictionaries, Sets, and Bonus Challenge.

This file contains my Python fundamentals practice.
"""

# ============================================================
# SECTION 1: VARIABLES
# ============================================================
print("=" * 50)
print("SECTION 1: VARIABLES")
print("=" * 50)

name = "umme"
print(name)
age = 21
print(age)
height = 1.78
print(height)

info = f"My name is {name}, I am {age} years old and {height}m tall."
print(info)

a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")


# ============================================================
# SECTION 2: DATA TYPES
# ============================================================
print("\n" + "=" * 50)
print("SECTION 2: DATA TYPES")
print("=" * 50)

print(type(name))
print(type(age))
print(type(height))

stu1 = 54
stu2 = 60
print(type(stu1 > stu2))

fruits_list = ["mango", "banana", "orange"]
print(type(fruits_list))

fruits_tuple = ("mango", "banana", "orange")
print(type(fruits_tuple))

student = {
    "name": "abc college",
    "age": 22,
}
print(type(student))

# Type conversion
num_str = "42"
result = int(num_str) + 8
print(result)  # 50

num_float = 3.99
result2 = int(num_float)
print(result2)  # 3 (truncates, doesn't round)

score = 100
result3 = str(score) + " points"
print(result3)  # "100 points"


# ============================================================
# SECTION 3: STRINGS
# ============================================================
print("\n" + "=" * 50)
print("SECTION 3: STRINGS")
print("=" * 50)

sentence = "Python is a fun and powerful programming language"
print(sentence.upper())
print(sentence.lower())
print(sentence.count("a"))
print(sentence.replace("fun", "awesome"))
print(sentence.split())
print(sentence[0:6])
print(sentence[::-1])
print("Python" in sentence)

words = sentence.split()
print(f"The sentence has {len(words)} words and {len(sentence)} characters.")


# ============================================================
# SECTION 4: CONDITIONALS
# ============================================================
print("\n" + "=" * 50)
print("SECTION 4: CONDITIONALS")
print("=" * 50)

number = -7
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

score = 76
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

check_num = 15
if check_num % 3 == 0 and check_num % 5 == 0:
    print("FizzBuzz")
elif check_num % 3 == 0:
    print("Fizz")
elif check_num % 5 == 0:
    print("Buzz")
else:
    print(check_num)

username = "admin"
password = "wrongpass"
if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")


# ============================================================
# SECTION 5: LISTS
# ============================================================
print("\n" + "=" * 50)
print("SECTION 5: LISTS")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[-1])
fruits.append("fig")
fruits.remove("banana")
fruits.insert(0, "avocado")
print(sorted(fruits))

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)
print(len(fruits))


# ============================================================
# SECTION 6: TUPLES
# ============================================================
print("\n" + "=" * 50)
print("SECTION 6: TUPLES")
print("=" * 50)

coordinates = (10, 20)
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

person = ("Alice", 30, "Engineer")
p_name, p_age, p_job = person
print(f"{p_name} is {p_age} years old and works as an {p_job}.")

favorites = ("jab we met", "when i fall towards u", "kgf2")
print(favorites)

print("Engineer" in person)

fruits_tuple2 = tuple(fruits)
print(fruits_tuple2)


# ============================================================
# SECTION 7: DICTIONARIES
# ============================================================
print("\n" + "=" * 50)
print("SECTION 7: DICTIONARIES")
print("=" * 50)

student = {
    "name": "Emma",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student["name"])
print(student["major"])

student["graduated"] = False
student["gpa"] = 3.9
del student["age"]
print(student)

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")

print(student.get("scholarship", "Not specified"))

words_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")


# ============================================================
# SECTION 8: SETS
# ============================================================
print("\n" + "=" * 50)
print("SECTION 8: SETS")
print("=" * 50)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)   # union
print(set_a & set_b)   # intersection
print(set_a - set_b)   # difference

set_a.add(10)
print(set_a)
set_a.remove(1)
print(set_a)
print(3 in set_a)

numbers_with_dupes = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_numbers = set(numbers_with_dupes)
print(unique_numbers)

list1_friends = ["Alice", "Bob", "Charlie", "David"]
list2_friends = ["Charlie", "David", "Eve", "Frank"]
common = set(list1_friends) & set(list2_friends)
print(common)


# ============================================================
# BONUS CHALLENGE: Combine everything!
# ============================================================
print("\n" + "=" * 50)
print("BONUS CHALLENGE")
print("=" * 50)

students = [
    ("John", 85),
    ("Sara", 45),
    ("Mike", 92),
    ("Lily", 67),
]

for name, score in students:
    if score >= 90:
        print(f"{name} scored {score} and got a A")
    elif score >= 80:
        print(f"{name} scored {score} and got a B")
    elif score >= 70:
        print(f"{name} scored {score} and got a C")
    elif score >= 60:
        print(f"{name} scored {score} and got a D")
    else:
        print(f"{name} scored {score} and got a F")
