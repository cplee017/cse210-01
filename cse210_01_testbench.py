# Assignment: CSE210 W01 Prove: Tic-Tac-Toe
# Author: Chris Lee

import cse210_01 as project


def test_suite():
    test_create_board()
    test_draw_board()

def test_draw_board():
    for i in range(3,10):
        testBoard = project.GameBoard(size=i)
        project.tic.draw_board(testBoard)

def test_create_board():
    for i in range(10):
        try:
            print(f'Test {i}:', project.create_board(i))
        except project.BoardSizeInvalid:
            print(f'Test {i}: Invalid Board Size caught')
    return 0

def main():
    test_suite()

if __name__ == "__main__":
    main()