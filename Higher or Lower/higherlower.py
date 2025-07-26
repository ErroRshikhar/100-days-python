from art import logo, logo2
from game_data import data
import random

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(logo2)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? 'A' or 'B': ").lower()

        print("\n" * 20)
        print(logo)
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong.! Final score: {score}")
            game_continue = False

game()
