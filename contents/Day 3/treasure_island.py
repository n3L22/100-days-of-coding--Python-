print("Welcome to Treasure Island \n You are in a crossroad what would you choose: ")
choice1 = input("LEFT OR RIGHT?")
if choice1 == 'LEFT':
    print("Great you arrived in an Island do you want to swim or wait for a car?")
    choice2 = input("Type Swim or Wait")
    if choice2 == 'Swim':
        print('Great you swim across which door would you choose: ')
        choice3 = input("Type Red, Blue, Yellow? ")
        if choice3 == 'Yellow':
            print('Winner')
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")