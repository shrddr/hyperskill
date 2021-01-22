class InvalidExpression(Exception):
    pass


class InvalidIdentifier(Exception):
    pass


class UnknownIdentifier(Exception):
    pass


ops = ['*', '/', '+', '-', '(', ')']
priorities = {'+': 0, '-': 0, '*': 1, '/': 1}


def tokenize(str):
    tokens = []
    token = ''
    for c in str:
        if not c.strip():
            continue
        if c in ops:
            if token:
                tokens.append(token)
            token = c
        elif c.isalpha():
            if token:
                if token.isalpha():
                    token += c
                else:
                    tokens.append(token)
                    token = c
            else:
                token = c
        elif c.isdigit():
            if token:
                if token.isdigit():
                    token += c
                else:
                    tokens.append(token)
                    token = c
            else:
                token = c

        else:
            raise InvalidExpression
    if token:
        tokens.append(token)

    return tokens


def to_postfix(tokens):
    polish = []
    stack = []
    for t in tokens:
        if t.isalpha():
            if t not in vars:
                raise UnknownIdentifier
            x = vars[t]
            polish.append(x)
        elif t.isdigit():
            x = int(t)
            polish.append(x)
        elif t in priorities:
            while stack and stack[-1] in priorities and priorities[t] <= priorities[stack[-1]]:
                polish.append(stack.pop())
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                polish.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise InvalidExpression

    while stack:
        op = stack.pop()
        if op in ['(', ')']:
            raise InvalidExpression
        polish.append(op)

    return polish


def eval_postfix(polish):
    stack = []
    for t in polish:
        if type(t) == int:
            stack.append(t)
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()
            if t == '+':
                x = arg2 + arg1
            elif t == '-':
                x = arg2 - arg1
            elif t == '*':
                x = arg2 * arg1
            elif t == '/':
                x = arg2 // arg1
            else:
                raise NotImplementedError
            stack.append(x)
    return stack.pop()


def eval_expression(line):
    tokens = tokenize(line)
    polish = to_postfix(tokens)
    res = eval_postfix(polish)
    return res


vars = {}
while True:
    line = input().strip()

    if len(line) and line[0] == '/':
        if line == '/exit':
            print('Bye!')
            break
        elif line == '/help':
            print('The program calculates the +-*/() of numbers')
            continue
        else:
            print('Unknown command')
            continue

    try:
        if not line:
            continue
        eq_pos = line.find("=")
        if eq_pos > -1:
            # definition
            var = line[:eq_pos].strip()
            if not var.isalpha():
                raise InvalidIdentifier
            res = eval_expression(line[eq_pos + 1:])
            vars[var] = res
        else:
            res = eval_expression(line)
            if res is not None:
                print(res)

    except (ValueError, IndexError, InvalidExpression):
        print('Invalid expression')
        continue
    except InvalidIdentifier:
        print('Invalid Identifier')
        continue
    except UnknownIdentifier:
        print('Unknown Identifier')
        continue
