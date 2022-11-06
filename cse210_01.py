# Assignment: CSE210 W01 Prove: Tic-Tac-Toe
# Author: Chris Lee
#
# main declaration

import game_logic
import game_menus
import splash

# infinite loop to control menu flow
def menu_loop():
    while True:
        # calls main menu to get player choice
        game = game_menus.main_menu()
        # game_menus.main_menu() return a game object if the user wants to play
        # returns 0 if the user has selected to quit
        if game:
            # when a game object is present calls the game logic
            game_logic.game_loop(game)
        else:
            return

# main entry point
# logic occurs in menu_loop()
def main():
    
    splash.draw_splash()

    menu_loop()

    splash.draw_exit_splash()

    return 0

# boilerplate
if __name__ == '__main__':
    main()
