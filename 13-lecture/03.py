# static class
class House:

    def __init__(self, color, area):

        self.color = color

        self.area = area  # Area in square meters

 

    @staticmethod

    def is_valid_area(area):

        # Static method to validate if the area value is reasonable (positive)

        return area > 0

 

# Using the static method to validate area before creating a House instance

print(House.is_valid_area(120))   # Expected output: True

print(House.is_valid_area(-50))   # Expected output: False