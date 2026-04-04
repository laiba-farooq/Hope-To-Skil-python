# Function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Using filter() to get only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)  # Output: [2, 4, 6]


