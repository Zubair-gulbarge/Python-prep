# Basic Input and Output:

# Input: Read two numbers from the user and print their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print("Sum:", result)


# Conditional Statements:

# Check if a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Loops:

# Print the first n natural numbers.
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    print(i)


# Functions:

# Calculate the factorial of a number using a function.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial:", result)

# Lists:

# Find the sum of elements in a list.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum:", total)

# Dictionaries:

# Create a dictionary of students and their grades.
students = {'Alice': 90, 'Bob': 85, 'Charlie': 78}
print("Bob's grade:", students['Bob'])

# String Manipulation:

# Count the number of vowels in a string.
text = "Hello, World!"
vowels = 'AEIOUaeiou'
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


# File Handling:

# Read and print the contents of a text file.
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Exception Handling:

# Handle an exception and display an error message.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# List Comprehensions:

# Create a list of squares of even numbers from 1 to 10.
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Squares of even numbers:", squares)
