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

    def human_move(self):
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
                if not self.is_empty(x, y):
                    print("This cell is occupied! Choose another one!")
                    continue
                self.make_move(x, y)
                print(self)
                return self.state()
            except ValueError:
                print("You should enter numbers!")
                continue

    def ai_move_easy(self):
        print('Making move level "easy"')
        while True:
            y = random.choice([0, 1, 2])
            x = random.choice([0, 1, 2])
            if self.is_empty(x, y):
                self.make_move(x, y)
                print(self)
                return self.state()

    def ai_find_2row(self, c):
        for x in range(self.size):
            if [self.data[y][x] == c for y in range(self.size)].count(True) == 2:
                for y in range(self.size):
                    if self.data[y][x] != c:
                        return x, y
        for y in range(self.size):
            if [self.data[y][x] == c for x in range(self.size)].count(True) == 2:
                for x in range(self.size):
                    if self.data[y][x] != c:
                        return x, y
        if [self.data[x][x] == c for x in range(self.size)].count(True) == 2:
            for x in range(self.size):
                if self.data[x][x] != c:
                    return x, x
        if [self.data[x][self.size - 1 - x] == c for x in range(self.size)].count(True) == 2:
            for x in range(self.size):
                if self.data[x][self.size - 1 - x] != c:
                    return x, x
        return None

    def ai_move_medium(self):
        print('Making move level "medium"')
        my_char = 'X' if self.is_x_move() else 'O'
        ret = self.ai_find_2row(my_char)
        if ret:
            self.make_move(*ret)

        op_char = 'O' if my_char == 'X' else 'X'
        ret = self.ai_find_2row(op_char)
        if ret:
            self.make_move(*ret)

        while True:
            y = random.choice([0, 1, 2])
            x = random.choice([0, 1, 2])
            if self.is_empty(x, y):
                self.make_move(x, y)
                print(self)
                return self.state()


def play(player_x, player_o):
    b = Board()
    print(b)

    fx = b.human_move
    if player_x == 'easy':
        fx = b.ai_move_easy

    fo = b.human_move
    if player_o == 'easy':
        fo = b.ai_move_easy

    while True:
        if b.is_x_move():
            state = fx()
        else:
            state = fo()

        if state != "Game not finished":
            print(state)
            break


AI_MODES = ['easy', 'medium']
MODES = ['user'] + AI_MODES

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
        if cmd == "start" and px in MODES and po in MODES:
            play(px, po)
            continue
        print('Bad parameters!')