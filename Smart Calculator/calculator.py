line = input()
args = [int(s) for s in line.split()]
if len(args) == 2:
    print(args[0] + args[1])