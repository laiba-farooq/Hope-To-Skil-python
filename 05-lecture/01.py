# Defining a function named 'add' that takes two numbers as parameters
def add(num1, num2):
    """This function takes two numbers, adds them, and returns the sum."""
    print("Number 1:", num1)  # Printing first number
    print("Number 2:", num2)  # Printing second number
    addition = num1 + num2  # Adding numbers
    return addition  # Returning the result

# Calling the function and storing the result
res = add(2, 4)
print("Result:", res)  # Expected Output: 6