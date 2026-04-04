from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Using reduce() to multiply all numbers in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product)  # Output: 120