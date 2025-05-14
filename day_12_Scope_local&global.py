
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")

# increase_enemies()
# print(f"enemies inside function {enemies}")

# --------------- local scope  ---------------

# def drink_position():
#     potion_strength = 2
#     print(potion_strength)

# drink_position()

# print(potion_strength) #it will give an error because we can not acces a variable from inside the function to outside the function

# -------------Global scope --------

# player_health = 10  #global variable
# def drink_position():
#     potion_strength = 2
#     print(player_health)

# drink_position()


# but without function it will work --

# game_level = 3
# enemies = ["skeleton", "Zombia", "Alion"]

# # def create_enemy():
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)


# --------------modify a global variable ----------

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 2            #here we can not modify a local variable of same name without declare the global type csating ..

#     print(f"enemies inside function {enemies}")

# increase_enemies()
# print(f"enemies inside function {enemies}")

# but this way it will change the global varible value , for this problem there is a solve below /.............

# enemies = 1

# def increase_enemies(enemy):
#     return enemy + 1
    

# output = increase_enemies(enemies)
# print(output)
# print(f"enemies outside function {enemies}")




# ----------python constant & global variable ------------

PI = 3.1416


# its a global constant and dont want to change this value either 





