#Pizza delivery

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L? ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
#number_of_pizzas = int(input("How many pizzas do you want? "))

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your bill is {bill}$")



#small = 15
#small + pepperoni = 15 + 2 = 17
#small + cheese = 15 + 1 = 16
#small + pepperoni + cheese = 15 + 2 + 1 = 18

#medium = 20
#medium + pepperoni = 20 + 3 = 23
#medium + cheese = 20 + 1 = 21
#medium + pepperoni + cheese = 20 + 3 + 1 = 24

#large = 25
#large + pepperoni = 25 + 3 = 28
#large + cheese = 25 + 1 = 26
#large + pepperoni + cheese = 25 + 3 + 1 = 29
