with open('example.txt', 'r+') as file:
    content = file.read()
    print('Current Content:', content)
    file.write('\nAdding new content in read+write mode.')
print('Content updated successfully.')


# Writing to a file
with open('example.txt', 'w') as file:
    file.write('This is a new line.')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

    