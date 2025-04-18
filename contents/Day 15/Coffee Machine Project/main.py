from database import MENU, resources

def operations(coffee_type):
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        try:
            resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        except:
            coffee_type == 'espresso'

def cost(coffee_type, value):
    
    if total > MENU[coffee_type]["cost"]:
        change = total - MENU[coffee_type]["cost"]
        print(f"This is your change: {change:.2f}")
        value += MENU[coffee_type]["cost"]
        
    elif total == MENU[coffee_type]["cost"]:
        value += MENU[coffee_type]["cost"]
        
    else:
        print("Sorry that's not enough money. Money refunded.")

coffee_machine_on = True
money = 0
while coffee_machine_on:
    choice = input("Available:\n Espresso - 1.5$\n Latte- 2.5$\n Cappuccino - 3.0$\nWhat would you like? ").lower()
    
    if choice in ['espresso', 'latte', 'cappuccino']:
        print("Please insert coins.")

        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        
        total = 0
        total += quarters + dimes + nickels + pennies
        
        print("\n"*2)
        operations(choice)
        cost(choice, money)
        

    
    elif choice == 'report':
        print("\n"*2)
        print(f"Coffee: {resources["coffee"]}gr")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Water: {resources["water"]}ml")
        print(f"Money: ${money}")
        
    elif choice == "off":
        coffee_machine_on = False
    
    else:
        print("Invalid input. Please choose one of the options below: ")
    
        
    