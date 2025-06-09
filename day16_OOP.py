
# import day16_AnotherModule

# print(day16_AnotherModule.another_variable)

# import turtle

# timmy = turtle.Turtle()

# Simplest way given below ------ 

# from turtle import Turtle

# timmy = Turtle()
# print(timmy)


# Basic attributes starts here .......

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)  #canvheight is the Attributes of my screen......


# Basic methods starts here ---------



# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) 
# my_screen.exitonclick()



# ------------ Pypi packages starts here -----------



from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age"]
table.add_row(["Alice", 30])
table.add_row(["Bob", 25])

print(table)




