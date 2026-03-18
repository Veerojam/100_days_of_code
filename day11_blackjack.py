import random

ascii = '''
SOME ASCIII ARTTT
'''

print(ascii)

#want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

your_cards = []
your_cards.append(random.randint(1,11)) 
print(your_cards)

computer_cards = []
computer_cards.append(random.randint(1,11)) 
print(computer_cards)