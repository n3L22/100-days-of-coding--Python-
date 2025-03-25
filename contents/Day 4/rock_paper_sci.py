# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
list_rps = [rock, paper, scissors]
pc_random = random.randint(0,2)

choice = int(input("Type what do you want to choose:\n Type 0 for Rock,\n Type 1 for Paper,\n Type 2 for Scissors.\n "))
print(f"Computer choose:{list_rps[pc_random]} ")

if choice >= 0 and choice <= 2:
    print(f"You choose:{list_rps[choice]} ")
    
if choice > 2 and choice < 0:
    print("Invalid data type!!")

if choice == 0 and pc_random == 2:
    print("You won")
elif choice == 2 and pc_random == 0:
    print("You lose")
elif choice > pc_random:
    print("You won")
elif choice < pc_random:
    print("You lose")
elif choice ==  pc_random:
    print("It is a draw")