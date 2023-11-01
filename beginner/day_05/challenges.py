#

#! Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
# print(total_height)

overall_student = 0
for student in student_heights:
  overall_student += 1
# print(overall_student)

average_height = round(total_height / overall_student)
print(average_height)

# overall_height = sum(student_heights)
# overall_student = len(student_heights)
# average_height = round(overall_height / overall_student)
# print(average_height)


#! Hight Score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_score = 0
for score in student_scores:
  if score > height_score:
    height_score = score
print(f"The highest score in the class is: {height_score}")

#! Adding Even Number

#Write your code below this row 👇
numbers = 0
for number in range(0, 101, 2):
    if number > 0:
        numbers += number
print(numbers)


#! FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)