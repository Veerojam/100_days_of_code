


### TODO-5.1: Update the word list to use word_list from hangman_words.py - DONE
### TODO-5.2: Update the code to use the stages from the file hangman_art.py - not needed
### TODO-5.3: Import the logo from hangman_art.py and print it at the start of the game. - not needed
### TODO-5.4: If the user has entered a letter they've already guessed, print the letter and let them know. You should not deduct a life for this. - DONE
### TODO-5.5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. - DONE
### TODO-5.6: Update the code below to tell the user how many lives they have left. E.g ******** x LIVES LEFT ******* - DONE
### TODO-5.6: Update the print statement to give the user the correct word they were trying to guess. E.g IT WAS <CORRECT WORD>! You lose! - DONE



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



# #word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
#          'coyote crow deer dog donkey duck eagle ferret fox frog goat '
#          'goose hawk lion lizard llama mole monkey moose mouse mule newt '
#          'otter owl panda parrot pigeon python rabbit ram rat raven '
#          'rhino salmon seal shark sheep skunk sloth snake spider '
#          'stork swan tiger toad trout turkey turtle weasel whale wolf '
#          'wombat zebra ').split()

word_list = ('sipelgas paavian mäger nahkhiir karu kobras kaamel kass karp kobra puuma '
            'koiott vares hirv koer eesel part kotkas tuhkur rebane konn kits '
            'hani kull lõvi sisalik laama mutt ahv põder hiir muul madu '
            'saarmas öökull panda papagoi tuvi püüton küülik jäär rott ronk '
            'ninasarvik lõhe hüljes hai lammas skunk laiskloom madu ämblik '
            'toonekurg luik tiiger kärnkonn forell kalkun kilpkonn nirk vaal hunt '
            'vombat sebra').split()

chosen_word = random.choice(word_list)

# Print the nr of _ needed to display to the player
placeholder = len(chosen_word) * ' _ '
print(placeholder)


guessed_letters = []
game_over = False
lives = 6

while not game_over:

    #guess = input("Guess a letter: ").lower()
    guess = input("Proovi tähte: ").lower()

    if guess in guessed_letters:
        print(f"Sa juba proovisid {guess}, palun proovi uuesti!")
        # print(f"You've already guessed '{guess}', try again.")
        continue #continue with the loop from top, otherwise it will deduct a life for the same guess.

    guessed_letters.append(guess)
    
    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    #print(f"\nWord to guess: {display}")
    print(f"\nSõna, mida arvata: {display}")

    if guess not in chosen_word:
        lives -=1
        
        print(f"Täht {guess} ei ole selles sõnas, proovi uuesti!")
        print(f" **** {lives} ELU JÄRGI **** ")
        print(f"Sõna, mida arvata: {display}")
        # print(f"The letter '{guess}' is not in the word, try again!")
        # print(f" **** {lives} LIVES LEFT **** ")

        if lives == 0:
            game_over = True
            #print(f"You lose! The correct word was '{chosen_word.upper()}'.")
            print(f"Sina kaotasid! Õige sõna oli '{chosen_word.upper()}'.")

    print(stages[6 - lives]) 

    if "_" not in display:
        game_over = True
        #print("\nCongratulations, you win!")
        print("\nPalju õnne, SA OLED MAAILMA SUURIM VÕITJAAAAAAA")

    

  
    


