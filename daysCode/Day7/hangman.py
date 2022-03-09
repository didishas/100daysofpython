import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list
# and assign it to a variable called chosen_word.
random_word = random.choice(word_list)


# TODO-2 - Ask the user to guess a letter and assign
# their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess)
# is one of the letters in the chosen_word.
for n in range(0, len(random_word) - 1):
    print("Right") if guess == random_word[n] else print("Wrong")
