from cell import Cell
from random import randint

"""Disclaimer: Methods are in alphabetical order."""
class Board():
    # Certain parameters and properties are given.
    # TODO: Add the remaining parameters and properties.
    def __init__(self, CHAR_MINE="*", CHAR_BLANK="?"):
        self.CHAR_MINE = CHAR_MINE
        self.CHAR_BLANK = CHAR_BLANK

        # TODO: Add objects of cell to grid by creating a nested for loop (for loop in a for loop).
        #       The nested for loop is going to be crucial for a majority of the methods!
        self.grid = []
        
        # generate_mines() method already added.
        # TODO: Add the calculate_neighbouring mines method.
        #       This method will only calculate the mines for one cell.
        #       How are we going to run through all the cells in the entire grid?
        self.generate_mines(MINE_NUMBER)
    
    """ Calculates the number of mines adjacent to a cell """
    def calculate_neighbouring_mines(self, row, column):  
        # You can get a cell out of the grid as follows
        cell = self.grid[row][column]
        # TODO: We want to check the 8 tiles surrounding the cell.
        #       What relation is there between the current row and column number
        #       and the row and column number of neighbouring cells? Express this in a nested for loop!

        # Not all neighbouring cells are valid. Some might be outside of the grid:
        # TODO: Add conditions to only check a neighbour if it is inside the grid.
        #       Use continue to go to the next neighbour if the current neighbour is invalid.
        #       Below line gives the condition for the neighbour being too large (outside of grid).
        if (row+i >= self.SQUARE_SIZE) or (column+j >= self.SQUARE_SIZE):
            continue
        

    
    """  Clears all mines that are adjacent to a given until a cell containing a mine is encountered. """
    def cascade(self, row, column):
        # You will need to implement the simple cascade by yourself.


        # For the proper cascade function. As indicated by the README. There are 4 situations.
        # Each of these will need to be properly addressed.
        
        # Example:  If a row and column number point to a cell outside the grid, the method should
        #           immediately stop. If this was not done it would lead to an error when 
        #           using these to find a certain cell in the grid (IndexError).
        if(row < 0 or row >= self.SQUARE_SIZE or column < 0 or column >= self.SQUARE_SIZE):
            return
        cell = self.grid[row][column]

        # TODO: Think about when a certain situation occurs. Make this the condition for an if-statement.
        #       Inside the if-statement, write what needs to happen when the situation takes place. 
        #       Tip:    When recursion takes place, cascade() should be called 8 times.
        #               Once per (possible) neighbour the cell has.

    """ Places mines at random cell positions in the entire grid list """
    def generate_mines(self, MINE_NUMBER):
    # We will need to place a number of mines. A for-loop works great for this.
    # However, we only want to go to the next iteration of the for loop after 
    # confirming that a blank space has been changed to a mine. A while loop is needed.

    # TODO: Randomly generate a value for the row and column (within size of the grid).
    #       Check if the cell at these values is not alreade a mine. If not, go to the
    #       next iteration of the for loop.
        for _ in range(MINE_NUMBER):
            while ...

    """ Template for header of board states """
    def display_header(self, message):
        # We already centered a message in the finance app - exercise. Go check there.
        # TODO: The other part of the message consists of two rows. The length depends
        #       on the SQUARE_SIZE. Use two for-loops to create these rows.
        #       After completing each row. Add below code to go to the next row.
        header += f"\n"

    """ Show grid whilst playing the game """
    def display_play_grid(self):
        # Get the header from the display_header() method.
        header = self.display_header("LET'S PLAY")
        
        # TODO: Create the body by creating a nested for loop. It is best to use enumerate.
        #       This way you can directly obtain the value in the cell as well as the position of
        #       the cell in the grid. Think about what text should be added at which time.
        body = f""
        for index_i, row in enumerate(self.grid):
            for index_j, cell in enumerate(row):

        print(header + body)

    """ Show grid with locations of mines revealed """
    def display_mines_grid(self):
        # Use the same strategy as given in display_play_grid()

    """ Show grid with number of neighbouring mines revealed """
    def display_neighbouring_mines_grid(self):
        # Use the same strategy as given in display_play_grid()