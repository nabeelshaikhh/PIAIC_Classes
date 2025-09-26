# -------------------------------------------
# Class_02 - Python Basics (PIAIC Q1)
# Topics: Print, Variables, Data Types, Operators
# -------------------------------------------

# Printing a message
print("Hello, World!")   # Output: Hello, World!

# Variables
name = "Nabeel"
number = 02
print(number)            # Output: 02

# -------------------------------------------
# Data Types
# -------------------------------------------
# 1. String
print("Nabeel")           # Output: Nabeel

# 2. Integer
print(2)                 # Output: 2

# 3. Float
print(5.5)               # Output: 5.5

# 4. Boolean
print(True)             # Output: True

# Checking types
user_name = "Nabeel"
print(type(user_name))   # Output: <class 'str'>

number = 20
print(type(number))      # Output: <class 'int'>

floating_number = 2.4
print(type(floating_number))  # Output: <class 'float'>

boolean_number = True
print(type(boolean_number))   # Output: <class 'bool'>

# -------------------------------------------
# Operators
# -------------------------------------------

# 1. Arithmetic Operators
print(2 + 2)   # Output: 4 (Addition)
print(10 - 5)  # Output: 5 (Subtraction)
print(10 * 2)  # Output: 20 (Multiplication)
print(20 / 2)  # Output: 10.0 (Division)
print(10 // 3) # Output: 3 (Floor Division)
print(10 % 3)  # Output: 1 (Modulus)
print(2 ** 3)  # Output: 8 (Exponentiation)

# 2. Comparison Operators
num1, num2 = 10, 5
print(num1 == num2)  # Output: False
print(num1 > num2)   # Output: True
print(num1 < num2)   # Output: False
print(num1 != num2)  # Output: True

# 3. Assignment Operators
num1 = 20
num2 = num1 + 5
print(num2)   # Output: 25

num3 = num1 - 5
print(num3)   # Output: 15

num4 = num1 * 5
print(num4)   # Output: 100

num5 = num1 / 5
print(num5)   # Output: 4.0

# 4. Logical Operators
num1, num2 = 10, 20
print(num1 != num2 and num1 < num2)  # Output: True
print(num1 != num2 and num1 > num2)  # Output: False
print(num1 != num2 or num1 > num2)   # Output: True

# -------------------------------------------
# Working with Data Structures
# -------------------------------------------
num1, num2 = 10, 20
print(num1, num2)                        # Output: 10 20
print("num1 added by num2", num1+num2)   # Output: num1 added by num2 30

# Strings to collections
x = "hello"
print(list(x))    # Output: ['h', 'e', 'l', 'l', 'o']
print(tuple(x))   # Output: ('h', 'e', 'l', 'l', 'o')
print(set(x))     # Output: {'h', 'e', 'o', 'l'}

# Dictionary from tuples
data = [("name", "Ali"), ("age", 20)]
print(dict(data)) # Output: {'name': 'Ali', 'age': 20}

# Range
print(list(range(1, 11))) # Output: [1,2,3,4,5,6,7,8,9,10]
