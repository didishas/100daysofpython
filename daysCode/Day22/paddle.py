from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(3,1)
        self.goto(280, 0)
        self.color("white")
        
        
    def move_up(self):
        print("up")
        new_y = self.ycor() + 5
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        print("down")
        self.down()