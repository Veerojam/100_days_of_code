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

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page

# print(f"words_per_page = {word_per_page}")
# print(f"total words = {total_words}")

### Exercise 6

# import random

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = new_item + item
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])


### Exercise 7

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."


### Exercise 8:

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    

### Exercise 9
# Target is the number up to which we count

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)

# fizz_buzz(15)