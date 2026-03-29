cubes = (x ** 3 for x in range(1, 11))   # Create a generator for cubes of numbers 1 through 10
print("Cubes generated:")
for cube in cubes:                       # Iterate through the generator to print each cube
    print(cube)