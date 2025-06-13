
from turtle import Turtle, Screen

timmy = Turtle()

# for _ in range(50):
#     timmy.forward(5)    # moving forwared 5 paces
#     timmy.penup()       #pen up no drawing now 
#     timmy.forward(5)    # moving forward 5 paces without drawing anything
#     timmy.pendown()     #then pen down that means it is now ready to draw


for _ in range(20):
    timmy.forward(5)
    timmy.color("white")
    timmy.forward(5)
    timmy.color("black")

screen = Screen()
screen.exitonclick()
