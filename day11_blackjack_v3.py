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
            # new_cards_sum = sum(new_cards)
            # return new_cards_sum
        
        def status(state, winner = None):
            
            if state == "first":
                print(f"Your first hand: {player_hand}, your current score: {sum(player_hand)}")
                print(f"Computer's first cards: {computer_hand}, computer's currect score {sum(computer_hand)}")
            
            elif state == "ongoing":
                print(f"Your current hand: {player_hand}, your current score: {sum(player_hand)}")
                print(f"Computer's current hand: {computer_hand}, , computer's currect score {sum(computer_hand)}")

            elif state == "finished" and winner == "computer":

                print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                print("You lose!")
            
            elif state == "finished" and winner == "player":
                print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                print("You win!")
            
            else:
                print(f"Your final hand: {player_hand}, your final score: {sum(player_hand)}")
                print(f"Computer's final hand {computer_hand}, computer's final score: {sum(computer_hand)}")
                print("It's a draw!")
                

        for _ in range(2):
            draw(player_hand)
            draw(computer_hand)
   

        status("first")

        to_continue = True

        while to_continue:
            
            if len(player_hand) == 2 and sum(player_hand) == 21:
                print("\nYour score: BLACKJACK!")

            another_card = input("Type 'y' to get another card, type 'n' to pass: \n")

            if another_card == 'n':
                while sum(computer_hand) <= 17:

                    draw(computer_hand)

                if sum(computer_hand) > 21:

                    status("finished", "player")
                
                elif sum(computer_hand) > sum(player_hand):
                        
                        status("finished", "computer")

                elif sum(player_hand) == sum(computer_hand):
                    
                    status("draw")
                
                else:

                    status("finished", "player")
                    
                to_continue = False

            else: # continue = yes
                draw(player_hand)

                if sum(player_hand) > 21:
                    if 11 in player_hand: #if 11 in hand and over 21, change it to 1.
                        location = player_hand.index(11)
                        player_hand[location] = 1

                        status("ongoing")

                    else:
                        
                        status("finished", "computer")

                        to_continue = False

                elif sum(computer_hand) > 21:

                    status("finished", "player")

                    to_continue = False
                
                else:
                    
                    status("ongoing")


