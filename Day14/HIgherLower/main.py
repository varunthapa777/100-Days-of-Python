import os
from data import *
from art import *
import random


def randint_exclude(start, end, exclude):

  r = random.randint(0, len(data) - 1)

  if r == exclude:
    return randint_exclude(start, end, exclude)
  else:
    return r


def higher(card1, card2):

    return True if card1['follower_count'] > card2['follower_count'] else False


def isGameOver(card1, card2, choice):

  if choice == 'a':
    if not higher(card1, card2):
      return True
    else:
      return False
  elif choice == 'b':
    if higher(card1, card2):
      return True
    else:
      return False
  else:
    return True


card1 = data[random.randint(0, len(data) - 1)]
card2 = data[randint_exclude(0, len(data) - 1, data.index(card1))]

print(logo)
score = 0
game_is_over = False
while (not game_is_over):

  print(
      f"Compare A: {card1['name']}, a {card1['description']}, {card1['country']}"
  )
  print(vs)
  print(
      f"Against B: {card2['name']}, a {card2['description']}, {card2['country']}"
  )

  choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  if isGameOver(card1, card2, choice):
    os.system('cls')
    print(f"Sorry that's wrong, final Score : {score}")
    ans = input("Want to play again? Type 'y' or 'n' : ").lower()
    if ans == 'y':
      score = 0
      card1 = data[random.randint(0, len(data) - 1)]
      card2 = data[randint_exclude(0, len(data) - 1, data.index(card1))]
      os.system('cls')
      print(logo)
    else:
      game_is_over = True
  else:
    score += 1
    os.system('cls')
    print(logo)
    print("You're Right, your score:", score)
    if higher(card1, card2):
      card1 = card2
      card2 = data[randint_exclude(0, len(data) - 1, data.index(card1))]
    else:
      card1 = card2
      card2 = data[randint_exclude(0, len(data) - 1, data.index(card1))]
