from renderer import Renderer
from input import InputHandler
import tetris
import time, random, copy

matrix_1 = [
    list(range(0, 8)), # Top Buttons
    list(range(8, 16)),
    list(range(16, 24)),
    list(range(24, 32)),
    list(range(32, 40)),
    list(range(40, 48)),
    list(range(48, 56)),
    list(range(56, 64)),
    list(range(64, 72)), # Bottom Buttons
    list(range(72, 80)), # Side Buttons
]

renderer = Renderer()
input_handler = InputHandler()
board = tetris.Board(8, 8)

current_piece = [[0]]
current_color = 0

def choose_piece():
    global current_piece, current_color
    # i = (i + 1) % 7
    i = random.randint(0, 6)
    current_piece = copy.deepcopy(tetris.pieces[i])
    current_color = copy.deepcopy(tetris.colors[i])


tick = 0

x = 0
y = 0
c = 0
speed = 1

def gen_matrix():
    matrix = copy.deepcopy(board.matrix)
    # for i in range(10):
    #     matrix += [[0] * 8]
    for iy in range(len(current_piece)):
        for ix in range(0, len(current_piece[0])):
            if current_piece[iy][ix] == 1:
                _y = y - iy
                _x = x + ix
                if _y >= len(matrix) or _y < 0 or _x < 0 or _x >= len(matrix[_y]):
                    continue
                else:
                # print(_y, _x, len(matrix), len(matrix[_y]))
                    matrix[_y][_x] = current_color
    return matrix


choose_piece()
while not board.finished():
    # print(board.finished())
    time.sleep(1/15)
    tick += 1
    renderer.render(gen_matrix(), speed)
    command = input_handler.poll()
    board.clearRows()
    if tick % (15- speed) == 0:
        y += 1
        print(y)
        if board.collides(current_piece, x, y):
            board.place(current_piece, x, y-1, current_color)
            choose_piece()
            x = 0
            y = 0
    if command:
        if command == "LEFT":
            if not board.collides(current_piece, x-1, y):
                x = x - 1
        elif command == "RIGHT":
            if not board.collides(current_piece, x+1, y):
                x = x + 1
            # x = (x + 1) % 8
        elif "ROT" in command:
            new_piece = tetris.rotate_piece(current_piece, command[4:])
            collides = board.collides(new_piece, x, y)
            print(collides)
            if collides == False:
                current_piece = new_piece
            elif collides == "OOB":
                temp_x = x
                if board.collides(new_piece, temp_x, y) == "OOB":
                    temp_x -= 1
                if board.collides(new_piece, temp_x, y) == False:
                    x = temp_x
                    current_piece = new_piece
        elif command == "C1":
            while not board.collides(current_piece, x, y):
                y += 1
            board.place(current_piece, x, y-1, current_color)
            choose_piece()
            x = 0
            y = 0
        elif "SPEED" in command:
            speed = int(command[6:])
            print("SPEED", speed)
    c = (c + 1) % 128
    