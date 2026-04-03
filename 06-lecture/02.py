counter = 0  # Global variable

def increment():
    global counter  # Explicitly modifying global variable
    counter += 1

increment()
print('Updated counter:', counter)


a = [1, 2, 3]
b = a  # Both point to the same object
c = [1, 2, 3]  # Different object with same values

print(a is b)  # Output: True
print(a is c)  # Output: False