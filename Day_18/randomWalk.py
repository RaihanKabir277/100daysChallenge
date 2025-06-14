
from turtle import Turtle, Screen
import random

timmy = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
            "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     timmy.right(angle)
#     timmy.forward(steps)
# timmy.pen(fillcolor="black", pencolor="red", pensize=10)
# timmy.forward(100)

def right():
    return timmy.right(random.choice(directions))
def left():
    return timmy.left(random.choice(directions))

actions = [right, left]

timmy.pensize(10)

# for i in range(20):
#     timmy.forward(30)
#     timmy.left(90)         #stairs drawing code 
#     timmy.forward(30)
#     timmy.right(90)
    
for n in range(40):
    timmy.color(random.choice(colours))
    timmy.forward(10)
    random.choice(actions)()
    timmy.forward(10)



screen = Screen()
screen.exitonclick()
