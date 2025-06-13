
from turtle import Turtle, Screen
import random
timmy = Turtle()

# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.color("red")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.color("green")
# timmy.forward(100)
# timmy.right(72)
# timmy.forward(100)
# timmy.right(72)
# timmy.forward(100)
# timmy.right(72)
# timmy.forward(100)
# timmy.right(72)
# timmy.forward(100)
# timmy.right(72)

# num_sides = 5
# timmy.color("red")

colors = ["red","green","black","medium sea green","ivory","khaki","cyan","azure"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    # timmy.color(col)
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(n)

screen = Screen()
screen.exitonclick()