import random 
friends = ["Alice", "Bob", "Charlie", "Davide"]
#1 Option
print(random.choice(friends))
#2 Option
random_index = random.randint(0, 3)
print(friends[random_index])
