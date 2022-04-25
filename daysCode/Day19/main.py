from turtle import Turtle, Screen


timy = Turtle()
screen = Screen()



def move_forward():
    timy.forward(10)

def move_backward():
    timy.backward(10)

def move_counter_clockwise():
    timy.right(10)

def move_clockwise():
    timy.left(10)

def clear():
    timy.penup()
    timy.clear()
    screen.clear()
    timy.home()
    timy.pendown()

screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=move_counter_clockwise, key="a")
screen.onkeypress(fun=move_clockwise, key="d")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()