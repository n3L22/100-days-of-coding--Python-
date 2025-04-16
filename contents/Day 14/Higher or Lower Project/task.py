from art_facts import data, art
import random


def check_answer(user_guess, a_key, b_key):
    """Take a user's guess and the account keys and returns if they got it right."""
    a_followers = data[a_key]
    b_followers = data[b_key]
    
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True

# Get list of all accounts
all_accounts = list(data.keys())

# Generate a random account to start
account_b = random.choice(all_accounts)

# Make the game repeatable
while game_should_continue:
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(all_accounts)
    
    # Make sure accounts A and B are different
    while account_a == account_b:
        account_b = random.choice(all_accounts)
    
    print(f"Compare A: {account_a}")
    print(art)
    print(f"Against B: {account_b}")
    
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Check if user is correct
    is_correct = check_answer(guess, account_a, account_b)
    
    # Clear the screen
    print("\n" * 3)
    
    # Give user feedback on their guess and update score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False