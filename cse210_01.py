# Assignment: CSE210 W01 Prove: Tic-Tac-Toe
# Author: Chris Lee

# REQS AND SUGS:
#   -One (1) if/then block
#   -One (1) while loop
#   -User friendly input validation
#   -Game over message
#   -Colors for players?

class BoardSizeInvalid(Exception):
    pass



def create_board(size):
    if size < 3 or size > 12:
        raise BoardSizeInvalid
    
    board = []

    for i in range(1, (size ** 2) + 1, 1):
        board.append(str(i))

    return board

def draw_board(size):
    print()

def main():
    return 0

if __name__ == '__main__':
    main()