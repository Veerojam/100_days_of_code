
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

# Print the nr of _ needed to display to the player

placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

### TODO-5.1: Update the word list to use word_list from hangman_words.py
### TODO-5.2: Update the code to use the stages from the file hangman_art.py
### TODO-5.3: Import the logo frm hangman_art.py and print it at the start of the game.
### TODO-5.4: If the user has entered a letter they've already guessed, print the letter and let them know. You should not deduct a life for this.
### TODO-5.5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
### TODO-5.6: Update the code below to tell the user how many lives they have left. E.g ******** x LIVES LEFT *******
### TODO-5.6: Update the print statement to give the user the correct word they were trying to guess. E.g IT WAS <CORRECT WORD>! You lose!


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

    print(f"\n{display}")

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("\nYou win!")

    print(stages_reversed[lives])

    # elif lives == 0:
    #     game_over = True
    #     print("\nYou lose!")
    


