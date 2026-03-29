names = ['Laiba', 'aliza', 'abobakar']   # List of names
ages = [20, 23, 25]                     # Corresponding list of ages
for name, age in zip(names, ages):      # zip pairs items from both lists together
    print(f"{name} is {age} years old")