# Author: Chris Lee
# Various defintions for tic-tac-toe game.

# Exceptions for flow control and debugging
class BoardSizeInvalid(Exception):
    pass

class InvalidMove(Exception):
    pass

class ProgrammerError(Exception):
    pass

# function to draw game board
def draw_board(game):
    # buffer
    print('\n', end='')

    print('      ', end='')             # UI
    for i in range(game.size):
        print('C', end='')
        if i < (game.size - 1):
            print(' ', end='')
    print('\n', end='')

    print('      ', end='')             # UI
    for i in range(game.size):
        print('O', end='')
        if i < (game.size - 1):
            print(' ', end='')
    print('\n', end='')

    print('      ', end='')             # UI
    for i in range(game.size):
        print('L', end='')
        if i < (game.size - 1):
            print(' ', end='')
    print('\n', end='')

    print('\n', end='')

    # prints column labels
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    print('      ', end='')             # UI
    # constrained my gameboard size
    for i in range(game.size):
        print(f'{alphabet[i]}', end='')
        if i < (game.size - 1):
            print(' ', end='')
    print('\n\n', end='')

    for i in range(game.size):         # Row logic
        print(f'ROW {i + 1} ', end='')
        for j in range(game.size):     # Column logic
            print(game.gameboard[(i * game.size) + j], end='')
            if j != (game.size - 1):
                print('|', end='')
            else:
                print('\n', end='')     # "Explicit is better than implicit"


        if i != (game.size - 1):        
            print('      ', end='')
            for j in range(game.size):
                print('-', end='')
                if j != (game.size - 1):
                    print('+', end='')
                else:
                    print('\n', end='')