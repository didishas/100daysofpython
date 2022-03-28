import random
from os import system
from art import logo, vs
from game_data import data


# section Intial variables
# score
score = 0
current_card = {}
new_card = {}


# section function
# * choose random Card
def get_random_card(arr):
    return random.choice(arr)

# * choose new card
def get_new_card(arr, current_card):
    new_card = {}
    while current_card == new_card or new_card:
        print('not yet')
    new_card = get_random_card(arr)
    return new_card

# * compare two card return only one
def get_highest_card(card1, card2):
    if card1['follower_count'] > card2['follower_count']:
        return card1
    else:
        return card2
    
def swap_current(current_card, new_card):
    current_card = new_card
    
# * keep scores
# def add_score(score):
#     return score += 1
# section end functions

# * compare guessed card
def game():
    score = 0
    # section printing logo and choosing cards
    # choices
    choices = 4
    current_card = get_random_card(data)
    
    while choices > 0:
        system("clear")
        print(logo) 
        new_card = get_new_card(data, current_card)

        # section printing cards and VS LOGO
        print(f"The score: {score}")
        print(f"Compare A: {current_card['name']}, {current_card['description']}, from {current_card['country']}")
        print(vs)
        print(f"Against B: {new_card['name']}, {new_card['description']}, from {new_card['country']}")
        
        # section compare
        answer = input("Who has more followers? Type 'A' or 'B': ")
        user_choice = {}
        
        if 'A' == answer:
            user_choice = current_card
        else:
            user_choice = new_card
        
        if get_highest_card(current_card, new_card) == user_choice:
            score += 1
        current_card = new_card
        choices -= 1 
    print(f"Final score is {score}")
    
game()
        
# ? compare followers 
# ? report score
# ? Check choices is_left
# ? swap current_card by new_card and choose new_card
