
from turtle import Turtle, Screen
import random

timmy = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
            "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]   #nort south east west 
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(20)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()