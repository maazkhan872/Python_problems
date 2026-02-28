"""
# Ask user for their name
name = input("Enter your name: ")

# Ask user for their age
age = input("Enter your age: ")

print("Hello", name + "! You are", age, "years old.") 

# Converting Input to Number
# Get numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform addition
sum = num1 + num2

print("Sum of", num1, "and", num2, "is", sum) 

# Calculator Problem
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Greeting by Age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Hello", name + ", You are eligible to vote!")
else:
    print("Hello", name + ", Too young to vote.") """