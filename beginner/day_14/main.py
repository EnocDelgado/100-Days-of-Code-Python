from data import data
import random

def get_random_account():
    """Get data from randrom account"""
    return random.choice(data)

def format_data(account):
    # Format the account data into printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    # Display art
    # import logo
    score = 0
    game_shuld_continue = True
    account_b = get_random_account()
    account_b = get_random_account()

    # Make the game repeatable.
    while game_shuld_continue:
        # Generate a random account from the game data.

        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Comapre A: {format_data(account_a)}")
        print(" ")
        print(f"Comapre B: {format_data(account_b)}")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Chaeck if user is correct.
        ## Get follower count of each account.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        ## Use if statemnt to check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen between rounds.
        # clear()

        # Give user feedback on their guess.
        # Score keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            game_shuld_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()