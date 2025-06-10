
# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table)


# ------ Alignment of the table ---------


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["kire", "bangla"])
# table.align = "l"
table.align = "r"
# table.border = False


print(table)

