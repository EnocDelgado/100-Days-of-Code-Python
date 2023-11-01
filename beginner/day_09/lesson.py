# day 9

#! Dictionaries

'''
key         Value

Bug         An Error in a program that preents the program from ruunging as expected.
Function    A piece of code that you can easily call over and over again.
Loop        The action of duing something over and over again.

'''

programming_dictionary = { 
    "Bug": "An Error in a program that preents the program from ruunging as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of duing something over and over again."
}

# Retieving items from dictionary
print(programming_dictionary["Loop"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of duing something over and over again"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionay
programming_dictionary["Loop"] = "The action of duing something over and over again!"
print(programming_dictionary)

# Loop in throuth a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#! Nested Dictionaries

'''
{
    key1: [List],
    key2: {Dict},
}
'''

# Nested
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested a list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Lyon"],
    "Germany": ["Berlin", "Munchen", "Leipzig"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Lyon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munchen", "Leipzig"], "total_visits": 5}
}

'''
[{
    key1: [List],
    key2: {Dict},
},
{
    key1: Value,
    key2: Value
}]
'''

# Nested Dictionary in a list

travel_log = {
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Lyon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Munchen", "Leipzig"], 
        "total_visits": 5
    }
}


#! 