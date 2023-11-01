#

#! Head or Tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_site = random.randint(0,1)
if random_site == 1:
    print("Heads")
else:
    print("Tails")


#! Bank Roulette

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_buy = names[random_choice]
print(f"{person_who_buy} is going to buy the meal today!")


#! Treasure map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal  = int(position[0])
vertical    = int(position[1])

map[vertical - 1][horizontal - 1 ] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")