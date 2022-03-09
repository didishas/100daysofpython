import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

figures = [rock, paper, scissors]

introduction = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
player_choice = int(
    input(introduction)
)

print(figures[int(player_choice)])
cpu_choice = random.randint(0, 2)

print(f"Computer chose: \n{figures[cpu_choice]}", cpu_choice)

if player_choice == 0:
    if cpu_choice == 0:
        print("Draw")
    elif cpu_choice == 1:
        print("You lose")
    else:
        print("You win")
elif player_choice == 1:
    if cpu_choice == 1:
        print("Draw")
    elif cpu_choice == 2:
        print("You lose")
    else:
        print("You win")
else:
    if cpu_choice == 2:
        print("Draw")
    elif cpu_choice == 0:
        print("You lose")
    else:
        print("You win")
