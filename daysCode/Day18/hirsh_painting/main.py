import colorgram, os
from PIL import Image
from turtle import Turtle, Screen, colormode
import random

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir+'/image.jpg')
rgb_colors = []
colors = colorgram.extract(cur_dir+'/image.jpg', 30)
for color in colors:
    rgb_colors.append(tuple(color.rgb))

colormode(255)

timy = Turtle()
screen = Screen()

timy.penup()
timy.setx(-200)
timy.sety(-300)

for line in range(10):
    timy.sety(-300 + (line*50))
    timy.setx(-200)
    for _ in range(10):
        choosen_color = random.choice(rgb_colors)
        timy.dot(20, choosen_color)
        timy.forward(50)
        
screen.exitonclick()    
