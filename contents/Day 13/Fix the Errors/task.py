#we can use try except methods for debugging 

try:
    age = int(input("How old are you?"))
    #the type of error you can find it in the traceback call when you click run
    
except ValueError:
    print("Invalid error only numbers allowed as input!!")
    age = int(input("How old are you?"))

if age > 20:
    print(f"You can drive at this age {age}")