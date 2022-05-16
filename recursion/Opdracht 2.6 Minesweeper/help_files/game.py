from board import Board

"Disclaimer: Methods are in alphabetical order."
class Game():
    # TODO: Add the correct parameters to the init() method.
    def __init__():
        # Properties of game object are set.
        self.board = Board(CHAR_MINE, CHAR_BLANK, SQUARE_SIZE, MINE_NUMBER)

    "Game loop of Minesweeper (already completed) "
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

    " Get the choice of the user "
    def get_user_choice(self):
        # Use while True loop to run code until a valid input is given.
        # If input is not valid, continue to next iteration of while.
        # If input is valid use return to exit method.
        # TODO: Add input user and other conditions.
        while True:

                # Input numbers too large. 
                if (row>=self.board.SQUARE_SIZE) or (col>=self.board.SQUARE_SIZE):
                    print(f"{user_input} is invalid, try again")
                    continue
                elif ...
                return row,col


    " Make a move on the board "
    def make_move(self):
        # Get input from user using the below line.
        row, col = self.get_user_choice()
        # TODO: Add code to check if player is dead, uncover certain cells 
        #       and if player has won the game.

"""
This will be executed when running the game.py file

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