# Using zip() to pair names and ages
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
paired = list(zip(names, ages))
print(paired)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Using enumerate() to print index and value
fruits = ['Apple', 'Banana', 'Cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f'{index}: {fruit}')