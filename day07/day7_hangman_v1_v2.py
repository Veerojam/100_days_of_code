
import random

### TODO-1.1: Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

word_list = ["aardvark", "baboon", "camel"]

#v1
#chosen_word = word_list[random.randint(0,2)]

#v2:
chosen_word = random.choice(word_list)
print(chosen_word)

### TODO-1.2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
### TODO-3.1: Use a while loop to let the user guess again

length_of_chosen_word = len(chosen_word)
nr_of_guesses = 0



def guessing():
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    current_guess = display
    print(current_guess)


while nr_of_guesses <= length_of_chosen_word:
    guess = input("Guess a letter: ").lower()
    nr_of_guesses += 1
    guessing()

### TODO-1.3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

### TODO-2.1: Create an empty String called 'placeholder'. For each letter in the chosen_word, add a _ to placeholder.
# So if the chosen word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.

placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

### TODO-2.2: Create a "display" that puts the guessed letter in the right position
### TODO-3.2 Change the for loop so that you keep the previous correct letters in display


##### v1:
# position_of_guess = 0
# for letter in chosen_word:
#     if letter == guess:
#         placeholder[position_of_guess] = guess
#     position_of_guess += 1

# placeholder = ''.join(placeholder)
# print(placeholder)

#could also be done with a for loop: for char in password, password += char
# word_together = ""
# for char in placeholder:
#     word_together += char
# print(word_together)




