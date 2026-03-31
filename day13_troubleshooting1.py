### Exercise 1


# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it!")

# my_function()

# Describe the Problem:
#1. What is the for loop doing?
# it's going over numbers between 1 and 19 (excluding 20)

#2. When is the function mean to "You got it"?
# When i is at 20 (when i is 20)

#3. What are your assumptions about the value of i?
# i is 1-19, but not 20


### Exercise 2

# Reproduce the bug (if we wanna recreate the bug, we can change the randint-s to be always out of range, i.e 6 and 12) or we could just set it to 6, not randint at all.

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])


### Exercise 3

# If the input is 1994, it will print nothing. The issue is that 'and year < 1994' doesnt include 1994.

# year = int(input("What's your year of birth? "))

# if year >= 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("Your are a Gen Z.")


### Exercise 4

# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("Invalid nr")
#     age = int(input("How old are you?"))

# if age > 18:
#     print(f"You can drive at age {age}")


### Exercise 5

### Exercise 6

### Exercise 7