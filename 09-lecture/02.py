try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print('File Content:', content)
except FileNotFoundError:
    print('Error: The file does not exist!')

#2
    with open('example.txt', 'w') as file:
     file.write('This is a new file created using write mode.')
print('File written successfully.')

#3
with open('example.txt', 'a') as file:
    file.write('\nThis is a new line added using append mode.')
print('New content appended successfully.')