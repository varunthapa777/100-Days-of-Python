from art import logo
import os

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 7. Making a user manual open when type help
user_manual = {
    "help": "Show the user manual guide",
    "off": "Close the Program",
    "report": "Get the report of available resources and profit",
    "menu": "show variety of coffe with the price"
}


# coins
# QUARTER = 0.25
# DIME = 0.10
# NICKLE = 0.05
# PENNY = 0.01


# TODO: 3. check resource is sufficient for process?
def check_resource(coffee):
    if menu[coffee]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif menu[coffee]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif menu[coffee]["ingredients"]["coffee"] > resources["milk"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO: 4 calculate the coins and check money is sufficient or not and give change
def process_coin(coffee):
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    coffee_cost = menu[coffee]["cost"]
    total = round((quarters + dimes + nickles + pennies), 2)

    if coffee_cost > total:
        return 0
    else:
        change = total - coffee_cost
        print(f"Here is ${change} in change")
        return coffee_cost


# TODO: 5. making coffe by using the resources
def make_coffe(coffee):
    resources["water"] -= menu[coffee]["ingredients"]["water"]
    resources["milk"] -= menu[coffee]["ingredients"]["milk"]
    resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]


switch = True
profit = 0.0
print(logo)

while switch:
    # TODO:1. print prompt asking for Type of coffee
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. program should be terminate if prompt get the input 'off'
    match choice:

        case 'off':
            switch = False

        case 'report':
            print(f"Water : {resources['water']}ml")
            print(f"Milk : {resources['milk']}ml")
            print(f"Coffee : {resources['coffee']}g")
            print(f"money : ${profit}")

        case 'espresso' | 'latte' | 'cappuccino':

            isSufficient = check_resource(choice)

            if isSufficient:
                sold_money = process_coin(choice)
                if sold_money == 0:
                    print("Sorry that's not enough money. Money refunded")
                else:
                    profit += sold_money
                    make_coffe(choice)
                    print(f"Here is your {choice}☕. Enjoy!")

        case 'help':
            print("Command    Description")
            for cmd in user_manual:
                print(f"{cmd}  ->  {user_manual[cmd]}")

        case 'menu':
            print(" MENU ".center(28, ':'))
            print("{:<15}       {:>5}".format('Coffee', 'Price'))
            print("----------------------------")
            for coffee in menu:
                print("{coffee:<17}      ${price:<5}".format(coffee=coffee, price=menu[coffee]["cost"]))

        case _:
            print("Invalid input, For help type 'help'.")
