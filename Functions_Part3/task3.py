# I used ChatGPT for this one you should know

def is_valid_move(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1


def print_board(board):
    for row in board:
        print(' '.join(str(col).rjust(2, '0') for col in row))
    print()


def solve_knight_tour(board, curr_x, curr_y, move_x, move_y, pos):
    if pos == len(board) * len(board[0]):
        return True

    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = pos
            if solve_knight_tour(board, next_x, next_y, move_x, move_y, pos + 1):
                return True
            board[next_x][next_y] = -1  # Backtracking
    return False


def knight_tour(n, start_x, start_y):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[start_x][start_y] = 0

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    if solve_knight_tour(board, start_x, start_y, move_x, move_y, 1):
        print_board(board)
    else:
        print("Solution does not exist")


# Example usage:
n = 6  # 6x6 board

# Starting position
start_x = int(input('Enter X coordinate: '))
start_y = int(input('Enter Y coordinate: '))

knight_tour(n, start_x, start_y)

