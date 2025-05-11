
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

game_level = 3
enemies = ["skeleton", "Zombia", "Alion"]

# def create_enemy():
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)




