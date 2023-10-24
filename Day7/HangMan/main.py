import os
import random
import wordlist
from graphic import stages, logo, heart

gameOver = False
lives = 6;
# word_list = ["aardvark", "baboon", "camel"]
word_list = wordlist.wordList

chosen_word = random.choice(word_list)

print(logo)

display = []

for _ in range(len(chosen_word)):
  display += "_"

# gameLogic
while not gameOver:
  guess = input("Guess a Letter: ").lower()

  os.system('cls')
  
  if guess not in display:
    for pos in range(len(chosen_word)):
      letter = chosen_word[pos]

      if letter == guess:
        display[pos] = letter

    print(f"{' '.join(display)}\n")
    
  else:
    print(f"{' '.join(display)}\n")
    print(f"Already Guessed letter {guess}")

  if guess not in chosen_word:
    print("You guessed Wrong, you losed a live")
    lives -= 1
    heart.pop()
  
  print(stages[lives])
  print(f"{''.join(heart)}")

  
  if "_" not in display:
    gameOver = True
    print("\n🥳YOU WIN!\n")

  if lives == 0:
    gameOver = True
    print("No lives left You Lose! 😿\n")
    print(f"The Word is '{chosen_word}'")
  