# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Apple", "Banana", "Orange", "Pear", "Plum"]
# TODO: Use a for loop to print each fruit in the list
for a in fruits:
  print(a)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
import time
count=5
while count > 0:
  print("Time remainning in: ",count)
  count -= 1
  time.sleep(1)
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for a in range(1, 11):
  square = a**2
  print(square)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
# TODO: Use a for loop to select and print 3 random colors from the list
random_colors = random.sample(colors, k=3)

for colors in random_colors:
  print(colors)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
# TODO: Use a while loop to create a simple calculator
while True:
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  operation = input("Enter choice: ")

  if operation == "5":
      print("Exiting Calculator...")
      break

  if operation in ("1", "2", "3", "4"):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Use numerical values only!")
      continue

    if operation == "1":
      print(f"Answer: {num1} + {num2} = {math_operations.add(num1, num2)}")

    if operation == "2":
      print(f"Answer: {num1} - {num2} = {math_operations.subtract(num1, num2)}")

    if operation == "3":
      print(f"Answer: {num1} * {num2} = {math_operations.multiply(num1, num2)}")

    if operation == "4":
      print(f"Answer: {num1} / {num2} = {math_operations.divide(num1, num2)}")

  else:
    print("Invalid selection! Please select a valid option from the menu!")