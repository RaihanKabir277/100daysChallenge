

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


directions = [0, 90, 180, 270]   #nort south east west 
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()