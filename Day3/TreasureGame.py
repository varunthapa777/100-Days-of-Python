print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your Mission is to find the treasure!")
move = input("Your at the crossroad.Where you want to go? Type 'left' or 'right'. ")

if move == "right":
  print("GameOver. You fall into the hole\n")
else:
  print("You reach at the end of island.There is another island.")
  move = input("Type 'swim' or 'wait' for the boat ")
  if move == "swim":
    print("GameOver! Your are ate by the sharks")
  else:
    print("Well Done You reach safely to the island")
    print("There are there doors red green yellow")
    move = input("Type 'red' or 'green' or 'yellow'.")
    if move == 'red':
      print("ohh Shit! Your get fired. GameOver")
    elif move == 'green':
      print("OHH God! the door get locked. you stuck there forever.")
    elif move == 'yellow':
      print("Well Done! You Got the treasure Full of Gold.")
    else:
      print("Go and learn some typing looser!")