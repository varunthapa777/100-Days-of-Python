print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


low_name1 = name1.lower()
low_name2 = name2.lower()

total_true = 0

total_true = low_name1.count("t")+low_name1.count("r")+low_name1.count("u")+low_name1.count("e")

total_true += low_name2.count("t")+low_name2.count("r")+low_name2.count("u")+low_name2.count("e")

total_love = 0

total_love = low_name1.count("l")+low_name1.count("o")+low_name1.count("v")+low_name1.count("e")

total_love += low_name2.count("l")+low_name2.count("o")+low_name2.count("v")+low_name2.count("e")

score = int(str(total_true)+str(total_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
