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
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
elif board[int(guess_row)][int(guess_col)] == "X":
    print "You guessed that one already."
else:
    if guess_row < 0 or guess_row > BOARDH-1 or guess_col < 0 or guess_col > BOARDW-1:
        print "Oops, that's not even in the ocean."
    else:
        print "You missed my battleship!"
        board[int(guess_row)][int(guess_col)] = "X"
        print_board(board)
    
