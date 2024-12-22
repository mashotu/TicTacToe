game_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board_size = len(game_board)
fill_tracker = []

def display_board():
    divider = (('-' * board_size + '|') * board_size) # for future make bigger tictactoe boards that have adaptable code
    divider_len = len(divider)
    
    print()

    for i, row in enumerate(game_board):
        print('|'.join(f'{cell:^3}' for cell in row))
        if i < board_size - 1:
            print(divider[:divider_len - 1])
    
    print()

def check_fill_override(num):
    for i in range(len(fill_tracker)):
        if fill_tracker[i] == num:
            return True
    return False

def replace_num(num, replacement):
    for i, row in enumerate(game_board):
        for j, cell in enumerate(row):
            if num == cell:
                fill_tracker.append(num)
                game_board[i][j] = replacement
                break

def check_rows():
    for i in range(board_size):
        if game_board[i] == (['O'] * board_size) or game_board[i] == (['X'] * board_size):
            return True
        else: 
           return False


def check_cols():
    for col in range(board_size):
        num_lst = [game_board[row][col] for row in range(board_size)]
        if num_lst == ['O'] * board_size or num_lst == ['X'] * board_size:
            return True
    return False

def check_diag():
    l_diag = [game_board[i][i] for i in range(board_size)]
    u_diag = [game_board[i][board_size - 1 - i] for i in range(board_size)]

    if (l_diag == ['O'] * board_size or u_diag == ['O'] * board_size) or (l_diag == ['X'] * board_size or u_diag == ['X'] * board_size):
        return True
    else:
        return False

def game():
    p1 = True

    display_board()

    while True:
        try:
            num = int(input(f"Enter a number from 1-9 player {'X' if p1 else 'O'}: "))

            if num < 1 or num > 9 or check_fill_override(num):
                print("\nOut of range, enter a number within 1-9 or number already filled/can't override\n")
            else:
                if p1:
                    replace_num(num, 'X')
                    p1 = False
                else:
                    replace_num(num, 'O')
                    p1 = True
                
                display_board()

            if check_rows() or check_cols() or check_diag():
                print('Player O wins!') if p1 else print('Player X wins!')
                display_board()
                break
        except ValueError:
            print("\nInvalid entry, integers only")

game()
