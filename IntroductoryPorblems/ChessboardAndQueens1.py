def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def count_queen_placements(board, col):
    if col == len(board):
        return 1
    count = 0
    for i in range(len(board)):
        if board[i][col] == '.' and is_safe(board, i, col):
            board[i][col] = 'Q'
            count += count_queen_placements(board, col + 1)
            board[i][col] = '.'

    return count

def total_queen_placements(board):
    return count_queen_placements(board, 0)

board = [list(input()) for _ in range(8)]
print(total_queen_placements(board))
