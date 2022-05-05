from cell import Cell
from board import Board
from game import Game

""" 
You can use this file if you want to check certain properties/methods.
Objects for all classes have already been created
"""

cell = Cell()
board = Board()
game = Game()


# Example. Let's check if the display_mines_grid() method works.
board.display_mines_grid()
for i in range(board.SQUARE_SIZE):
    for j in range(board.SQUARE_SIZE):
        if board.grid[i][j].display_character == board.CHAR_MINE:
            print(f"Bomb located at row {i}, column {j}")