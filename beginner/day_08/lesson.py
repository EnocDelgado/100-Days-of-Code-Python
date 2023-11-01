# DAY 8

#! Functions with Inputs

# Functions

'''
def my_function():
    Do this
    Then do this
    Finally do this
'''

# Review:
# Create a function called greet()
# Write 3 print statements inside the funtion.
# Call the greet() funtion and run your code.

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the wheater nice today?")

greet()


# Functions with Inputs

'''
def my_function(something):
    Do this with something
    Then do this
    Finally do this
'''

# Review:
# Create a function with a argument called greet()
# Write 3 print statements inside the funtion.
# Call the greet() funtion, gives a parameter and run your code.
def greet_with_arg(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the wheater nice today?")

greet_with_arg("Angela")


#! Positional vs Keyword Arguments

# Positional Arguments

'''
def my_function(a, b, c):
    Do this with a
    Then do this with b
    Finally do this with c
'''

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Nowhere")


# Keyword Arguments
'''
def my_function(a = 1, b = 2, c = 3):
    Do this with a
    Then do this with b
    Finally do this with c
'''

def greet_with_keyword(name="Angela", location="London"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_keyword("Jack Bauer", "Nowhere")