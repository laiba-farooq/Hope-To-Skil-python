#Basic try-except Structure
try:
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    # Attempt to divide 10 by the entered number
    print(10 / num)  
except ZeroDivisionError:
    # Handle the case where the user enters zero
    print("Error! You cannot divide by zero.")

     #Handling Multiple Exceptions
try:
    # Prompt the user to enter the first number
    num1 = int(input('Enter first number: '))
    # Prompt the user to enter the second number
    num2 = int(input('Enter second number: '))
    # Attempt to divide the first number by the second number
    result = num1 / num2
    # Print the result of the division
    print('Result:', result)
except ZeroDivisionError:
    # Handle the case where the second number is zero
    print('Error: Cannot divide by zero!')
except ValueError:
    # Handle the case where the input is not a valid integer
    print('Error: Invalid input! Please enter numbers only.')