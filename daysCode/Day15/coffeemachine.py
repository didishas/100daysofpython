MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# section Constants
CHANGE = {"quarter": 0.25, "dime": 0.10, "nickle": 0.05, "penny": 0.01}


# section Helpers


def get_report():
    for k, v in resources.items():
        if k != "coffee":
            print(f"{k}: {v}ml")
        elif k == "coffee":
            print(f"{k}: {v}g")
        else:
            print(f"{k}: ${v}")


def get_coins_total(quarter, dime, nickle, penny):
    total = 0
    total += CHANGE["quarter"] * quarter
    total += CHANGE["dime"] * dime
    total += CHANGE["nickle"] * nickle
    total += CHANGE["penny"] * penny
    return total


def give_change_back(total, price):
    change = round((total - price), 2)
    print(f"Here is  ${change} in change")
    return change



usr_request = input("What would you like ? (espresso, latte, capuccino): ")

if usr_request == "report":
    get_report()
else:
    print("Please insert coins.")
    quarter = float(input("How many quarter?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = get_coins_total(quarter, dimes, nickles, pennies)
    price = MENU[usr_request]["cost"]

    change = give_change_back(total, price)
    
    if change >= 0:
        print(f"Here is your {usr_request} ☕ Enjoy.")
    else:
        print(f"It is not enough for a {usr_request}")
