# Example 9: Using itertools to cycle through a list
import itertools

colors = ['red', 'green', 'blue']   # List of colors
counter = 0                         # Counter to limit the loop
print("Cycling through colors using itertools.cycle:")
for color in itertools.cycle(colors):  # Cycle through colors indefinitely
    print(color)
    counter += 1
    if counter == 6:  # Stop after 6 iterations to avoid an infinite loop
        break