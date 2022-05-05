from board import Board

class Game():

    """ Game loop of Minesweeper (already completed) """
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
                self.board.display_mines()
                break

"""
Game settings, to be passed on to Board through Game.
    CHAR_MINE: Character to be used when displaying mines (default *)
    CHAR_BLANK: Character to be used when displaying blanks (default ?)
    SQUARE_SIZE: The width and height of the minesweeper square (default 9)
    MINE_NUMBER: THe amount of mines in the square (default 9)

When leaving Game() empty, the default values listed above should be used.
"""
if __name__ == "__main__":
    game = Game()
    game.game_loop()