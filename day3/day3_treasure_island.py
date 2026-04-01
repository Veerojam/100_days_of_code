#https://ascii.co.uk/art/treasure
ascii = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
print(ascii)
print("Welcome to Treasure Island!\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?")

left_or_right = input('     Type "left" or "right"\n').lower

if left_or_right == "left":
    swim_or_wait = input("You're now at a river. Do you want to swim or wait?\n ").lower
    if swim_or_wait == "wait":
        door = input("There are now 3 doors in front of you red, yellow and blue. Which one do you open?\n").lower
        if door == "red":
            print("You opened the door into a raging inferno. You are painfully burning. Game Over!")
        elif door == "yellow":
            print("You found the treasure. You win!!!!")
        elif door == "blue":
            print("You were eaten by blue beasts. Game Over!")
        else:
            print("Game over!")
    else:
        print("You were attacked by a trout. Game Over!")
else:
    print("Tee-hee, wrong choice, you fell into a hole. It's game over for you!")