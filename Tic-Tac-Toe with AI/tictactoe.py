
class Board:
    size = 3

    def __init__(self, text):
        self.data = []
        if len(text) != self.size * self.size:
            raise ValueError
        for c in text:
            if c in ['_', 'O', 'X']:
                self.data.append(c)
            else:
                raise ValueError
        self.data = [self.data[self.size * i:self.size * (i + 1)] for i in range(self.size)]

    def is_x_move(self):
        xs = 0
        for y in range(self.size):
            xs += self.data[y].count('X')
        os = 0
        for y in range(self.size):
            os += self.data[y].count('O')
        return xs == os

    def is_empty(self, x, y):
        return self.data[y][x] == '_'

    def make_move(self, x, y):
        if self.is_x_move():
            self.data[y][x] = 'X'
        else:
            self.data[y][x] = 'O'

    def state(self):
        for x in range(self.size):
            is_x = [self.data[y][x] == 'X' for y in range(self.size)]
            if all(is_x):
                return "X wins"
            is_o = [self.data[y][x] == 'O' for y in range(self.size)]
            if all(is_o):
                return "O wins"

        for y in range(self.size):
            is_x = [self.data[y][x] == 'X' for x in range(self.size)]
            if all(is_x):
                return "X wins"
            is_o = [self.data[y][x] == 'O' for x in range(self.size)]
            if all(is_o):
                return "O wins"

        is_x = [self.data[x][x] == 'X' for x in range(self.size)]
        if all(is_x):
            return "X wins"
        is_x = [self.data[x][self.size-1-x] == 'X' for x in range(self.size)]
        if all(is_x):
            return "X wins"
        is_o = [self.data[x][x] == 'O' for x in range(self.size)]
        if all(is_o):
            return "O wins"
        is_o = [self.data[x][self.size-1-x] == 'O' for x in range(self.size)]
        if all(is_o):
            return "O wins"

        for x in range(self.size):
            free = [self.data[y][x] == '_' for y in range(self.size)]
            if any(free):
                return "Game not finished"

        return "Draw"

    def __str__(self):
        s = "---------\n"
        for y in range(self.size):
            s += "| " + " ".join(self.data[y]) + " |\n"
        s += "---------\n"
        return s


def ask_move(b):
    while True:
        print("Enter the coordinates:")
        text = input()
        values = text.split(" ")
        try:
            y = int(values[0])
            x = int(values[1])
            if 1 > x or x > 3 or 1 > y or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            x = x - 1
            y = y - 1
            if not b.is_empty(x, y):
                print("This cell is occupied! Choose another one!")
                continue
            b.make_move(x, y)
            print(b)
            print(b.state())
            break
        except ValueError:
            print("You should enter numbers!")
            continue


print("Enter the cells:")
text = input()
b = Board(text)
print(b)

ask_move(b)



