import random
from art_facts import facts, art

# Initialize the game
score = 0

# Get initial options A and B
available_options = list(facts.keys())
current_a = random.choice(available_options)

print( "Welcome to the Higher or Lower game!")
# Get B, making sure it's different from A
available_options.remove(current_a)
current_b = random.choice(available_options)

# Main game loop
while True:
    # Display the current options
    print(f"Compare A: {current_a}")
    print(art)
    print(f"Against B: {current_b}")
    
    # Get the player's choice
    while True:
        choice = input("Which one do you think has more followers? 'A' or 'B': ").lower()
        if choice in ['a', 'b']:
            break
        print("Invalid input. Please enter 'A' or 'B'.")
    
    # Check if the player's answer is correct
    if choice == 'a':
        if facts[current_a] > facts[current_b]:
            score += 1
            print(f"You are right!! Your score is {score}")
            # Keep A as A, get new B
            available_options = list(facts.keys())
            available_options.remove(current_a)
            current_b = random.choice(available_options)
        else:
            print(f"You lose. Your final score was {score}")
            break
    else:  # choice == 'b'
        if facts[current_b] > facts[current_a]:
            score += 1
            print(f"You are right!! Your score is {score}")
            # Move B to position A, get new B
            current_a = current_b
            available_options = list(facts.keys())
            available_options.remove(current_a)
            current_b = random.choice(available_options)
        else:
            print(f"You lose. Your final score was {score}")
            break