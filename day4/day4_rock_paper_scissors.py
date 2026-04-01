import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# STEP 1: Get input as a string first (no int() yet)
player_chooses = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

# STEP 2: Validate while it's still a string
if player_chooses not in ["0", "1", "2"]:
    print("Invalid input. Please select a number between 0-2.")

else:
    # STEP 3: NOW it's safe to convert to int
    player_chooses = int(player_chooses)
    
    computer_chooses = random.choice(choices)

    print(f"You chose {choices[player_chooses]}")
    print(f"Computer chose {computer_chooses}")

    if player_chooses == 0:
        if computer_chooses == rock:
            print("It's a draw!")
        elif computer_chooses == paper:
            print("You lose!")
        elif computer_chooses == scissors:
            print("You win!")
    elif player_chooses == 1:
        if computer_chooses == rock:
            print("You win!")
        elif computer_chooses == paper:
            print("It's a draw!")
        elif computer_chooses == scissors:
            print("You lose!")
    elif player_chooses == 2:
        if computer_chooses == rock:
            print("You lose!")
        elif computer_chooses == paper:
            print("You win!")
        elif computer_chooses == scissors:
            print("It's a draw!")
