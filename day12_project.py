# ----Number guessing problem ---
import random

easy_level_turns = 10
hard_level_turns = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print("Welcome to the Number Guessing Game! ")
    print("Iam thinking of a number between 1 to 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts reamaining to guess the number.")
        guess = int(input("Make a guess : "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("you loose..")
            return
        elif guess != answer:
            print("Guess again.")


game()