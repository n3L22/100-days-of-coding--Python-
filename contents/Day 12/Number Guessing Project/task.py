#number guessing game 
import random

attempts = 0 
choice = input("Choose a difficulty. 'easy' or 'hard': ").lower()

def level(levels):
    if choice == 'easy':
        return levels + 10
    elif choice == 'hard':
        return levels + 5
    
def main(lives):
    number = random.randint(1,100)
    #print(number) to check the code 
    while lives > 0:
        print(f"\nYou have {lives}, attempts left to guess the number!")
        guess = int(input("Make a guess:"))
        if guess == number:
            print(f"You won!!! The number was {number}.")
            break
        
        elif guess > number:
            print("Lower the number!! ⬇️")
        else:
            print("Think of a bigger number! ⬆️")

        lives -=1
        
    if lives == 0:    
        print(f"You ran out of lives The number was {number}!! Try again tomorrow! 🥹")
    
attempts = level(attempts)
main(attempts)
        
        
