def greet():
    return 'Hello!'

def call_function(func):
    return func()

print(call_function(greet))  # Output: 'Hello!'

#Basic Structure of a Decorator
#A decorator is a function that wraps another function to modify its behavior.
def decorator_function(original_function):
    def wrapper_function():
        # Add extra functionality
        return original_function()
    return wrapper_function