# Methods = Object’s Behavior
class House:
    # The constructor (__init__) method initializes the attributes of the object
    def __init__(self, color, size):
        self.color = color  # Attribute to store the color of the house
        self.size = size    # Attribute to store the size of the house

    # Method to describe the house
    def describe(self):
        print(f"The house is {self.color} and {self.size}.")

# Create an object of the House class with specific color and size
my_house = House("blue", "large")

# Call the describe method to print details about the house
my_house.describe()