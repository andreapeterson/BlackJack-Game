############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 1]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import os
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
import random

def deal_two_cards():
  return random.choices(cards, k=2)
  
def deal_one_card():
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, comp_score):
  if user_score == comp_score:
    return "🏁🏁🏁Draw.🏁🏁🏁"
  elif comp_score==0:
    return "🏁🏁🏁You Lose, dealer has Blackjack.🏁🏁🏁"
  elif user_score==0:
    return "🏁🏁🏁You win with a Blackjack!🏁🏁🏁"
  elif user_score>21:
    return "🏁🏁🏁You lose, you went over.🏁🏁🏁"
  elif comp_score>21:
    return "🏁🏁🏁 You win, dealer went over!🏁🏁🏁"
  elif user_score> comp_score:
    return "🏁🏁🏁You win, you had the highest score.🏁🏁🏁"
  else:
    return "🏁🏁🏁You lose, dealer had a higher score.🏁🏁🏁"
  

def play_game():
  
  print(logo)
  
  user_cards=deal_two_cards()
  user_cards_list=[]
  for items in user_cards:
    user_cards_list.append(items)
        
  comp_cards=deal_two_cards()
  comp_cards_list=[]
  for items in comp_cards:
    comp_cards_list.append(items)
  
  should_continue= True
  
  while should_continue:
    user_score=calculate_score(user_cards_list)
    comp_score= calculate_score(comp_cards_list)
      
    print(f"  Your cards: {user_cards_list}. Your current score is: {user_score}")
    print(f"  Computer's first card: {comp_cards_list[0]}")
  
    if user_score>=21 or user_score==0 or comp_score==0:
      should_continue=False
      
    else:
      answer2=input("Do you want to draw another card? Type 'y' to get another card or type 'n' to keep your current hand: ")
      if answer2=="y":
        user_cards_list.append(deal_one_card())
      else:
        should_continue=False
        
        
      
  while comp_score !=0 and comp_score<17:
      comp_cards_list.append(deal_one_card())
      comp_score=calculate_score(comp_cards_list)
  
  print(compare(user_score, comp_score))
  
  print(f"  Your final hand: {user_cards_list}, final score: {user_score}")
  print(f"  Computer's final hand: {comp_cards_list}, final score: {comp_score}")
  






while input("Do you want to play a game of python Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
else:
  clear()
  print("Thank you for playing! Have a great day and may luck be forever in your favor!")
