print("::::Welcome to the tip Calculator::::")
total_bill = float(input("What was the total bill? $"))

tip = int(input("what percentage tip would you like to give? 10, 12, 0r 15? "))

num_person = int(input("How many people to split the bill? "))
tip = total_bill*(tip/100)
total_bill += tip

split_bill = round(total_bill/num_person,2)

print(f"\nEach person should pay: ${split_bill}")