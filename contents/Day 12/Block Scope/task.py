#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()

#Global scope 
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

#there is no block scope in python 
#so when we use an if loop it doesn't matter that the variable inside is a local variable
#as long as it is not inside a function then everything is ok!

#prime number
def is_prime(num):
    
    if num == 2:
        print("T")
    if num == 1:
        print("F")
        
    for i in range(2,num):
        if num % i == 0:
            print("F")
    
    print("T")
    
is_prime(1)



