import random


class Board:
    size = 3

    def __init__(self, text=None):
        if text:
            self.data = []
            if len(text) != self.size * self.size:
                raise ValueError
            for c in text:
                if c in ['_', 'O', 'X']:
                    self.data.append(c)
                else:
                    raise ValueError
            self.data = [self.data[self.size * i:self.size * (i + 1)] for i in range(self.size)]
        else:
            self.data = [['_'] * self.size for _ in range(self.size)]

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
            if all([self.data[y][x] == 'X' for y in range(self.size)]):
                return "X wins"
            if all([self.data[y][x] == 'O' for y in range(self.size)]):
                return "O wins"

        for y in range(self.size):
            if all([self.data[y][x] == 'X' for x in range(self.size)]):
                return "X wins"
            if all([self.data[y][x] == 'O' for x in range(self.size)]):
                return "O wins"

        if all([self.data[x][x] == 'X' for x in range(self.size)]):
            return "X wins"
        if all([self.data[x][self.size - 1 - x] == 'X' for x in range(self.size)]):
            return "X wins"
        if all([self.data[x][x] == 'O' for x in range(self.size)]):
            return "O wins"
        if all([self.data[x][self.size - 1 - x] == 'O' for x in range(self.size)]):
            return "O wins"

        for x in range(self.size):
            if any([self.data[y][x] == '_' for y in range(self.size)]):
                return "Game not finished"

        return "Draw"

    def __str__(self):
        s = "---------\n"
        for y in range(self.size):
            s += "| "
            for x in range(self.size):
                c = self.data[y][x]
                if c == '_':
                    c = ' '
                s += c + " "
            s += "|\n"
        s += "---------"
        return s


def human_move(b):
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
            return b.state()
        except ValueError:
            print("You should enter numbers!")
            continue


def ai_move(b):
    print('Making move level "easy"')
    while True:
        y = random.choice([0, 1, 2])
        x = random.choice([0, 1, 2])
        if b.is_empty(x, y):
            b.make_move(x, y)
            print(b)
            return b.state()


def play(px, po):
    b = Board()
    print(b)

    fx = human_move
    if px == 'easy':
        fx = ai_move

    fo = human_move
    if po == 'easy':
        fo = ai_move

    while True:
        if b.is_x_move():
            state = fx(b)
        else:
            state = fo(b)

        if state != "Game not finished":
            print(state)
            break


if __name__ == "__main__":
    while True:
        print("Input command:")
        text = input()
        if text == 'exit':
            break

        try:
            cmd, px, po = text.split()
        except ValueError:
            print('Bad parameters!')
            continue
        if cmd == "start" and px in ['user', 'easy'] and po in ['user', 'easy']:
            play(px, po)
            continue
        print('Bad parameters!')