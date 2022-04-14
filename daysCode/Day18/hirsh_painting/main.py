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

timy.setheading(225)
timy.forward(300)
timy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timy.dot(20, random.choice(rgb_colors))
    timy.forward(50)
    
    if dot_count % 10 == 0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)
    
screen.exitonclick()