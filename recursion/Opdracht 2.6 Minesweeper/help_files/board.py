from tracemalloc import start
from cell import Cell
<<<<<<< HEAD
import random

class Board():
    def __init__(self, SQUARE_SIZE = 9, CHAR_MINE = '*', CHAR_BLANK = '?', MINE_NUM = 9):
        self.CHAR_MINE = '*'
        self.CHAR_BLANK = '?'
        self.SQUARE_SIZE = 9
        self.FULL_SIZE = self.SQUARE_SIZE **2
        self.MINE_NUM = 9
        self.covered_cells = (self.FULL_SIZE) - self.MINE_NUM
        self.grid = [['?','?', '?', '?', '?', '?', '?', '?', '?'], 
        ['?','?', '?', '?', '?', '?', '?', '?', '?'], 
        ['?','?', '?', '?', '?', '?', '?', '?', '?'], 
        ['?','?', '?', '?', '?', '?', '?', '?', '?'], 
        ['?','?', '?', '?', '?', '?', '?', '?', '?'],
        ['?','?', '?', '?', '?', '?', '?', '?', '?'],
        ['?','?', '?', '?', '?', '?', '?', '?', '?'],
        ['?','?', '?', '?', '?', '?', '?', '?', '?'], 
        ['?','?', '?', '?', '?', '?', '?', '?', '?']]

    def generate_mines(self):
        for i in range(self.MINE_NUM):
            r_row = random.randint(0, 8)
            r_col = random.randint(0,8)
            self.grid[r_row][r_col] = self.CHAR_MINE

    def calculate_neighbouring_mines(self, x, y):
        neighbours = []
        mine_count = 0

        x_max = x + 1 if x + 1 < self.SQUARE_SIZE else x
        x_min = x - 1 if x - 1 >= 0 else x
        y_max = y + 1 if y + 1 < self.SQUARE_SIZE else y
        y_min = y - 1 if y - 1 >= 0 else y

        for i in range(x_min, x_max):
            for j in range(y_min, y_max):
                for index, row in enumerate(self.grid):
                    for index, cell in enumerate(self.grid):
                        if self.grid[i][j] == '*':
                            mine_count += 1
        self.grid[x][y] = mine_count
        return self.grid
                    
    def display_header(self, message):
        header = message.center(2*(self.SQUARE_SIZE+2), "*")
        print(header)
        print(f'   0', end=' ')
        for number in range(1, self.SQUARE_SIZE):
            if number == self.SQUARE_SIZE - 1:
                print(f'{number}')
            else:
                print(f'{number}', end=' ')
        print('   -', end='')
        for number in range(0,(2*self.SQUARE_SIZE+2)):
            print('-', end='')

        return ''


        
bord=Board()
print(bord.display_header("LET'S PLAY"))



=======
from random import randint

class Board():
    """ constructor for objects of Board """
    def __init__(self, CHAR_MINE="*", CHAR_BLANK="?", SQUARE_SIZE=9, MINE_NUMBER=9):
        self.CHAR_MINE = CHAR_MINE
        self.CHAR_BLANK = CHAR_BLANK
        self.SQUARE_SIZE = SQUARE_SIZE
        self.covered_cells = SQUARE_SIZE**2-MINE_NUMBER
        # Short method for grid
        self.grid = [[Cell(CHAR_BLANK) for _ in range(SQUARE_SIZE)] 
                    for _ in range(SQUARE_SIZE)]
        
        self.generate_mines(MINE_NUMBER)

        for row in range(SQUARE_SIZE):
            for column in range(SQUARE_SIZE):
                self.calculate_neighbouring_mines(row, column)
    
    """ Calculates the number of mines adjacent to a cell """
    def calculate_neighbouring_mines(self, row, column):  
        cell = self.grid[row][column]
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (row+i < 0) or (column+j < 0):
                    continue
                if (row+i >= self.SQUARE_SIZE) or (column+j >= self.SQUARE_SIZE):
                    continue
                other_cell = self.grid[row+i][column+j]
                if other_cell.display_character == self.CHAR_MINE:
                    cell.neighbouring_mine_count+=1
    
    """  Clears all cells that are adjacent to a given cell until a cell neighbouring a mine is encountered. """
    def cascade(self, row, column):
        pass

    """ Places mines at random cell positions in the entire grid list """
    def generate_mines(self, MINE_NUMBER):
        for _ in range(MINE_NUMBER):
            mine_placed = False
            while mine_placed == False:
                rand_row = randint(0,self.SQUARE_SIZE-1)
                rand_col = randint(0,self.SQUARE_SIZE-1)
                rand_cell = self.grid[rand_row][rand_col]
                if rand_cell.display_character == self.CHAR_BLANK:
                    rand_cell.display_character = self.CHAR_MINE
                    mine_placed = True

    """ Template for header of board states """
    def display_header(self, message):
        """ Header of display mines message """
        header = f"{message.center(self.SQUARE_SIZE*2+2,'%')}\n  "
        for index in range(self.SQUARE_SIZE):
            header += f"{index} "
        header += f"\n  "
        for index in range(self.SQUARE_SIZE):
            header += f"--"
        header += f"\n"
        return header

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