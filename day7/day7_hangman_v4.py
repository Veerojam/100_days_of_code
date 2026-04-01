
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

stages_reversed = stages[::-1] # Because the list was copied in the wrong order

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Print the nr of _ needed to display to the player
placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

### TODO-4.1: Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
### TODO-4.2: If guess is not a letter in the chosen_word, reduce lives by 1.
# If lives goes down to 0, then the game should end, and it should print "You lose!"
### TODO-4.3: Print the ASCII art from the list 'stages' that corresponds to the current number of lives the user has remaining.

guessed_letters = []
game_over = False
lives = 6

while not game_over:

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    
    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -=1

        print(stages_reversed[lives])

    if "_" not in display:
        game_over = True

        print("\nYou win!")

    elif lives == 0:
        game_over = True

        print("\nYou lose!")
    


