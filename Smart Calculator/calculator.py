while True:
    line = input()
    if line == '/exit':
        print('Bye!')
        break
    args = [int(s) for s in line.split()]
    if len(args) == 1:
        print(args[0])
    if len(args) == 2:
        print(args[0] + args[1])