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


# section Helpers


def get_report():
    for k, v in resources.items():
        if k != "coffee":
            print(f"{k}: {v}ml")
        elif k == "coffee":
            print(f"{k}: {v}g")
        else:
            print(f"{k}: ${v}")


usr_request = input("What would you like ? (espresso, latte, capuccino): ")

if usr_request == "espresso":
    print("espresso")
elif usr_request == "latte":
    print("latte")
elif usr_request == "capuccino":
    print("capuccino")
else:
    # print("report")
    get_report()
