from board import Board

board = Board(5, 5)

print str(board)

MAX_TURNS = 4

for turn in range(1,MAX_TURNS+1): #loop for 4 guesses
	print turn
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))


	if board.is_a_hit(guess_row, guess_col):
		print "Congratulations! You sank my battleship!"
		break
	else:
		if turn==MAX_TURNS:
			print "*** Game Over ***"
		elif not board.is_in_ocean(guess_row, guess_col):
			print "Oops, that's not even in the ocean."
		elif board.was_already_guessed(guess_row, guess_col):
			print "You guessed that one already."
		else:
			board.record_guess(guess_row, guess_col)
			print "You missed my battleship!"
			print str(board)

