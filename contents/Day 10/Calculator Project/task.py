def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 /n2


storing = {"-":subtract,
           "+":add,
           "*":multiply,
           "/":divide}

#if you want to multiply call the key to get both key and value in ->() type what do you want to execute
#storing["*"](4,8)

def calculator():
    print("Calculator APP")
    num1 = float(input("What is your first number? "))

    while True:
        
        for operations in storing:
            print(operations)

        choice = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))

        result = (storing[choice](num1, num2))
        print(num1, choice, num2, '=', result)

        choice2 = input(f"Do you want to operate with {result}? Type 'Y' for yes or 'N' for no: ").lower()

        if choice2 == 'y':
            num1 = result
            
        if choice2 == 'n':
            False
            print('\n' *100)
            #when you call a function inside of it you call it recursion
            calculator()
            


calculator()