enemies = 1

def increase_enemies():
    global enemies
    enemies += 1

def local_scope_example():
    enemies = 5  # This is a local variable, it won't affect the global 'enemies'
    print("Local enemies:", enemies)  # Output: 5
    # The global 'enemies' variable is not modified here

print("Initial enemies:", enemies)  # Output: 1
increase_enemies()
print("Enemies after increase:", enemies)  # Output: 2
local_scope_example()  # This will print the local 'enemies' variable
print("Enemies after local scope example:", enemies)  # Output: 2

def game():
    enemies = 2  # This is a local variable for the 'game' function
    print("Enemies in game:", enemies)  # Output: 2
    # The global 'enemies' variable is not modified here
    def level(): # This is a nested function
        nonlocal enemies # This allows us to modify the 'enemies' variable from the enclosing scope
        enemies += 1
        print("Enemies in level:", enemies)  # Output: 3
    

    level()  # Call the nested function to modify 'enemies'
    print("Enemies after level:", enemies)  # Output: 3
