import json

# Sample dictionary
data = {'name': 'Haris', 'age': 25, 'city': 'Lahore'}

# Writing JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON data from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
    
#2

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error: The file does not exist!')