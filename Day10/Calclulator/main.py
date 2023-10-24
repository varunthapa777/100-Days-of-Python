from art import logo
import os


def operation(a,b,op):
  """ Thi functin take two numbers and one operator as input
  and return the result of operation"""
  if op == "+":
    return a + b
  elif op == "-":
    return a - b
  elif op == "*":
    return a * b
  elif op == "/":
    if b == 0:
      return "Invalid operation"
    return a / b
  else:
    return "Invalid operation"


while(True):
  restart = False
  while(not restart):
    print(logo)
    ch = ''
    num1 = float(input("What's the first number?: "))
  
    print("""+
-
*
/""")
    op = input("Pick an Operator: ")
  
    num2 = float(input("What's the next number?: "))
  
    result = operation(num1,num2,op)
  
    print(f"{num1} {op} {num2} = {result}")
  
    if result == "Invalid operation":
      input("Press any key to continue").lower()
    else:
      ch = input(f"Press 'y' to continue calc with {result} or type 'n' to restart: ")
    
    while(ch == 'y'):
      num1 = result
      print("""+
-
*
/""")
      op = input("Pick an Operator: ")
  
      num2 = float(input("What's the next number?: ")) 
  
      result = operation(num1,num2,op)
      
      print(f"{num1} {op} {num2} = {result}")
  
      if result == "Invalid operation":
        input("Press any key to continue").lower()
        ch = "n"
      else:
        ch = input(f"Press 'y' to continue calc with {result} or type 'n' to restart: ")
  
    restart = True
    os.system('cls')