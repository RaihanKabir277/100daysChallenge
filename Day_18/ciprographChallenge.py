
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)

timmy.speed("fastest")

# for _ in range(3):
#     timmy.color(random_color())
#     timmy.circle(60)
#     # current_heading = (timmy.heading())
#     # timmy.setheading(current_heading + 10)

#     # redundant this two lines od code below

#     timmy.setheading(timmy.heading() + 10) 

def draw_spirograph(size_of_gaph):
    for _ in range(int(360 / size_of_gaph)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gaph)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
