import random
from art import logo


def choose_difficulty():
    """returns number of attemps according to level of difficulty"""

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5


def get_attempts_left(attempts):
    """returns number of attempts left and after reduce it by 1"""

    print(f"You have {attempts} attempts remaining to guess The number.")
    attempts -= 1
    return attempts


def ask_guess():
    return int(input("Make a guess: "))


def evaluate_guess(guess_number, target_number):
    if guess_number > target_number:
        print("Too high.")
        return False
    elif guess_number < target_number:
        print("Too low.")
        return False
    else:
        return True


def play_game():
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(0, 101)

    attempts = choose_difficulty()
    end_of_game = False

    while attempts > 0:
        attempts = get_attempts_left(attempts)
        guess = ask_guess()
        end_of_game = evaluate_guess(guess, random_number)

        if end_of_game:
            attempts = 0
            print("You win 😎")
        elif attempts == 0:
            print("You lose 😰")


is_game_over = False
while not is_game_over:
    print(logo)
    play_game()
    if input("Do you want to play again, type 'y' or 'n'?: ") == "n":
        is_game_over = True
