import mido

class InputHandler():
    def __init__(self):
        names = mido.get_input_names()
        for name in names:
            print(name)
            if "Launchpad MK2" in name:
                self.port = mido.open_input(name)
        if not self.port:
            raise Exception("No launchpad")
    
    def poll(self, debug=False):
        msg = self.port.poll()
        if debug and msg:
            print(msg)
        if msg:
            if msg.type == "control_change" and msg.value == 127:
                if msg.control == 104:
                    return "ROT_RIGHT"
                elif msg.control == 105:
                    return "ROT_LEFT"
                elif msg.control == 106:
                    return "LEFT"
                elif msg.control == 107:
                    return "RIGHT"
                elif msg.control == 111:
                    return "C1"
                elif msg.control == 109:
                    return "C2"
                elif msg.control == 110:
                    return "C3"
                elif msg.control == 108:
                    return "C4"
            elif msg.type == "note_on" and msg.note % 10 == 9:
                return "SPEED_" + str((msg.note - 9)//10)
        return None

if __name__ == "__main__":
    ih = InputHandler()
    while 1:
        g = ih.poll(True)
    