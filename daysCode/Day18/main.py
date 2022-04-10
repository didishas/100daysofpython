#####Turtle Intro######

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(speed=1)
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


######## Challenge 1 - Draw a Square ############
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
timmy_the_turtle.setheading(0)

screen = Screen()
screen.exitonclick()
