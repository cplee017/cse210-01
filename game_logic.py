# Author: Chris Lee
# Assignment: CSE 210_01
#
# Definitions related to game logic

import cse210_01_funcs as tic

# defintion of game object
class GameBoard:
    """Class for game board object"""

    # setup
    def __init__(self, size):
        self.size = size
        self.create_board(size)
        self.winner = 0
        self.player1 = ''
        self.player2 = ''
        self.moves = size ** 2
    
    #function to create initial game board
    def create_board(self, size):
        if size < 3 or size > 9:
            raise tic.BoardSizeInvalid
    
        self.gameboard = []

        for i in range(1, (size ** 2) + 1, 1):
            self.gameboard.append(' ')

        return
    
    # method for handling player moves
    def move(self, player, row, column):
        # row, column expected as 0 indexed ints
        # error handling
        if player != 'player1' and player != 'player2':
            raise tic.ProgrammerError(f'invalid player arg for GameBoard.move() -- Received {player}')
        if row >= self.size or column >= self.size:
            raise tic.ProgrammerError(f'invalid row/column arg for GameBoard.move() -- Received R: {row}, C: {column}')
        
        # move logic
        move_array_index = (row * self.size) + column # calculation of vector index from row,column values
        # checks validity of move
        # move is valid if and only if array value is not yet equal to a player symbol
        if self.gameboard[move_array_index] == self.player1 or self.gameboard[move_array_index] == self.player2:
            raise tic.InvalidMove
        # with valid move updates game array
        else:
            if player == 'player1':
                self.gameboard[move_array_index] = self.player1
            else:
                self.gameboard[move_array_index] = self.player2
            # decrements available moves
            self.moves = self.moves - 1
        
        # Check win conditions
        symbol_count = 0
        # Check horizontals
        for i in range(self.size):
            if self.gameboard[(row * self.size) + i] == self.gameboard[move_array_index]:
                symbol_count += 1
        if symbol_count == self.size:
            self.winner = int(player[6]) # This is admittedly atrocious but I don't have time to refactor
            return
        else:
            symbol_count = 0
        # Check verticals
        for i in range(self.size):
            if self.gameboard[(i * self.size) + column] == self.gameboard[move_array_index]:
                symbol_count += 1
        if symbol_count == self.size:
            self.winner = int(player[6])
            return
        else:
            symbol_count = 0
        # Check diags
        if (move_array_index - (row * self.size) - row) == 0: # Checks if current move lies on top-left -> bottom-right
            for i in range(self.size):
                if self.gameboard[i + (self.size * i)] == self.gameboard[move_array_index]:
                    symbol_count += 1
            if symbol_count == self.size:
                self.winner = int(player[6])
                return
            else:
                symbol_count = 0
        if (move_array_index - ((row + 1) * (self.size - 1))) == 0: # Checks if current move lies on top-right -> bottom-left
            for i in range(self.size):
                if self.gameboard[(self.size - 1) * (i + 1)] == self.gameboard[move_array_index]:
                    symbol_count += 1
            if symbol_count == self.size:
                self.winner = int(player[6])
                return
            else:
                symbol_count = 0
        # Check draw
        if self.moves == 0:
            self.winner = 3
            return
        
        return

# game logic loop
def game_loop(game):
    # Setup
    choices_r = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    choices_c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    row_choices = choices_r[0:game.size]
    column_choices = choices_c[0:game.size]

    # player welcome
    print('Have fun!\n')
    tic.draw_board(game)
    print('\nEach player takes a turn, starting with player 1.')
    print('When it is your turn, select a square to place your mark by entering the appropriate ROW number and COLUMN letter.')
    print('Quit at anytime by entering "quit"')
    print('Good luck!')

    # loop while no one has won and there are valid moves
    while game.winner == 0:
        # Player 1 turn
        while True:
            print('Player 1, please select a square')
            move_row = input('Row number: ')
            move_column = input('Column letter: ')
            # validates input
            if move_row in row_choices and move_column in column_choices:
                # checks move validity
                try:
                    game.move(player='player1', row=row_choices.index(move_row), column=column_choices.index(move_column))
                    break # valid move leaves player turn loop
                # handles invalid move
                except tic.InvalidMove:
                    print('Square already taken. Please try again.')
            # quit logic
            elif move_row == 'quit' or move_column == 'quit':
                return
            else:
                print('Please select a valid square.')
        # leave player 1 turn loop
        tic.draw_board(game)
        # checks for winner
        if game.winner != 0:
            break # leaves game loop if winner
        # Player 2 turn
        while True:
            print('Player 2, please select a square')
            move_row = input('Row number: ')
            move_column = input('Column letter: ')
            # validates input
            if move_row in row_choices and move_column in column_choices:
                # checks move validity
                try:
                    game.move(player='player2', row=row_choices.index(move_row), column=column_choices.index(move_column))
                    break # valid move leaves turn loop
                # handles invalid moves
                except tic.InvalidMove:
                    print('Square already taken. Please try again.')
            # quit logic
            elif move_row == 'quit' or move_column == 'quit':
                return
            else:
                print('Please select a valid square.')
        # leave player2 loop
        tic.draw_board(game)
        # check for winner
        if game.winner != 0:
            break # leaves game loop if winner
        

    # End
    match game.winner:
        case 1:
            print('Congratulations player 1!')
        case 2:
            print('Congratulations player 2!')
        case 3:
            print('It\'s a draw!')
            print('Better luck next time!')
    return