
# Take full name as input
name = input("Enter your full name (first and last name): ")

# Find the space index to separate first and last name
space = name.find(" ")

# Slice first and last name using string slicing
first_name = name[:space]
last_name = name[space+1:]

# Print sliced names
print("\n--- Name Details by Maham ---")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")


print("\n---Mini Calculator by Maham ---")
# Take two numeric inputs from the user
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

# Display results using formatted print statements
print("\n--- Arithmetic Operations ---")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {multiply}")
print(f"Division: {div}")
