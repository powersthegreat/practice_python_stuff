import random

def row_checker(board):
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        print("player one you have won")
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        print("player one you have won")
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        print("player one you have won")
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        print("player one you have won")
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        print("player one you have won")
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        print("player one you have won")
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        print("player one you have won")
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        print("player one you have won")

    elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        print("player one you have won")
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        print("player one you have won")
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        print("player one you have won")
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        print("player one you have won")
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        print("player one you have won")
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        print("player one you have won")
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        print("player one you have won")
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        print("player one you have won")
    else:
        return True


winner_is_2 = [
    [2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]
]

def board_generator():
    row_1 = []
    row_2 = []
    row_3 = []
    rows = [row_1, row_2, row_3]

    for i in range(0,3):
        random_int_1 = random.randint(0,2)
        row_1.append(random_int_1)
        random_int_2 = random.randint(0,2)
        row_2.append(random_int_2)
        random_int_3 = random.randint(0,2)
        row_3.append(random_int_3)

    return rows

board = board_generator()

for row in range(0,3):
    print(board[row])


row_checker(board)
