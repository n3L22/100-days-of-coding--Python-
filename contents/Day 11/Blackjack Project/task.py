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
    """Return a random card from the deck"""
    deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck_cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Check for an 11 (ace). If the score is over 21, remove the 11 and replace it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose!!"
    elif computer_score > 21:
        return "Opponent went over. You win!!"
    elif user_score > computer_score:
        return "You win!!"
    else:
        return "You lose!!"

def play_game():
    print(art)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    # Deal 2 cards each to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check if game should end
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' for another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Computer's turn - computer keeps drawing cards until it has a score of at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    # Show final hands and result
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)  # Clear the screen
    play_game()