
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. Guess the number.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
correct_nr = random.randint(1,100)

print(correct_nr)

if difficulty == "hard":
    nr_of_guesses = 5
else:
    nr_of_guesses = 10

def guessing(guess, nr_of_guesses):
    if guess > correct_nr:
        nr_of_guesses -= 1
        print("Too high. Guess again!")
        return nr_of_guesses

    elif guess < correct_nr:
        nr_of_guesses -= 1
        print("Too low. Guess again")
        return nr_of_guesses
        
user_not_correct = True

while user_not_correct:
        
        guess = int(input(f"You have {nr_of_guesses} attempts remaining to guess the number.\nMake a guess: "))
        nr_of_guesses = guessing(guess, nr_of_guesses)

        if guess == correct_nr:
             print(f"You got it! The answer was {correct_nr}!")
             user_not_correct = False

        if nr_of_guesses == 0:
             print("Sorry, you didn't get it right this time. Game over!")
             user_not_correct = False

