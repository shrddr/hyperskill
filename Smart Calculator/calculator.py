class InvalidExpression(Exception):
    pass


def try_int(s):
    try:
        return int(s)
    except ValueError:
        return None


class Expr:
    def __init__(self):
        self.arg = None
        self.op = None

    def complete(self):
        return self.arg is not None and self.op is not None

    def compute(self, left):
        if self.op == '+':
            return left + self.arg
        if self.op == '-':
            return left - self.arg

    def parse_op(self, c):
        if self.op is None:
            self.op = c
        else:
            if c == '-':
                self.op = '-' if self.op == '+' else '+'

    def parse_arg(self, i):
        if self.arg is None:
            self.arg = i
        else:
            raise InvalidExpression

    def parse(self, s):
        i = try_int(s)
        if i is None:
            for c in s:
                if c in ['-', '+']:
                    self.parse_op(c)
                else:
                    raise InvalidExpression

        else:
            self.parse_arg(i)


while True:
    line = input()
    if len(line) and line[0] == '/':
        if line == '/exit':
            print('Bye!')
            break
        elif line == '/help':
            print('The program calculates the +- of numbers')
            continue
        else:
            print('Unknown command')
            continue

    args = line.split()
    res = None
    e = Expr()
    try:
        for s in args:
            if res is None:
                res = int(s)
                continue
            e.parse(s)
            if e.complete():
                res = e.compute(res)
                e = Expr()
        if res is not None:
            print(res)

    except (ValueError, InvalidExpression):
        print('Invalid expression')
        continue
