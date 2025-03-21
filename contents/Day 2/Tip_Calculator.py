print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip you would like ot give? 10, 12 or 15?"))*total/100
people = int(input("How many people should split the bill?"))
pay = round((total + tip) / people, 2)

print(f"Each person should pay: ${pay}")