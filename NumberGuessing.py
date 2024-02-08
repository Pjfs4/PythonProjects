import random

DIFFICULTY_HARD = 5
DIFFICULTY_EASY = 10


def guess_number(guessed_number, random_number, attempts):
    if guessed_number == random_number:
        print(f"You got it! The answer was {guessed_number}.")
    elif guessed_number > random_number:
        print("Too high.")
        return attempts - 1
    else:
        print("Too low.")
        return attempts - 1


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return DIFFICULTY_EASY
    else:
        return DIFFICULTY_HARD


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = random.randint(1, 100)
    # Just to test it
    print(f"Pssst, the number is {computer_number}")
    lives = set_difficulty()
    guess = 0
    while guess != computer_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = guess_number(guess, computer_number, lives)
        if lives == 0:
            print("You are out of guesses, you lose.")
            return
        elif guess != computer_number:
            print("Guess again.")


want_to_play = False
while not want_to_play:
    game()
    continue_playing = input("Would you like to play again? Type 'y' or 'n': ")
    if continue_playing != 'y':
        want_to_play = True
