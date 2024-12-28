import os

# Add game board generation of different grid sizes later
game_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

BOARD_SIZE = len(game_board)
fill_tracker = []

def display_board():
    divider = (('-' * BOARD_SIZE + '|') * BOARD_SIZE) # for future make bigger tictactoe boards that have adaptable code
    divider_len = len(divider)
    
    print()

    for i, row in enumerate(game_board):
        print('|'.join(f'{cell:^3}' for cell in row))
        if i < BOARD_SIZE - 1:
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
    for i in range(BOARD_SIZE):
        if game_board[i] == ['O'] * BOARD_SIZE or game_board[i] == ['X'] * BOARD_SIZE:
            return True
    return False



def check_cols():
    for col in range(BOARD_SIZE):
        num_lst = [game_board[row][col] for row in range(BOARD_SIZE)]
        if num_lst == ['O'] * BOARD_SIZE or num_lst == ['X'] * BOARD_SIZE:
            return True
    return False

def check_diag():
    l_diag = [game_board[i][i] for i in range(BOARD_SIZE)]
    u_diag = [game_board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]

    if (l_diag == ['O'] * BOARD_SIZE or u_diag == ['O'] * BOARD_SIZE) or (l_diag == ['X'] * BOARD_SIZE or u_diag == ['X'] * BOARD_SIZE):
        return True
    else:
        return False

def start_over():
    option = input("\nWould you like to start a new game (y/n/yes/no)?: ")
    user_input = option.lower()
    while user_input not in ['yes', 'no', 'y', 'n']:
        option = input("\nThe option entered is invalid (y/n/yes/no): ")
        user_input = option.lower()
        
    if user_input == 'y' or user_input == 'yes':
        global game_board
        game_board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ] 
        fill_tracker.clear()
        return True
    else:
        return False

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    p1 = True

    display_board()

    while True:
        try:
            num = int(input(f"Enter a number from 1-9 player {'X' if p1 else 'O'}: "))

            if num < 1 or num > 9:
                print("\nOut of range, enter a number within 1-9\n")
            elif check_fill_override(num):
                print("\nThe cell has already been filled, select another one\n")
            else:
                if p1:
                    replace_num(num, 'X')
                    p1 = False
                else:
                    replace_num(num, 'O')
                    p1 = True
                
                display_board()

            if check_rows() or check_cols() or check_diag():
                clear_terminal()
                display_board()
                print("Player O wins!") if p1 else print("Player X wins!")
                
                if start_over():
                    game()
                else:
                    break
            elif BOARD_SIZE ** 2 == len(fill_tracker):
                print("Game Over!\n")

                if start_over():
                    game()
                else:
                    break
        except ValueError:
            print("\nInvalid entry, integers only")

game()

