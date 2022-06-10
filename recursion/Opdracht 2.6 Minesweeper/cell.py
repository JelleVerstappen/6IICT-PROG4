class Cell():
    def __init__(self, display_character):
        self.is_covered = True
        self.display_character = display_character
        self.neighbouring_mines = 0

