from cell import Cell

class Board():
    def __init__(self, SQUARE_SIZE = 9):
        self.grid = []

        for i in range(SQUARE_SIZE):
            row = []
            for j in range(SQUARE_SIZE):
                row.append(Cell("?"))
            self.grid.append(row)


    """ Show grid whilst playing the game """
    def display_play_grid(self):
        """ Header of display grid message"""
        header = self.display_header("LET'S PLAY")
        
        """ Body of display grid message """
        body = f""
        for index, row in enumerate(self.grid):
            body += f"{index}|"
            for index, cell in enumerate(row):
                if cell.is_covered == True:
                    body += f"{self.CHAR_BLANK} "
                else:
                    body += f"{cell.neighbouring_mine_count} "
            body+=f"\n"
        print(header + body)

    """ Show grid with locations of mines revealed """
    def display_mines_grid(self):
        """ Header of display mines message"""
        header = self.display_header("Mine Placement")
        """ Body of display mines message """
        body = f""
        for index, row in enumerate(self.grid):
            body += f"{index}|"
            for index, cell in enumerate(row):
                body += f"{cell.display_character} "
            body+=f"\n"

        print(header + body)

    """ Show grid with number of neighbouring mines revealed """
    def display_neighbouring_mines_grid(self):
        """ Header of display neighbours message"""
        header = self.display_header("Neigbouring mines")
        """ Body of display neighbours message """
        body = f""
        for index, row in enumerate(self.grid):
            body += f"{index}|"
            for index, cell in enumerate(row):
                if cell.display_character==self.CHAR_MINE:
                    body += f"{self.CHAR_MINE} "
                else:
                    body += f"{cell.neighbouring_mine_count} "
            body+=f"\n"
        print(header+body)

