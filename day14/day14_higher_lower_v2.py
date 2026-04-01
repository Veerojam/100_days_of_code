
import random
from art import logo, vs
from game_data import instagram_followers, data_list

print(logo)


insta_list = list(instagram_followers)

def pick_random(one_or_two, previous_pick):
    random_pick1 = random.choice(insta_list)
    
    if one_or_two == 2:
        random_pick2 = random.choice(insta_list)
        while random_pick1 == random_pick2:
            random_pick1 = random.choice(insta_list)
        return random_pick1, random_pick2
    else:
        while random_pick1 == previous_pick:
            random_pick1 = random.choice(insta_list)
        return random_pick1


def a_or_b(A, B):
            if instagram_followers[A] > instagram_followers[B]:
                return "A"
            else:
                return "B"


def the_game(A, B):
    score = 1

    while True:
        print(f"Compare A: {B}")
        A = pick_random(1, B)
        print(f"Against B: {A}")

        answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()

        correct = a_or_b(B, A)

        if correct == answer:
            score += 1
            print(f"You're right! Your current score is: {score}")
            B = A
        else:
            print(f"Sorry, you were wrong! Your final score is {score}")
            break


A, B = pick_random(2, None)

print(f"Compare A: {A}")
print(f"Against B: {B}")
answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()
correct = a_or_b(A, B)

if answer == correct:
    print(f"You're right! Your current score is: 1")
    the_game(A, B)
else:
    print("You lost with the first try, good one bruv!")
