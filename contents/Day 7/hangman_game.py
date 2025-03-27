import random
word_list = ["hardwork","baboon","camel"]

word = random.choice(word_list)

answer = (input("Guess a letter:")).lower
print(type(word),type(answer) )
for letter in word:
    if letter == answer:
        print("wrong")
    elif letter != answer:
        print (letter)
        print("correct")

