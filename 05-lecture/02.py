# Function with a default middle name
def name(fname, mname="aliza", lname="malika"):
    print("Hello,", fname, mname, lname)

# Calling function with only first name
name("laiba") 

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# Calling function using keyword arguments in any order
name(mname="izma", lname="areeba", fname="momal")