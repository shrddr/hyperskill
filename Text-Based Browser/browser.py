import os.path
import argparse
import requests

argparser = argparse.ArgumentParser()
argparser.add_argument("dir")
args = argparser.parse_args()


def display(url, dot_position):

    filename = url[:dot_position]
    filepath = os.path.join(args.dir, filename)

    if os.path.exists(filepath):
        with open(filepath) as f:
            page = f.read()
    else:
        if url[:8] != 'https://':
            url = 'https://' + url
        r = requests.get(url)
        page = r.text

        if not os.path.exists(args.dir):
            os.mkdir(args.dir)
        if not os.path.isdir(args.dir):
            print("Error: dir exists but is not a dir")
        with open(filepath, 'w', encoding='utf8') as f:
            f.write(page)

    print(page)



history = []
while True:
    cmd = input()
    if cmd == "exit":
        break

    if cmd == "back":
        if len(history) >= 2:
            display(history[-2])

    dot_position = cmd.find('.')
    if dot_position >= 0:
        display(cmd, dot_position)
        history.append(cmd)
    else:
        print('Error: no dot')
