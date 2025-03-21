print("welcome to Pizza Deliveries")
size = input("What size do you want your pizza? S, M , L?")
pepperoni = input("Do you want peperoni on your pizza? Y or N?")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N?")
bill = 0

if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
    print(f"Total bill is ${bill}")
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Total bill is ${bill}")
else:
    bill = 25
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Total bill is ${bill}")