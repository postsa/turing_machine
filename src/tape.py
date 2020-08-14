class Square:
    def __init__(self, previous):
        self.symbol = " "
        self.previous = previous
        self.next = None


class Tape:
    def __init__(self):
        self.position = 0
        self.current_square = Square(None)

    def read_current_symbol(self):
        return self.current_square.symbol

    def seek_left(self):
        if self.current_square.previous:
            self.current_square = self.current_square.previous
            self.position -= 1

    def seek_right(self):
        if not self.current_square.next:
            next_square = Square(self.current_square)
            self.current_square.next = next_square
            self.current_square = next_square
        else:
            self.current_square = self.current_square.next
        self.position += 1

    def print_symbol(self, symbol):
        self.current_square.symbol = symbol

    def erase(self):
        self.current_square.symbol = " "

    def get_state(self):
        starting_position = self.position
        state = ""
        while self.current_square.previous:
            self.seek_left()
        while self.current_square.next:
            state += self.read_current_symbol()
            self.seek_right()
        state += self.read_current_symbol()
        while self.position > starting_position:
            self.seek_left()
        return state
