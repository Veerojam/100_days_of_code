from day15_resources import resources_in_machine, resources_per_coffee
import time

def report():
    for resource, details in resources_in_machine.items():
        print(f"{resource}: {details['amount']}{details['unit']}")


def ask_money():
    print("Please insert coins")
    quarters = int(input("How many quarters? ")) * 0.25 # Quarter 0.25
    dimes = int(input("How many dimes? ")) * 0.1 # Dime 0.10
    nickles = int(input("How many nickles? ")) * 0.05 # Nickel 0.05
    pennies = int(input("How many pennies? ")) * 0.01 # Penny 0.01
    resources_in_machine["money"]["amount"] += quarters + dimes + nickles + pennies


def money_back():
    #here is ... in change ---------------------------------------
    cash_back = round(resources_in_machine['money']['amount'], 2)
    resources_in_machine["money"]["amount"] = resources_in_machine["money"]["amount"] - resources_in_machine["money"]["amount"]

    if cash_back > 0:
        print(f"Here is {cash_back}$ back. Enjoy your coffee!")
    else:
        print(f"Enjoy your coffee!")
    


def check_resources():
    for resource, details in resources_in_machine.items():
        if details["amount"] >= resources_per_coffee[coffee_type][resource]:
            continue
        else:
            print(f"Sorry, not enough {resource} in the machine!")
            enough_resources = False
            return enough_resources
    enough_resources = True
    return enough_resources
    


def take_resources():
    if coffee_type == "report":
        report()
    if coffee_type == "off":
        exit() #this still prints cashback
    else:
        for resource in ["water", "milk", "coffee", "money"]:
            resources_in_machine[resource]["amount"] -= resources_per_coffee[coffee_type][resource]
        print(f"Please wait, brewing your {coffee_type}...")
        time.sleep(3)


while True:
    coffee_type = input("What would you like? Espresso, Latte, or Cappuccino: ").lower()
    ask_money()
    check_resources()
    if enough_resources == True:
        take_resources()
        money_back()
    else:
        money_back()

