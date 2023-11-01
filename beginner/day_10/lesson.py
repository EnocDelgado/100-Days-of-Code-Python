# DAY 10

#! Functions with Outputs

'''
Function

def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this

my_function(something)
'''

'''
Function with Outputs

def my_function():
    #return 3 + 2

output = my_function()
'''

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("Enoc", "Byan")
print(formated_string)


#! Multiples Return Values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any value"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

formatted_name = format_name("Enoc", "Byan")
print(formatted_name)


#! Docstring

#Already used functions with outputs
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide any value"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"