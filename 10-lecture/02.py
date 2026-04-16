try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num  # May raise ZeroDivisionError
    print("Result:", result)
except Exception as e:  # Catching all exceptions
    print("An error occurred:", e)
#using finaly block
try:
    # Attempt to open the file in read mode
    file = open("example.txt", "r")
    # Read the content of the file
    content = file.read()
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("File not found!")
finally:
    # This block runs no matter what
    print("Closing file...")
    file.close()