# Define a decorator function that takes another function as an argument
def log_decorator(func):                    
    # Define a wrapper function that will modify the behavior of the original function
    def wrapper():  
        print(f'Calling function: {func.__name__}')  # Print the name of the function being called
        return func()  # Call the original function
    return wrapper  # Return the modified function

# Apply the decorator to the 'say_hello' function using @log_decorator
@log_decorator  
def say_hello():                
    print('Laiba')  # This function simply prints "Hello!"

# Call the decorated function
say_hello()  

# Output:
# Calling function: say_hello
# Laiba!