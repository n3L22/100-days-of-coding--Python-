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


def deal_card():
    """return a random card from the deck"""
    deck_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(deck_cards)
    return card

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the code"""
    #we do sum 21 because we are checking if 11 and 10 are in the cards 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, p_score):
    if u_score == p_score:
        return "Draw!!"
    elif p_score == 0:
        return "Lose, Opponent has a BlackJack"
    elif u_score == 0:
        return "Win with a a Blackjack"
    elif u_score > 21:
        return "You went over. You lose!!"
    elif p_score >21:
        return "Opponent went over. You win!!"
    elif u_score > p_score:
        return "You got over the winner. You win!!"
    else:
        return "You lose!!"

def play_game():
    print(art)
    user_cards = []
    pc_cards = []
    pc_score = -1
    user_score = -1
    is_game_over = False


    for _ in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards) 
        pc_score = calculate_score(pc_cards) 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' for another card or type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while pc_score != 0 and pc_score < 17:
        pc_score.append(deal_card())
        computer_score = calculate_score(pc_score)
    
    
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computers first card: {pc_cards}")
print(compare(user_score, pc_score))


while input("Type 'y' for another card or type 'n' to pass:") == 'y':
    print("\n"*20)
    play_game()