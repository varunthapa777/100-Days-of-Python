import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_list = [rock, paper, scissors]
hand_list_name = ["Rock", "Paper", "Scissors"]


player_comp = random.randint(0, 2)


player_hum = int(input("Enter 0 for Rock , 1 for Paper and 2 for Scissors\n"))

if player_hum == 0 or player_hum == 1 or player_hum == 2:
  print(hand_list[player_comp])
  print(f"compluter: {hand_list_name[player_comp]}\n")
  
  print(hand_list[player_hum])
  print(f"You: {hand_list_name[player_hum]}\n")

#logic
  if player_hum == 0:
      if player_comp == 1:
          print("YOU LOSE!\n")
      elif player_comp == 2:
          print("YOU WON!\n")
      else:
          print("DRAW!\n")
  elif player_hum == 1:
      if player_comp == 2:
          print("YOU LOSE!\n")
      elif player_comp == 0:
          print("YOU WON!\n")
      else:
          print("DRAW!\n")
  else:
      if player_comp == 0:
          print("YOU LOSE!\n")
      elif player_comp == 1:
          print("YOU WON!\n")
      else:
          print("DRAW!\n")
  

else:
  print("Enter the Correct Choice")