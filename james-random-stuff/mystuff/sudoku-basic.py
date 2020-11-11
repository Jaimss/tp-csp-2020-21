board = [
        [0, 0, 2, 7, 8, 0, 0, 0, 9],
        [7, 6, 0, 0, 0, 5, 0, 0, 3],
        [4, 0, 3, 6, 0, 0, 0, 0, 0],
        [9, 1, 0, 0, 2, 4, 0, 8, 0],
        [0, 0, 4, 1, 0, 7, 9, 0, 0],
        [0, 2, 0, 9, 3, 0, 0, 7, 4],
        [0, 0, 0, 0, 0, 1, 7, 0, 5],
        [5, 0, 0, 3, 0, 0, 0, 9, 8],
        [2, 0, 0, 0, 5, 9, 4, 0, 0],
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check the 3x3 cube/box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    '''print a board to the screen that is a bit nicer looking'''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('-' * 21)

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            print(str(bo[i][j]), end=' ' if j != 8 else '\n')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


if solve(board):
    print_board(board)
