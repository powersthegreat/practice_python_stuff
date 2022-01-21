import random

def board_generator():
    row_1 = []
    row_2 = []
    row_3 = []
    rows = [row_1, row_2, row_3]

    for i in range(0,3):
        random_int_1 = random.randint(0,0)
        row_1.append(random_int_1)
        random_int_2 = random.randint(0,0)
        row_2.append(random_int_2)
        random_int_3 = random.randint(0,0)
        row_3.append(random_int_3)

    return rows

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

def split_input(user_input):
    user_input_split = user_input.split(",")
    split_1 = int(user_input_split[0])
    split_2 = int(user_input_split[1])
    return split_1, split_2

def tictactoe_logic(board):
    while row_checker(board) == True:
        user_1 = input("Player 1 enter coordinates for your move in form 'X,Y'\n")
        user_1_return = split_input(user_1)
        int_user_1_x = user_1_return[0]
        int_user_1_y = user_1_return[1]
        board[-int_user_1_y][-int_user_1_x] = 1
        
        for row in range(0,3):
            print(board[row])

        user_2 = input("Player 2 enter coordinates for your move in form 'X,Y'\n")
        user_2_return = split_input(user_2)
        int_user_2_x = user_2_return[0]
        int_user_2_y = user_2_return[1]
        board[-int_user_2_y][-int_user_2_x] = 2
        
        for row in range(0,3):
            print(board[row])

intro_input = input("Would you like to play tic tac toe? Enter 'yes' or 'no'.\n")

while intro_input == "yes":
    board = board_generator()
    tictactoe_logic(board)
    intro_input = input("Would you like to play again? Enter 'yes' or 'no'.\n")