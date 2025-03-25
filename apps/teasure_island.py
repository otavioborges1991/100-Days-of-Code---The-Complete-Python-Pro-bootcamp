
def main():
    print("Wellcome to the Treasure Island.\n"
    "Your mission is to find treasure.\n"
    "You're at a cross road. Where do you want to go?")
    direction = input('Type [Left] or [Right]: ').lower().strip()
    if direction == "left":
        print("You've coma to a lake.\n"
              "There is an island in the middle of the lake.\n")
        direction = input("[Wait] for a boat or [Swim] across the lake: ").lower().strip()
        if direction == "wait":
            print("You arrive at the island unharmed.\n"
             "There is a house with 3 doors.\n"
             "One red, one yellow and one blue; which colour do you choose?\n")
            direction = input("[Red] [Yellow] [Blue]: ").lower().strip()
            if direction == "yellow":
                print("""treasure chest:
                             __________
                            /\____;;___\
                           | /         /
                           `. ())oo() .
                            |\(%()*^^()^\
                           %| |-%-------|
                          % \ | %  ))   |
                          %  \|%________|
      """)
                print('Congratulations! you found the treasure.')
            elif direction == 'red':
                print('You have entered a room in fire.')
                exit('GAME OVER')
            else:
                print('You have entered a room with giants beats.')
                exit('GAME OVER')

        else:
            print('While you swim, a giant cat fish swallows you whole.')
            exit('GAME OVER')
    else:
        print("You arrive at a forest and fall into a hole in the ground.")
        exit('GAME OVER')





if __name__ == "__main__":
    main()
