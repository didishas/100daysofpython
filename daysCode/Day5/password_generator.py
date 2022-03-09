import random

# Password Generator Project

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters_list randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

characters_list = [letters, symbols, numbers]

numchar_per_list = [nr_letters, nr_symbols, nr_numbers]

total_numchar = sum(numchar_per_list)

password_chars = []

for n in range(0, total_numchar):
    # Choosing random character[random_char] in a random char_list[random_list]
    # 1 Choosing random index in the stored list of user input
    random_list_index = random.randint(0, len(numchar_per_list) - 1)
    # 2 List (letters, symbols or numbers) from stored list
    random_list = characters_list[random_list_index]
    # 3 Random Character from list chosen
    random_char = random_list[random.randint(0, len(random_list) - 1)]
    # 4 Append random char in password list
    password_chars.append(random_char)
    # TWEAK
    numchar_per_list[random_list_index] -= 1
    # remove list of char if nr_char == 0
    if 0 in numchar_per_list:
        index_char_list_to_remove = numchar_per_list.index(0)
        numchar_per_list.pop(index_char_list_to_remove)
        characters_list.pop(index_char_list_to_remove)

pwd_string = "".join(password_chars)
print(pwd_string)
