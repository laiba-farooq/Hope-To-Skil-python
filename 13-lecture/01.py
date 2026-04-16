# class instant
class House:

    def __init__(self, color):

        # 'self.color' stores the paint color for this specific house instance

        self.color = color

 

    def show_color(self):

        # Prints the color of this house instance using 'self'

        print(f"This house is painted {self.color}")

 

# Create an instance of House with color "blue"

my_house = House("blue")

 

# Call the method to display the house color

my_house.show_color()