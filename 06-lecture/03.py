a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # Output: True (Same values)
print(a is b)  # Output: False (Different objects in memory)
print(c is a) 


a = 1000
b = 1000
print(a is b)  # Output: False (Different memory locations)

a = 257
b = 257
print(a is b)  # Output: True (same memory locations)
# Reason: Python caches small integers (from -5 to 256)

c = 10
d = 10
print(c is d)