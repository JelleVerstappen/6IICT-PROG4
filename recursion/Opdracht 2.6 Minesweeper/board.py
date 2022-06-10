from tracemalloc import start
from cell import Cell
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



