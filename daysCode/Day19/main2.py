from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
    print("moved from 10 mesures")

screen.listen()
screen.onkeypress(key='space', fun=move_forward)

screen.exitonclick()