import prettytable

data = prettytable.PrettyTable()
data.field_names = ["Pokemon Name", "Pokemon Type"]
data.align["Pokemon Name"] = "l"  # Left align
data.align["Pokemon Type"] = "c"  # Center align
data.padding_width = 1  # One space between column edges and contents
data.hrules = prettytable.ALL  # Draw lines between all rows
data.vrules = prettytable.ALL  # Draw lines between all columns
data.add_row(["Pikachu", "Electric"])
data.add_row(["Charmander", "Fire"])
data.add_row(["Squirtle", "Water"])
data.add_row(["Bulbasaur", "Grass"])
data.add_row(["Jigglypuff", "Normal"])

print(data)
