from turtle import Turtle

FONT = ("Arial", 24, 'normal')
ALIGNEMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,268)
        self.hideturtle()
        self.color("white")
        self.update()
        
    def update(self):
        self.write(f'Score = {self.score}', align="center",font=("Arial", 24, 'normal'))
    
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNEMENT,font=FONT)
        
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update()
    
        
    
    
    
        