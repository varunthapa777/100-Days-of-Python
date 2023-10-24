import random


actual_number = random.randint(1,100)

print( """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_ \\| |_| |  __/\__ \__ \\  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number b/w 1 to 100")
difficult = input("Choose a Difficulty: Type 'easy' or 'hard': ") != 'easy'

attempt = 5 if difficult else 10

while attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guessed_Number = int(input("Make a Guess: "))

    if guessed_Number == actual_number:
        print("YOU Guess It Right. YOU WIN!")
        break
    else:
        attempt -= 1
        if attempt == 0:
            print("You'r run Out of guesses, You Lose!  ")
        else:
            if guessed_Number > actual_number:
                print("Too High")
                print("Guess again.")
            else:
                print("Too Low")
                print("Guess again")  
        
        
        
        


