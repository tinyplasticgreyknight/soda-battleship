from random import randint

board = []

BOARDW, BOARDH = (5, 5)

for x in range(0, BOARDH):
	board.append(["O"] * BOARDW)

def print_board(board):
	for row in board:
		print " ".join(row)

print_board(board)

def random_row(board):
	return randint(0, BOARDH - 1)

def random_col(board):
	return randint(0, BOARDW - 1)

ship_row = random_row(board)
ship_col = random_col(board)

MAX_TURNS = 4

for turn in range(1,MAX_TURNS+1): #loop for 4 guesses
	print turn
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))


	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sank my battleship!"
	else:
		if turn==MAX_TURNS:
			print "*** Game Over ***"
		elif not ((0 <= guess_row < BOARDH) and (0 <= guess_col < BOARDW)):
			print "Oops, that's not even in the ocean."
		elif board[guess_row][guess_col] == "X":
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
			print_board(board)

