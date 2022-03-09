# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

name_combined = name1_lower + name2_lower

# Counting tens
tens = name_combined.count("t")
tens += name_combined.count("r")
tens += name_combined.count("u")
tens += name_combined.count("e")

# Counting units
units = name_combined.count("l")
units += name_combined.count("o")
units += name_combined.count("v")
units += name_combined.count("e")

love_result = str(tens) + str(units)

if int(love_result) < 10 or int(love_result) > 90:
    print(f"Your score is {love_result}, you go together like coke and mentos.")
elif 40 < int(love_result) and int(love_result) < 50:
    print(f"Your score is {love_result}, you are alright together.")
else:
    print(f"Your score is {love_result}.")
