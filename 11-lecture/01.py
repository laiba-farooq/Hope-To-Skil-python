#(OOP)
class House:
    # The constructor (__init__) method initializes the attributes of the object
    def __init__(self, color, size):
        self.color = color  # Attribute to store the color of the house
        self.size = size    # Attribute to store the size of the house

# Create an object of the House class with specific color and size
my_house = House("blue", "large")

# Print the color of the house object
print(my_house.color)