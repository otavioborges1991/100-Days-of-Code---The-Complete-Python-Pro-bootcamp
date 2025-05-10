game_level = 3
enemies = ["skeleton", "zombie", "goblin"]

def create_enemy():
    if game_level < 5:
        global new_enemies
        new_enemies = enemies[0]

print("New enemies:", new_enemies)  # Output: skeleton