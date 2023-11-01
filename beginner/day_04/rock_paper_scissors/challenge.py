import random
rock = '''
	_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
	_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [ rock, paper, scissors]

person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))


if person_choice >= 3 or person_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[person_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

    if person_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and person_choice == 2:
        print("You lose")
    elif computer_choice > person_choice:
        print("You lose")
    elif computer_choice == person_choice:
        print("It's a draw")