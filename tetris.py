pieces = [
    [
        [0, 1, 1],
        [1, 1, 0],
    ],
    [
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]
colors = [5, 13, 21, 3, 37, 45, 53]

def rotate_piece(piece, direction):
    new_list = []
    if direction == "RIGHT":
        for x in range(0, len(piece[0])):
            new_list_2 = []
            for y in range(len(piece)-1, -1, -1):
                new_list_2.append(piece[y][x])
            new_list.append(new_list_2)
    elif direction == "LEFT":
        for x in range(len(piece[0])-1, -1, -1):
            new_list_2 = []
            for y in range(0, len(piece)):
                new_list_2.append(piece[y][x])
            new_list.append(new_list_2)
    return new_list

# print(pieces[1])
# print(rotate_piece(pieces[1], "LEFT"))
# print(rotate_piece(rotate_piece(pieces[1], "LEFT"), "LEFT"))

class Board():
    def __init__(self, x, y):
        self.matrix = []
        for i in range(y):
            self.matrix.append([0] * x)
        self.x = x
        self.y = y
    
    def place(self, piece, x, y, color):
        for iy in range(len(piece)):
            for ix in range(0, len(piece[0])):
                if piece[iy][ix] == 1:
                    self.matrix[y - iy][x + ix] = color
    
    def clearRows(self):
        for iy in range(self.y):
            if self.row_filled(iy) == self.x:
                self.matrix.remove(self.matrix[iy])
                self.matrix = [[0]*8] + self.matrix
    
    def collides(self, piece, x, y):
        try:
            if (x < 0) or (x + len(piece[0]) > self.x) or (y >= self.y):
                return "OOB"
            for iy in range(len(piece)):
                for ix in range(0, len(piece[0])):
                    if ((y - iy) >= len(self.matrix)) or ((x + ix) >= len(self.matrix[y - iy])) or ((y - iy) < 0):
                        continue
                    elif piece[iy][ix] == 1 and self.matrix[y - iy][x + ix] > 0:
                        return True
                        # print(ix, iy, x + ix, y - iy)
        except IndexError as e:
            pass
        return False
            
    def row_filled(self, y):
        filled = 0
        for ix in range(self.x):
            if self.matrix[y][ix] > 0:
                filled += 1
        return filled
        
    def column_height(self, x):
        for iy in range(self.y):
            if self.matrix[iy][x] > 0:
                return self.y - iy
        return 0
    
    def finished(self):
        for ix in range(self.x):
            # print(self.column_height(ix))
            if self.column_height(ix) == self.y:
                return True
        return False