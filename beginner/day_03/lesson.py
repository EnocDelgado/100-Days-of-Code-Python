# DAY 


#! Contol flow

print("Welcome to the rollercaster!")
height = int("What is your height in cm?\n")

if height > 120:
	print("You can ride the rollercaster!")
else:
	print("Sorry, you have to grow taller before you can ride.")
	

'''
| Operator | Meaning |
| --- | --- |
| > | Greater than |
| < | Less than |
| ≥ | Greater than or equal to |
| ≤ | Less than or equal to |
| == | Equal to |
| ≠ | Not equal to |
'''

#! Nested if and elif

print("Welcome to the rollercaster!")
height = int("What is your height in cm?\n")

if height > 120:
	print("You can ride the rollercaster!")
	age = int(input("What is your age? \n"))
	if age < 12:
		print("Please pay $5.")
	elif age <= 18:
		print("Please pay $7.")
	else: 
		print("Please pay $12.")
else:
	print("Sorry, you have to grow taller before you can ride.")
	
#! multiples if statements

print("Welcome to the rollercaster!")
height = int("What is your height in cm?\n")
bill = 0

if height > 120:
	print("You can ride the rollercaster!")
	age = int(input("What is your age? \n"))
	if age < 12:
		bill = 5
		print("Please pay $5.")
	elif age <= 18:
		bill =7
		print("Please pay $7.")
	else:
		bill = 12
		print("Please pay $12.")

	wants_photo = input("Do oyu want a photo taken? Y or N.")
	if wants_photo == "Y":
		bill += 3

	print(f"Your final bill is {bill}")

else:
	print("Sorry, you have to grow taller before you can ride.")
	

#! Logical Operators

height = int("What is your height in cm?\n")
bill = 0

if height > 120:
	print("You can ride the rollercaster!")
	age = int(input("What is your age? \n"))
	if age < 12:
		bill = 5
		print("Please pay $5.")
	elif age <= 18:
		bill =7
		print("Please pay $7.")
	elif age >= 45 and age <= 55:
		print("Everithing is going to be ok. Have a free ride on us!")
	else:
		bill = 12
		print("Please pay $12.")

	wants_photo = input("Do oyu want a photo taken? Y or N.")
	if wants_photo == "Y":
		bill += 3

	print(f"Your final bill is {bill}")

else:
	print("Sorry, you have to grow taller before you can ride.")
	

