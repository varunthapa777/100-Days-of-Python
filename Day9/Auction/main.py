import os
from logo import gavel

print(gavel)

bidder_data = []

print("Welcome to the secret auction program.")

end_of_bid = False

while(not end_of_bid):
  name = input("What is your Name?: ")
  bid = int(input("What's you Bid?: "))

  bid_info = {}

  bid_info["name"] = name
  bid_info["bid"] = bid

  bidder_data.append(bid_info)

  ch = input("Are there any other bidder?[Y/N] ").lower()

  end_of_bid = ch != "y" 
  os.system('cls')


max = 0
higest_bidder = {}
for bidder in bidder_data:  
  
  if max < bidder["bid"]:
    max = bidder["bid"]
    higest_bidder = bidder


print(gavel)
print("::::::::::::ITEM::SOLD!:::::::::::::::\n")
print("Highest Bidder : "+higest_bidder["name"])
print("Bidding Price : $"+str(higest_bidder["bid"]))

    