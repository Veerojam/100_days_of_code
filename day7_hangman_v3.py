
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


nr_of_guesses = 0

# Print the nr of _ needed to display to the player
placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)

### TODO-3.1: Use a while loop to let the user guess again
### TODO-3.2: Change the for loop so that you keep the previous correct letters in display

guesses_so_far = []
game_over = False

while not game_over:

    guess = input("Guess a letter: ").lower()
    guesses_so_far.append(guess)
    display = ""

    for letter in chosen_word:
        if letter in guesses_so_far:
            display += letter
        else:
            display += "_"
    nr_of_guesses += 1
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
    

##### Angela's solution:

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win!")















