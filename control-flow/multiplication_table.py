x = int (input ("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    z = x * y
print(f"{x} * {y} = {z}")
# multiplication_table.py

# Prompt the user to enter a number
# The input is saved in a variable named 'number'
number_input = input("Enter a number to see its multiplication table: ")

# Convert the input string to an integer
# For this exercise, we assume the user will enter a valid whole number.
number = int(number_input)

# Print a header for the multiplication table for clarity
print(f"\nMultiplication Table for {number}:\n")

# Use a for loop to iterate through numbers from 1 to 10 (inclusive)
for i in range(1, 11):
    # Calculate the product of the user's number and the current iterator 'i'
    product = number * i
    
    # Print each line of the multiplication table in the specified format: "X * Y = Z"
    # X is 'number', Y is 'i', and Z is 'product'
    print(f"{number} * {i} = {product}")
