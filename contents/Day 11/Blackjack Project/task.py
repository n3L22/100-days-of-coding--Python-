'''Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (Y) to take another card.
      (N) to Pass.
      The dealer stops hitting at 17.
      '''

import random
from image import art

print(art)
deck_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

deck = {
    "cards":{
        "your_cards" : [],
        "Pc_cards":[random.choice(deck_cards)]
    },
    "results":{
        "our_result": 0,
        "pc_result": 0
    }
}

for i in range(2):
    card = random.choice(deck_cards)
    deck['cards']['your_cards'].append(card)
    deck['results']['our_result'] += card
    
print(f"Your cards: {deck['cards']['your_cards']}, current score: {deck['results']['our_result']}")
print(f"Computers first card: {deck['cards']['Pc_cards']}")
