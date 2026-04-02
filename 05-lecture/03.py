# Function with *args (Tuple of Arguments)
def name(*names):
    print("Hello,", names[0], names[1], names[2])

name("James", "Buchanan", "Barnes")

# Function returning a full name
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

# Calling the function and printing result
print(name("James", "Buchanan", "Barnes"))