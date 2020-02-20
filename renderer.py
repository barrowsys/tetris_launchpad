import mido

def pos_to_note(x, y):
    note = (8 - y) * 10
    note += x + 1
    return note
    # if y == 0:
    #     return 104 + x
    # elif y == 9:
    #     note = (9 - x) * 10
    #     note -= 1
    #     return note
    # else:

def make_message(matrix):
    data = [0, 32, 41, 2, 24, 10]
    for y in range(8):
        for x in range(8):
            data.append(pos_to_note(x, y))
            data.append(matrix[y][x])
    return mido.Message('sysex', data=data)

class Renderer():
    def __init__(self):
        names = mido.get_output_names()
        for name in names:
            print(name)
            if "Launchpad MK2" in name:
                self.port = mido.open_output(name)
        if not self.port:
            raise Exception("No launchpad")
    
    def render(self, matrix):
        msg = make_message(matrix)
        self.port.send(msg)

print(pos_to_note(0, 9))