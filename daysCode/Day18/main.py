#####Turtle Intro######

from turtle import Turtle, Screen

tim = Turtle()
tim.speed(speed=1)
screen = Screen()

tim.shape("turtle")
tim.color("red")


######## Challenge 1 - Draw a Square ############
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
# tim.setheading(0)

########### Challenge 2 - Draw a Dashed Line ########

# for i in range(20):
#     tim.forward(7)
#     tim.penup()
#     tim.forward(3)
#     tim.pendown()

########### Challenge 3 - Draw Shapes ########
# import random
#  tim.colormode(255)

# for _ in range(4, 10):
#     r,g,b = random.random(0, 255), random.random(0, 255), random.random(0, 255)
#     tim.pencolor((float(r),float(g),float(b)))
#     for turn in range(_):
#       tim.forward(100)
#       tim.right(360 / _)


########### Challenge 4 - Random Walk ########
import random

directions = (1, 2)
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

is_continued = True
tim.pensize(5)
tim.speed(20)

while is_continued:
    dir_choice = random.choice(directions)
    col_choice = random.choice(colours)
    tim.pencolor(col_choice)
    if dir_choice == 1:
        tim.forward(20)
        tim.left(90)
    else:
        tim.forward(20)
        tim.right(90)


screen = Screen()
screen.exitonclick()
