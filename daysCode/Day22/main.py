from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Pong Game')

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up,"Up")
screen.onkey(paddle.move_down,"Down")

game_over = False

# while not game_over:
    
screen.exitonclick()