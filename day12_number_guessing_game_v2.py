
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, turns, answer):
    if guess > answer:
        print("Too high!")
        return turns -1

    elif guess < answer:
        print("Too low!")
        return turns -1
    
    else:
        print(f"You got it! The answer was {answer}!")


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. Guess the number.")
    answer = randint(1,100)
    print(answer)

    turns = difficulty()
   
    guess = 0
    while guess != answer:
        guess = int(input(f"You have {turns} attempts remaining to guess the number.\nMake a guess: "))
        turns = check_answer(guess, turns, answer)
        if turns == 0:
            print("Sorry, you didn't get it right this time. Game over!")
            return
        elif guess != answer:
            print("Guess again!")


game()
