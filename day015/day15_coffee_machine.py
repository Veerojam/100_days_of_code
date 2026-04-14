
from day15_resources import resources

# Coin operated
# Coins = Penny 0.01, Nickel 0.05, Dime 0.10, Quarter 0.25
# what would you like? Espresso, Latte, Cappuccino
# or if user enters 'report' it will print report
# report has water 300 ml, milk 200 ml, coffee 100g, money 0$
# 1. Print report 
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
    # 4.1 Refund
# 5. Make coffee


#coffee_type = input("What would you like? Espresso, Latte, or Cappuccino: ").lower()

def report():
    print(resources).items()

def take_resources():
    if coffee_type == "espresso":
        water -= 1
        milk -= 1
        coffee -= 1
        money -= 1

    elif coffee_type == "latte":
        water -= 1
        milk -= 1
        coffee -= 1
        money -= 1

    elif coffee_type == "cappuccino":
        water -= 1
        milk -= 1
        coffee -= 1
        money -= 1
    
    elif coffee_type == "off":
        print("Your watch has ended")

    else:
        report

# def check_resources()
#     asd

#report()

print(resources.items())




