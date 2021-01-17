while True:
    line = input()
    if line == '/exit':
        print('Bye!')
        break
    if line == '/help':
        print('The program calculates the sum of numbers')
        continue
    args = [int(s) for s in line.split()]
    if len(args) > 0:
        res = sum(args)
        print(res)
