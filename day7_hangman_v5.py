
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

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word = random.choice(word_list)
#print(chosen_word)

# Print the nr of _ needed to display to the player
placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

### TODO-5.1: Update the word list to use word_list from hangman_words.py - DONE
### TODO-5.2: Update the code to use the stages from the file hangman_art.py - not needed
### TODO-5.3: Import the logo from hangman_art.py and print it at the start of the game. - not needed
### TODO-5.4: If the user has entered a letter they've already guessed, print the letter and let them know. You should not deduct a life for this. - 
### TODO-5.5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. - DONE
### TODO-5.6: Update the code below to tell the user how many lives they have left. E.g ******** x LIVES LEFT ******* - DONE
### TODO-5.6: Update the print statement to give the user the correct word they were trying to guess. E.g IT WAS <CORRECT WORD>! You lose! - DONE


guessed_letters = []
game_over = False
lives = 6

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed '{guess}', try again.")
        continue

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
        
        print(f"The letter '{guess}' is not in the word, try again!")
        print(f" **** {lives} LIVES LEFT **** ")

        if lives == 0:
            game_over = True
            print(f"You lose! The correct word was '{chosen_word.upper()}'.")

    

    elif "_" not in display:
        game_over = True
        print("\nCongratulations, you win!")

    print(stages_reversed[lives])

    # elif lives == 0:
    #     game_over = True
    #     print("\nYou lose!")
    


