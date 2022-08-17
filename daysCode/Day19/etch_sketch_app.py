from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
    
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
    
def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
moves = {
    "w": move_forward,
    "s": move_backward,
    "a": turn_left,
    "d": turn_right,
    "c": reset
}


screen.listen()

screen.onkeypress(key="w", fun=moves["w"])
screen.onkeypress(key="s", fun=moves["s"])
screen.onkeypress(key="a", fun=moves["a"])
screen.onkeypress(key="d", fun=moves["d"])
screen.onkeypress(key="c", fun=moves["c"])
    
screen.exitonclick()