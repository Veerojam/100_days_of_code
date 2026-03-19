import random

continue_playing = True

while continue_playing:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == 'n':
        continue_playing = False

    else:

        ascii = '''
                                                                                           
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  

        '''

        print(ascii)
        
        cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        player_hand = []
        computer_hand = []


        def draw(list_name):
            list_name.append(random.choice(cards_list))

        # First draw - player draws twice, computer draws once?
        draw(player_hand)
        draw(player_hand)
        draw(computer_hand)
        #draw(computer_hand

        print(f"Your current hand: {player_hand}, your current score: {sum(player_hand)}")
        print(f"Computer's first card: {computer_hand}")

        to_continue = True

        while to_continue:

            another_card = input("Type 'y' to get another card, type 'n' to pass: \n")

            if another_card == 'n':
                while sum(computer_hand) <= 17:

                    draw(computer_hand)

                if sum(computer_hand) > 21:

                    print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                    print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                    print("Computer loses")
                
                elif sum(computer_hand) > sum(player_hand):
                        print(f"\nYour final hand: {player_hand}, your final score: {sum(player_hand)}")
                        print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                        print("You lose!")

                elif sum(player_hand) == sum(computer_hand):
                    
                    print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                    print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                    print("It's a draw!")
                
                else:
                    
                    print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                    print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                    print("You win!")

                to_continue = False

            else: # continue = yes
                draw(player_hand)

                if sum(player_hand) > 21:
                    if 11 in player_hand:
                        location = player_hand.index(11)
                        player_hand[location] = 1

                        print(f"Your current hand: {player_hand}, your current score: {sum(player_hand)}")
                        print(f"Computer's current hand: {computer_hand}")

                    else:
                        print(f"\nYour final hand: {player_hand}, your final score: {sum(player_hand)}")
                        print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                        print("You lose!")

                        to_continue = False

                elif sum(computer_hand) > 21:

                    print(f"\nYour final hand: {player_hand}, your final score: {sum(player_hand)}")
                    print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                    print("You win!")

                    to_continue = False
                
                else:
                    print(f"Your current hand: {player_hand}, your current score: {sum(player_hand)}")
                    print(f"Computer's current hand: {computer_hand}")

