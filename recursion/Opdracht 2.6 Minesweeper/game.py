from board import Board

class Game():
    def __init__(self, CHAR_MINE="*", CHAR_BLANK="?", SQUARE_SIZE=9, MINE_NUMBER=9):
        self.board = Board(CHAR_MINE, CHAR_BLANK, SQUARE_SIZE, MINE_NUMBER)

    """ Get the choice of the user """
    def get_user_choice(self):
        pass

    """ Make a move on the board """
    def make_move(self):
        row, col = self.get_user_choice()
        if self.board.grid[row][col].display_character == self.board.CHAR_MINE:
            return False
        self.board.cascade(row,col)
        if self.board.covered_cells <= 0:
            return True

    """Game loop of Minesweeper """
    def game_loop(self):
        self.board.display_mines_grid()
        self.board.display_neighbouring_mines_grid()

        game_end = None
        while True:
            self.board.display_play_grid()
            game_end = self.make_move()
            if game_end == True:
                print(f"Congrats you won!")
                break
            if game_end == False:
                print(f"Bomb exploded!!!!")
                self.board.display_mines_grid()
                break

"""
Game settings, to be passed on to Board through Game.
    CHAR_MINE: Character to be used when displaying mines (default *)
    CHAR_BLANK: Character to be used when displaying blanks (default ?)
    SQUARE_SIZE: The width and height of the minesweeper square (default 9)
    MINE_NUMBER: THe amount of mines in the square (default 9)
"""
if __name__ == "__main__":
    game = Game(CHAR_MINE = "µ", SQUARE_SIZE=7, MINE_NUMBER=40) # CHAR_MINE = "µ", SQUARE_SIZE=7, MINE_NUMBER=40
    game.game_loop()