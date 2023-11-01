# Challenges

#! Typing

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 
number1 = two_digit_number[0]
number2 = two_digit_number[1]
operation = int(number1) + int(number2)
print(operation)


#! BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / float( height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


#! Life weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_remainder = 90 - int(age)
days = age_remainder * 365
weeks = age_remainder * 52
months = age_remainder * 12
print(f"You have {days} days, {weeks}, and {months} months left.")
