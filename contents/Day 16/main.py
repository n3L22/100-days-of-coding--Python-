from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine_on  = True
#object   #class
menu = Menu()  # Create Menu instance once
coffee_maker = CoffeeMaker()# Create CoffeeMaker instance
money = MoneyMachine()

while coffee_machine_on:
    print('What would you like to drink?')
    choice = input(f"{menu.get_items()}\n ")
    
    if choice in menu.get_items():
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print(f"Sorry, not enough resources to make this drink.")
        
    elif choice == 'report':
        coffee_maker.report()
        money.report()
        
    elif choice == 'off':
        coffee_machine_on = False
        
    else:
        print("Sorry, that's not a valid choice.")
        
    