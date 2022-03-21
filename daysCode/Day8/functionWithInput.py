# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hello, My name is Sally")
    print("I am the AI")
    print("I will Help you during your journey.")


greet()


def greet_with_name(name="Didier"):
    print(f"Hello {name}")
    print(f"I am the AI for you, {name}")
    print("I will Help you during your journey.")


greet_with_name()


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"I am the AI for you, {name}")
    print(f"I will Help you during your {location} journey.")


greet_with("Cathy", "computing")
