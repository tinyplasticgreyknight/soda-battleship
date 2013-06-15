from random import randint

class Board:
	def __init__(self, width, height):
		self.grid = []
		for x in range(0, height):
			self.grid.append(["O"] * width)
		self.width  = width
		self.height = height
		self.ship_row = randint(0, height -1)
		self.ship_col = randint(0, width -1)
	def is_a_hit(self, row, col):
		if row == self.ship_row and row == self.ship_col:
			return True
		else:
			return False
	def is_in_ocean(self, row, col):
		if type(row) != int or type(col) != int:
			return False 
		if (0 <= row < self.height) and (0 <= col < self.width):
			return True
		else:
			return False			   
	def record_guess(self, row, col):
		self.grid[row][col] = "X"
	def was_already_guessed(self, row, col):
		if self.grid[row][col] == "X":
			return True
		else:
			return False
	def __str__(self):
		rowstrs = []
		for row in self.grid:
			rowstrs.append(" ".join(row))
		return "\n".join(rowstrs)
