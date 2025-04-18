from database import MENU, resources

def operations(coffee_type):
    # First check if we have enough resources
    for i in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][i] > resources[i]:
            print(f"There is not enough {i}. Try another one or Come back later!")
            return False  # Exit the loop if any ingredient is insufficient
            
    # If we get here, all ingredients are sufficient
    # Now deduct the ingredients using the same loop
    for i in MENU[coffee_type]["ingredients"]:
        resources[i] -= MENU[coffee_type]["ingredients"][i]
            
    return True  # Successfully made the coffee

def cost(coffee_type):
    global money
    if total > MENU[coffee_type]["cost"]:
        change = total - MENU[coffee_type]["cost"]
        print(f"This is your change: {change:.2f}")
        money += MENU[coffee_type]["cost"]
        
    elif total == MENU[coffee_type]["cost"]:
        money += MENU[coffee_type]["cost"]
        
    else:
        print("Sorry that's not enough money. Money refunded.")

coffee_machine_on = True
money = 0
while coffee_machine_on:
    choice = input("Available:\n Espresso - 1.5$\n Latte- 2.5$\n Cappuccino - 3.0$\nWhat would you like? ").lower()
    
    if choice in ['espresso', 'latte', 'cappuccino']:
        
        operations(choice)
        print("\n"*2)
        print("Please insert coins.")
        

        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        
        total = 0
        total += quarters + dimes + nickels + pennies
        
        cost(choice)

    
    elif choice == 'report':
        
        print(f"Coffee: {resources["coffee"]}gr")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Water: {resources["water"]}ml")
        print(f"Money: ${money}")
        print("\n"*2)
        
    elif choice == "off":
        coffee_machine_on = False
    
    else:
        print("Invalid input. Please choose one of the options below: ")
    
        
    