import random

ascii = '''
SOME ASCIII ARTTT
'''

print(ascii)

#want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

player_cards = []
computer_cards = []


def draw(list_name):
    list_name.append(random.randint(1,11))


draw(player_cards)
draw(computer_cards)


print(f"Your current hand: {player_cards}")
print(f"Computer's current hand: {computer_cards}")

to_continue = True

while to_continue:

    another_card = input("Type 'y' to get another card, type 'n' to pass: \n")

    if another_card == 'n':
        print(f"Your final hand: {player_cards}")
        print(f"Computer's final hand {computer_cards}")

        if sum(player_cards) > sum(computer_cards):
            print("You win!")
        elif sum(player_cards) == sum(computer_cards):
            print("It's a draw!")
        else:
            print("Computer wins!")
        to_continue = False

    else:
        draw(player_cards)
        draw(computer_cards)

        print(f"Your current hand: {player_cards}")
        print(f"Computer's current hand: {computer_cards}")

        if sum(player_cards) > 21:
            print(f"\nYour final hand: {player_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("You lose!")
            to_continue = False

        if sum(computer_cards) > 21:
            print(f"\nYour final hand: {player_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("You win!")
            to_continue = False

