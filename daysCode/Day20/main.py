from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')


# Initialisation of major pieces   
snake = Snake()
food = Food()
score = Scoreboard()

# binding key on the screen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        
        # extend snake
        snake.extend()
        
    # Detect collisions with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.game_over()
        game_is_on = False
        
    # Detect collisions with tail
    for segment in snake.segments:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
            
    


screen.exitonclick()