class Student:
    def __init__(self, name, marks):
        self.name = name    # Attribute
        self.marks = marks  # Attribute

    # Ye aik Method hai (Action)
    def check_result(self):
        if self.marks >= 50:
            print(f"{self.name} pass ho gaya hai!")
        else:
            print(f"{self.name} fail ho gaya hai.")

# Object banaya
s1 = Student("Laiba", 85)

# Method ko call kiya
s1.check_result()