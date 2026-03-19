
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")


if difficulty == "hard":
    nr_of_guesses = 5
    print("You have 5 attempts remaining to guess the number.\nMake a guess: ")
else:
    nr_of_guesses = 10
    print("You have 10 attempts remaining to guess the number.\nMake a guess: ")