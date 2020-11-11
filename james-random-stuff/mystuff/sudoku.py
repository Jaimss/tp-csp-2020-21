import os
import pygame
import time

os.environ['SDL_AUDIODRIVER'] = 'dsp'

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

pygame.init()
size = width, height = 900, 900

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Sudoku Solver')


def update_board_slot(pos, value, color=black):
    y, x = pos
    slot = bo_y, bo_x = y * (height / 9) - 60, x * (width / 9) - 60

    font = pygame.font.Font(None, 50)
    text = font.render(str(value), 1, color)

    screen.blit(text, slot)

    pygame.display.update()


def open_game(bo):
    screen.fill(white)
    pygame.display.update()

    for i in range(1, 9):
        pygame.draw.line(screen, black, (width / 9 * i, 0), (width / 9 * i, height), 7 if i % 3 != 0 else 10)

    for i in range(1, 9):
        pygame.draw.line(screen, black, (0, height / 9 * i), (width, height / 9 * i), 7 if i % 3 != 0 else 10)

    pygame.display.update()

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] != 0:
                update_board_slot((i, j), bo[i][j], (0, 150, 190))


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        y, x = find

    time.sleep(.5)

    # fill in a random number
    for i in range(1, 10):
        if valid(bo, (y, x), i):
            bo[y][x] = i
            update_board_slot((x + 1, y + 1), i, (255, 0, 0))

            if solve(bo):
                return True

            bo[y][x] = 0
            update_board_slot((x + 1, y + 1), ' ')

    return False


def valid(bo, pos, num):
    y, x = pos
    if num == 0:
        raise ValueError

    # check the row for the same number
    for i in range(len(bo[0])):
        if bo[y][i] == num and x != i:
            return False

    # check the column for the same number
    for i in range(len(bo)):
        if bo[i][x] == num and y != i:
            return False

    # check the box for the same number
    box_x = x // 3
    box_y = y // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # y, x

    return None  # no space found


def print_board(bo):
    """print the board"""
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('---------------------')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(f'{bo[i][j]} ' if bo[i][j] != 0 else '  ')
            else:
                print(f'{bo[i][j]} ' if bo[i][j] != 0 else '  ', end='')


open_game(board)
solve(board)
