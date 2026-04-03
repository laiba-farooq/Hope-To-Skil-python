x = 'global'  # Global variable

def outer_function():
    x = 'enclosing'  # Enclosing variable
    def inner_function():
        x = 'local'  # Local variable
        print('Inside inner function:', x)  # Prints local variable
    inner_function()
    print('Inside outer function:', x)  # Prints enclosing variable

outer_function()
print('Outside all functions:', x)