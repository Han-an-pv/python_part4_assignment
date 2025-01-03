# Python-Functions
# What does the len() function do in Python?

"""" The len() function returns the number of items in an object. """

# Write a code example using len() to find the length of a list.
newlist=[1,2,'aa','anil','a']
print(len(newlist))

# Write a Python function greet(name) that takes a person('s name as input and prints "Hello, [name]!".
def greet(name):
     print("Hello," + name+"!")
greet("Anu")

# Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.

def find_maximum():
    numbers=[23,6,8,90,56,100,56,1000,15678]

    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    print("max value is",max)

find_maximum()

# Explain the difference between local and global variables in a Python function.
"""
Local variables can be accessed only within the function or block where it is defined, whereas global variables are accessed throughout the 
entire program. Global variables use the global keyword to modify it inside a function, whereas local variables do not require any special keyword.
"""
# Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
x='global'

def local_global():
    x='local'
    print(x)

local_global()
print(x)
""" if the variable has the same name both locally and globally,python will prioratize the local variable over the global one when 
accessed inside the function."""


# Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length is provided, the function should assume
# the width is 5. Show how the function behaves when called with and without the width argument.

def calculate_area(length, width=5):
    area=length*width
    return (area)
print(calculate_area(34))
print(calculate_area(9,7))#here the width argument overwrite the defualt width
