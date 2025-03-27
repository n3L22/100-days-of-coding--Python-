import random
from ascii_codes import stages
from list_of_words import word_list

print("""                 Welcome to the best Hangman Game
            ~Done by the precious 'Antonela Rakipaj'
        -------🤖--------Enjoy the game!!---------🤖-----""")
word = random.choice(word_list)
display = list("_" * len(word))

output = " ".join(display)
print(f"The word is: {output}")
lives = 6

while lives > 0:
    answer = input("Guess a letter:").lower()
    if answer in word:  
        for position in range(len(word)):
            if word[position] == answer:
                display[position] = answer
        output = " ".join(display)
        print(output)
    else:
        lives -= 1
        print(f"Meh, {lives} lives left")
        print(stages[lives])
        
        
    if "_" not in display:
        print("*******************🥇WINNER***************************\n")
        game_over = True

print("*********************😿  DISSAPOINTED**************************\n")
print(f"The word was {word}. Maybe next time!\n")