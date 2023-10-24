
import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

length = len(names)

random_name = names[random.randint(0, length - 1)]

print(f"{random_name} is going to buy the meal today!")
