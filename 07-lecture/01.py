#used higher order function
# Function to double a number
def double(x):
    return x * 2

# Using map() to double numbers in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]