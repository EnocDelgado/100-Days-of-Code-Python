# DAY 4

#! Random Module

import random

random_int = random.randint(1, 10)
print(random_int)

# 0.00000 * ).9999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)


#! Methods

states_of_usa = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 
                 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 
                 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 
                 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 
                 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 
                 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 
                 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 
                 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 
                 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 
                 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

states_of_usa[1] = "Pennsylvania"

# Array methods
states_of_usa.append("Angeland")
states_of_usa.insert(-1, "c")
states_of_usa.remove("c")
states_of_usa.pop("")


#! Indexing lists

states_1 = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 
            'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 
            'New Hampshire', 'Virginia', 'New York', 'North Carolina', 
            'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 
            'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama']

states_2 = ['Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 
            'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 
            'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 
            'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 
            'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

states = [states_1, states_2]
print(states)