height = int(input("What is your height?"))
weight = int(input("What is your weight?"))
bmi = weight/height**2
print(bmi)

print(int(bmi)) #chops what comes after the . 
print(round(bmi)) #round to the nearest 0.5 int 

print(round(bmi, 2)) #to round it to 2 decimal places 