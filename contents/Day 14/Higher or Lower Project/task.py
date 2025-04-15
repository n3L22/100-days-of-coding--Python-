import random
from art_facts import facts, art

score = 0

# Get initial options
def get_options():
    variants = []
    for i in range(2):  # Loop twice
        random_fact = random.choice(list(facts.keys()))
        variants.append(random_fact)
    return variants

# Initial selection
options = get_options()
a = options[0]
b = options[1]

# Game loop
game_active = True
while game_active:
    # Display current comparison
    print(f"Compare A: {a}")
    print(art)
    print(f"Against B: {b}")
    
    # Get user choice
    choice = input("Which one do you think has more followers? 'A' or 'B': ").lower()
    
    # Process the choice
    if choice == 'a':
        if facts[a] > facts[b]:
            score += 1
            print(f"You are right!! Your score is {score}")
            # Keep a, get new b
            temp_b = b
            while temp_b == b:  # Make sure we get a different fact
                temp_b = random.choice(list(facts.keys()))
            b = temp_b
        else:
            print(f"You lose, Your score was {score}")
            game_active = False
            
    elif choice == 'b':
        if facts[b] > facts[a]:
            score += 1
            print(f"You are right!! Your score is {score}")
            # Move b to a, get new b
            a = b
            temp_b = b
            while temp_b == b:  # Make sure we get a different fact
                temp_b = random.choice(list(facts.keys()))
            b = temp_b
        else:
            print(f"You lose, Your score was {score}")
            game_active = False
    else:
        print("Invalid input. Please enter 'A' or 'B'.")

