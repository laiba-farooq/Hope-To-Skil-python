 #Class Methods
class House:

    def __init__(self, color, age):

        self.color = color      # Instance attribute: specific color of this house

        self.age = age          # Instance attribute: how old the house is

 

    @classmethod

    def from_construction_year(cls, color, construction_year):

        # Class method to create a House object by calculating age from construction year

        return cls(color, 2024 - construction_year)

 

# Create a new house instance using the class method as a factory

my_house = House.from_construction_year("white", 2000)

 

# Print the age of the house instance

print(my_house.age)