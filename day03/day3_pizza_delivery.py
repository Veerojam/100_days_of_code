#Pizza delivery

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L? ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
number_of_pizzas = int(input("How many pizzas do you want? "))

price_sum = 0
price_small = 15
price_medium = 20
price_large = 25
pepperoni_small = 2
pepperoni_medium = 3
price_cheese = 1


if size == "S":
    price_sum = price_small
    if pepperoni == "Y":
        price_sum += pepperoni_small
    if extra_cheese == "Y":
        price_sum += price_cheese
    print(f"Your final bill is ${price_sum}")
elif size == "M":
    price_sum = price_medium
    if pepperoni == "Y":
        price_sum += pepperoni_medium
    if extra_cheese == "Y":
        price_sum += price_cheese
    print(f"Your final bill is ${price_sum}")
elif size == "L":
    price_sum = price_large
    if pepperoni == "Y":
        price_sum += pepperoni_medium
    if extra_cheese == "Y":
        price_sum += price_cheese
    print(f"Your final bill is ${price_sum}")




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
