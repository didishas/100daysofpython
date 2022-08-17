from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup (width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win ? Enter a color: ")
is_race_on = False

turtles = {}
colors = ["yellow", "green", "red", "orange", "blue", "purple"]
width, height = -240, -160


for i in range(0,6):
    color = colors[i]
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(width, height)
    height += 60
    

if user_bet:
    is_race_on = True
    
    
while is_race_on:
    print("race")
    for color in colors:
        turtles[color].forward(random.randint(0, 10))
        if turtles[color].xcor() >= 230:
            if turtles[color].pencolor() == user_bet:
                print(f"You have won the game, the winning color is {turtles[color].pencolor()}")
            else:
                print(f"You have lost the game, the winning color is {turtles[color].pencolor()}")
            is_race_on = not is_race_on
            break


screen.exitonclick()