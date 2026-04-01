import random

ascii = '''
SOME ASCIII ARTTT
'''

print(ascii)

#want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

player_cards = []

def player_draw():
    player_cards.append(random.randint(1,11))

def playa_sum():
    player_sum = 0
    for card in player_cards:
        player_sum += card
    return player_sum



computer_cards = []

def computer_draw():
    computer_cards.append(random.randint(1,11))


def comp_sum():
    computer_sum = 0
    for card in computer_cards:
        computer_sum += card
    return computer_sum


player_draw()
computer_draw()

computer_sum = comp_sum()
player_sum = playa_sum()

print(player_cards)
print(computer_cards)

to_continue = True

while to_continue:

    another_card = input("Type 'y' to get another card, type 'n' to pass: \n")

    if another_card == 'n':
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand {computer_cards}")

        if player_sum > computer_sum:
            print("You win!")
        elif player_sum == computer_sum:
            print("It's a draw!")
        else:
            print("Computer wins!")
        to_continue = False

    else:
        player_draw()
        player_sum = playa_sum()

        if player_sum > 21:
            print("You lose!")
            to_continue = False

        computer_draw()
        computer_sum = comp_sum()

        print(player_cards)
        print(player_sum)
        print(computer_cards)
        print(computer_sum)

        if computer_sum > 21:
            print("You win!")

