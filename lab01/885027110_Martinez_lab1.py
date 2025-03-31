# A) Numbers 
num1 = 10
num2 = 15
num3 = 20

result = ( num1 * num2 ) / num3 
print("Multiplication and Division Result: ", result)

# Modulus Operator
remainder = num1 % num3
print("Remainder of a Divided by b: ", remainder)

# Square and Cube Calculations
square = num1 ** num2 
cube = pow(num1, 3)
print("Square of a: ", square)
print("Cube of a: ", cube)

print("\n")

# B) Strings
name = "Andrew Martinez"
print("Full name: ", name)

# Name Split 
first_name, last_name = name.split()
print("First Name: ", first_name)
print("Last Name: ", last_name)

# Upper and Lower Case
print("Uppercase: ", name.upper())
print("Lowercase: ", name.lower())

# Reversed Name
print("Reversed name: ", name[::-1])

print ("\n")

# C) Lists
foods = ["Pizza", "Steak", "Potatoes", "Eggs", "Chicken"]

# Print
print("First food: ", foods[0])
print("Last food: ", foods[-1])

# Add
foods.append("Tacos")
foods.append("Salad")
print("Updated food list: ", foods)

# Remove

foods.remove("Pizza")
print("Final food list: ", foods)

# Sort

foods.sort()
print("Alpabetically sorted food list: ", foods)

