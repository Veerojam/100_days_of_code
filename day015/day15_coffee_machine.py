
from day15_resources import resources_in_machine, resources_per_coffee

# or if user enters 'report' it will print report
# 1. Print report 
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
    # 4.1 Refund
# 5. Make coffee


coffee_type = input("What would you like? Espresso, Latte, or Cappuccino: ").lower()

def report():
    for resource, details in resources_in_machine.items():
        print(f"{resource}: {details['amount']}{details['unit']}")

def calc_money():
    print("Please insert coins!")
    quarters = int(input("How many quarters? ")) * 0.25 # Quarter 0.25
    dimes = int(input("How many dimes? ")) * 0.1 # Dime 0.10
    nickles = int(input("How many nickles? ")) * 0.05 # Nickel 0.05
    pennies = int(input("How many pennies? ")) * 0.01 # Penny 0.01

    cash = quarters + dimes + nickles + pennies

    #raha tagasi ja ülejäänu lisa resources alla
    #cash_back = cash - price_coffee
    resources_in_machine["money"]["amount"] += cash

    #print(resources_in_machine["money"]["amount"])



def take_resources():
    
    price_espresso = resources_per_coffee["espresso"]["price"]
    
    price_cappuccino = resources_per_coffee["cappuccino"]["price"]

    price_latte = resources_per_coffee["latte"]["price"]

    # need tõsta välja funktsioonist
        
    # print(price_latte, price_espresso, price_cappuccino)
    

    if coffee_type == "espresso":
        calc_money()
        if resources_in_machine["money"]["amount"] >= price_espresso: 
            resources_in_machine["money"]["amount"] = resources_in_machine["money"]["amount"] - price_espresso
        else:
            print("Not enough money.")
    elif coffee_type == "cappuccino":
        calc_money()
        if resources_in_machine["money"]["amount"] >= price_cappuccino: 
            resources_in_machine["money"]["amount"] = resources_in_machine["money"]["amount"] - price_cappuccino
        else:
            print("Not enough money.")
    elif coffee_type == "latte":
        calc_money()
        if resources_in_machine["money"]["amount"] >= price_latte: 
            resources_in_machine["money"]["amount"] = resources_in_machine["money"]["amount"]- price_latte
        else:
            print("Not enough money.")
    # siin kordan kalkulatsiooni, saab ehk lihtsustada
    elif coffee_type == "report":
        report()

def money_back():
    #here is ... in change
    cash_back = round(resources_in_machine['money']['amount'], 2)
    print(f"Here is {cash_back}$ back! Enjoy your coffee.")
    resources_in_machine["money"]["amount"] = resources_in_machine["money"]["amount"] - resources_in_machine["money"]["amount"]

#calc_money()
take_resources()
print(resources_in_machine["money"]["amount"])
money_back()
# def check_resources()
#     asd

# report()
#calc_money()

#print(resources["money"]["amount"])