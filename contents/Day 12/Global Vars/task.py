player_health = 10

def drink_potion():
    global player_health
    player_health += 2
    print(player_health)

drink_potion()

#in order to change a global variable inside a local scope we use global keyword 

#the cons of using global is that no matter before or after the function where this variable 
# was declared it will always call it!

#instead we can use the return function to modify an outside variable like below:

player_health  = 1

def drink_potion(health):
    return health + 1

player_health = drink_potion(player_health)
print('test1',player_health)