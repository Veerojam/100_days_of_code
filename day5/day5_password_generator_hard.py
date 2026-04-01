# Hard version: The final password does not follow a pattern. Each time you generate a password, the positions of letters, symbols and numbers are different.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("----> Welcome to the PyPassword Generator! <----\n")

nr_of_letters = input("How many letters would you like in your password?\n")
nr_of_symbols = input("How many symbols would you like?\n")
nr_of_numbers = input("How many numbers would you like?\n")

password = []

for _ in range(int(nr_of_letters)):
    password += random.choice(letters)
    
for _ in range(int(nr_of_symbols)):
    password += random.choice(symbols)

for _ in range(int(nr_of_numbers)):
    password += random.choice(numbers)
random.shuffle(password)

#turn the list into a string, which could also be done with a for loop: for char in password, password += char
password = ''.join(password)
print(f"Your password is: {password}")



# 1st version:

# pw_length = len(password)
# randomized_pw = ""

# for _ in range(pw_length):
#     randomized_pw += random.choice(password)

# print(randomized_pw)