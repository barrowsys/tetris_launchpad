import mido

def pos_to_note(x, y):
    if y == 8:
        note = (9 - x) * 10
        note -= 1
        return note
    else:
        note = (8 - y) * 10
        note += x + 1
        return note
    # if y == 0:
    #     return 104 + x
    # elif y == 9:
    # else:

def make_message(matrix, speed):
    data = [0, 32, 41, 2, 24, 10]
    for y in range(8):
        for x in range(8):
            data.append(pos_to_note(x, y))
            data.append(matrix[y][x])
    for x in range(8):
        data.append(pos_to_note(x, 8))
        # print(speed, 8-x)
        if 8-speed <= x:
            data.append(3)
        else:
            data.append(0)
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
    
    def render(self, matrix, speed):
        msg = make_message(matrix, speed)
        self.port.send(msg)

print(pos_to_note(0, 9))