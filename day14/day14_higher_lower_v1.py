
import random

# logo = "higher/lower"
# print(logo)

instagram_followers = {
    "Cristiano Ronaldo, a footballer from Portugal 1": 672_000_000,
    "Lionel Messi, a footballer from Argentina 2": 504_000_000,
    "Selena Gomez, a singer and actress from the United States 3": 420_000_000,
    "Dwayne 'The Rock' Johnson, an actor and wrestler from the United States 4": 391_000_000,
    "Beyoncé, a singer and performer from the United States 5": 319_000_000,
    "Nike, a sportswear brand from the United States 6": 304_000_000,
    "Taylor Swift, a singer-songwriter from the United States 7": 284_000_000,
    "National Geographic, a nature and science magazine from the United States 8": 281_000_000,
    "Zendaya, an actress and fashion icon from the United States 9": 177_000_000,
    "NASA, a space agency from the United States 10": 100_000_000,
}

insta_list = []
for item in instagram_followers:
    insta_list.append(item)


def pick_from_list(one_or_two, previous_pick):
    any_pick1 = random.choice(insta_list)
    any_pick2 = random.choice(insta_list)

    if one_or_two == 2:
        while any_pick1 == any_pick2:
            any_pick1 = random.choice(insta_list)
        else:
            return any_pick1, any_pick2
    else:
        while any_pick1 == previous_pick:
            any_pick1 = random.choice(insta_list)
        else:
            return any_pick1


# if else statemente saab paremaks muuta, prolly ära kaotada osad

def a_or_b(user_answer, A, B):
    if user_answer == "A":
        if instagram_followers[A] > instagram_followers[B]:
            return True
        else:
            return False
    elif user_answer == "B":
        if instagram_followers[B] > instagram_followers[A]:
            return True
        else:
            return False


def the_game(A, B):
    score = 1

    while True:
        print(f"Compare A: {B}")
        A = pick_from_list(1, B)
        print(f"Against B: {A}")

        answer = input("\nWho has more followers? Type 'A' or 'B': ")

        right_or_wrong = a_or_b(answer, B, A)

        if right_or_wrong == True:
            score += 1
            print(f"You're right! Your current score is: {score}")
            B = A
        else:
            print(f"Sorry, you were wrong! Your final score is {score}")
            break


A, B = pick_from_list(2, None)
print(f"Compare A: {A}")
print(f"Against B: {B}")
answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()


first_pick = a_or_b(answer, A, B)


if first_pick == True:
    print(f"You're right! Your current score is: 1")
    the_game(A, B)
else:
    print("You lost with the first try, good one bruv!")


