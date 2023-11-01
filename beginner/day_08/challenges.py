# Challenges

#! Paint Area Calculator 

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cars of paint")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#! Prime Number Checker

#Write your code below this line 👇
def prime_checker(number):
    # validation
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)