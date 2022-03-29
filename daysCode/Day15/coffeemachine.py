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
        if k in ["water", "milk"]:
            print(f"{k}: {v}ml")
        elif k == "coffee":
            print(f"{k}: {v}g")
        else:
            print(f"{k}: ${round(v, 2)}")


def get_coins_total(quarter, dime, nickle, penny):
    total = 0
    total += CHANGE["quarter"] * quarter
    total += CHANGE["dime"] * dime
    total += CHANGE["nickle"] * nickle
    total += CHANGE["penny"] * penny
    return total


def give_change_back(total, price):
    change = round((total - price), 2)
    if change > 0:
        print(f"Here is  ${change} in change")
    return change


def check_ressources(usr_request, res):
    is_enough = True

    for k, v in MENU[usr_request]["ingredients"].items():
        if v > res[k]:
            is_enough = False
            return is_enough
    return True


def reduce_res(usr_request, res):
    for k, v in MENU[usr_request]["ingredients"].items():
        res[k] -= v


usr_request = "on"
resources["Money"] = 0
while usr_request != "off":
    usr_request = input("What would you like ? (espresso, latte, capuccino): ")

    while usr_request not in ["espresso", "latte", "capuccino", "report", "off"]:
        usr_request = input("Sorry we only serve => espresso, latte, capuccino ")

    if usr_request == "report":
        get_report()
    elif usr_request in ["espresso", "latte", "capuccino"]:
        print("Please insert coins.")
        quarter = float(input("How many quarter?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))

        total = get_coins_total(quarter, dimes, nickles, pennies)
        resources["Money"] += total
        price = MENU[usr_request]["cost"]

        change = give_change_back(total, price)

        if change >= 0:
            is_ressource_enough = check_ressources(usr_request, resources)
            if is_ressource_enough:
                reduce_res(usr_request, resources)
                print(f"Here is your {usr_request} ☕ Enjoy.")
            else:
                print("Not enough resources")
        else:
            print(f"Sorry that's not enough money. ${change} refunded")
    else:
        print("Off")
