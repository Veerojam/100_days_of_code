
# Print report
# Check resources sufficient
# Process coins
# Check transaction successful?
# Make coffee


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink today? {options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report() 
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(choice)
        print(f"{choice.capitalize()} is {chosen_drink.cost}$")
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
        

    ##### Minu variant:
    # else:
    #     chosen_drink = menu.find_drink(choice)
    #     cost = chosen_drink.cost
                
    #     if not coffee_maker.is_resource_sufficient(chosen_drink):
    #         continue

    #     print(f"{choice.capitalize()} is {cost}$")
        
    #     if money_machine.make_payment(cost):
    #         coffee_maker.make_coffee(chosen_drink)



        
