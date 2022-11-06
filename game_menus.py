# Author: Chris Lee
# Assignment: CSE210_01
#
# Definitions for menus
import game_logic
import splash

# menu logic for game setup
def setup_menu():
    while True:
        print('Excellent!')
        print('Gameboards of 3x3 to 9x9 are available.')
        print('For each player, an uppercase letter may be chosen as the player\'s symbol.')

        # loops for valid input
        while True:
            print('Please select a nXn game board size:')
            choices = ['3', '4', '5', '6', '7', '8', '9']
            user_input = input('n=')
            # checks input against valid sizes
            if user_input in choices:
                # if valid creates a game object
                game = game_logic.GameBoard(size=int(user_input))
                # leaves loop with valid input
                break
            else:
                print('Ooops! Remember the board size must be between 3x3 and 9x9.')
                print('Please select a number from 3 to 9.')
        
        # loops for valid input
        while True:
            print('Please select a symbol for player 1.')
            print('You may select any uppercase letter, but each player must have a different symbol.')
            print('Press enter without making a selection for the default.')
            choices = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            user_input = input('Player 1 symbol: ')

            # checks for default selection
            if user_input == '':
                game.player1 = 'X'
                break # leave loop with valid input
            # validates input and modifies game object
            elif user_input in choices:
                game.player1 = user_input
                break # leave loop with valid input
            else:
                print('Ooops! The symbol for player 1 must be an uppercase letter.')
                print('Please select an uppercase letter or leave blank for the default.')
                
        # loops for valid input
        while True:
            print('Please select a symbol for player 2.')
            print('You may select any uppercase letter, but each player must have a different symbol.')
            print('Press enter without making a selection for the default.')
            choices = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            user_input = input('Player 2 symbol: ')

            # checks for default selections
            if user_input == '' and game.player1 != 'O':
                game.player2 = 'O'
                break # leave loop with valid input
            elif user_input == '' and game.player1 == 'O':
                game.player2 = 'X'
                break # leave loop with valid input

            # validates input and modifies game object
            elif user_input in choices and user_input != game.player1:
                game.player2 = user_input
                break # leave loop with valid input

            elif user_input in choices and user_input == game.player1:
                print('Ooops! The symbol for player 2 must be different than the symbol for player 1.')
            else:
                print('Ooops! The symbol for player 1 must be an uppercase letter.')
                print('Please select an uppercase letter or leave blank for the default.')

        # loops for valid input
        while True:        
            # confirmation screen
            print(f'Congratulations! You have selected a board size of {game.size}X{game.size}, player 1\'s symbol as ', game.player1, ', and player 2\'s symbol as ', game.player2, '.', sep='')
            print('Size: ', game.size, 'X', game.size, '\nPlayer 1: ', game.player1, '\nPLayer 2: ', game.player2, sep='')
            print('Please make a selection:')
            print('1: Play!')
            print('2: Return to main menu.')
            print('3: Reset game options.')
            choices = ['1', '2', '3']
            user_input = input()

            # validates input
            if user_input in choices:
                match int(user_input):
                    case 1:
                        return game # returns game object for menu logic to launch
                    case 2:
                        return 0 # returns 0 to indicate player choice
                    case 3:
                        break # returns to loop beginning to reset game setup
            else:
                print('Please select a valid option.')

# main menu logic
def main_menu():
    # loops for valid input
    while True:
        print('Welcome to Tic-Tac-Toe! Please make a selection:')
        print('1: Play game')
        print('2: Quit')
        print('3: Credits')
        choices = ['1','2','3']

        user_input = input()

        # returns to loop beginning on invalid input
        if user_input not in choices:
            continue

        # selects user selection
        user_input = int(user_input)
        match user_input:
            case 1:
                # launches game setup menu
                game = setup_menu()
                # checks if user selected a game or menu return
                if game:
                    # if game object is present, the object is passed to menu logic to be launched
                    return game
            case 2:
                # returns 0 to indicate no game object and selection to exit
                return 0
            case 3:
                # display credit
                splash.splash_credits()