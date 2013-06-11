from random import randint

class Board:
    def __init__(self, width, height):
        self.grid = []
        for x in range(0, height):
            self.grid.append(["O"] * width)
        self.width  = width
        self.height = height
    def is_a_hit(self, row, col):
        pass
    def is_in_ocean(self, row, col):
        pass
    def was_already_guessed(self, row, col):
        pass
    def to_string(self):
        pass
