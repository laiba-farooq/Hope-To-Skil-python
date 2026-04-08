#Creating Custom Exceptions
def withdraw(amount):
    # Check if the amount is negative
    if amount < 0:
        # Raise a ValueError if the amount is negative
        raise ValueError("Amount cannot be negative!")
    # Print the withdrawal amount
    print(f"Withdrawing ${amount}")

try:
    # Attempt to withdraw a negative amount
    withdraw(-100)
except ValueError as e:
    # Handle the ValueError and print the error message
    print(f"Error: {e}")