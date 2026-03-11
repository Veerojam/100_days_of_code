# Easy version: Generate the password in sequence. Letters, then symbols, then numbers.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")

nr_of_letters = int(input("How many letters would you like in your password?\n"))
nr_of_symbols = int(input("How many symbols would you like?\n"))
nr_of_numbers = int(input("How many numbers would you like?\n"))

password = "" #2nd, enhanced ver
for _ in range(nr_of_letters):
    password += random.choice(letters) #2nd, enhanced ver
    #1st ver: random_letter = random.choice(letters)
    #1st ver: print(random_letter, end="")

for _ in range(nr_of_symbols):
    password += random.choice(symbols) #2nd, enhanced ver
    #1st ver: random_symbol = random.choice(symbols)
    #1st ver: print(random_symbol, end="")

for _ in range(nr_of_numbers):
    password += random.choice(numbers) #2nd, enhanced ver
    #1st ver: random_number = random.choice(numbers)
    #1st ver: print(random_number, end="")

print(password)
