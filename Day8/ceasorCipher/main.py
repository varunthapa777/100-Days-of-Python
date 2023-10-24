alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import graphic
import os

def encrypt(text,shift):
  encoded_text = []
  
  for i in range(0,len(text)):

    if text[i].isalpha():
      shift_index = alphabet.index(text[i]) + shift
      encoded_text += alphabet[shift_index]
    else:
      encoded_text += text[i]
      
  print("The encoded text is: "+''.join(encoded_text))
  

def decrypt(text,shift):
  decoded_text = []

  for i in range(0,len(text)):

    if text[i].isalpha():
      shift_index = alphabet.index(text[i],26) - shift
      decoded_text += alphabet[shift_index]
    else:
      decoded_text += text[i]

  print("The decoded text is: "+''.join(decoded_text))


end_game = False
while(end_game != True):
  print(graphic.caesar_cipher)
  direction = input("Type 'encode' to encrypt, type 'decode'  to decrypt:\n")
  if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
      encrypt(text,shift)
    elif direction == "decode":
      decrypt(text,shift)
  else:
    print("Enter the correct choice!")

  cont = input("Do you want to contiue[y/n]: ")
  
  if cont.lower() == "n":
    end_game = True
  elif cont.lower() == 'y':
    end_game = False
    os.system('cls')
  
