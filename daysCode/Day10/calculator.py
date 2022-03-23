from art import logo
import os


# Calculator

# Add
def add(a, b):
    return a + b


# Substract
def substract(a, b):
    return a - b


# Multiply
def multiply(a, b):
    return a * b


# Divide
def divide(a, b):
    return a / b


operations = {"+": add, "-": substract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    first_number = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for operator in operations:
            print(operator)
        
        symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        operation = operations[symbol]
        result = operation(first_number, second_number)

        print(f"{first_number} {symbol} {second_number} = {result}")

        if (
            input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            first_number = result
        else:
            should_continue = False
            calculator()

calculator()