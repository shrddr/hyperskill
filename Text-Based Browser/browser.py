import os.path
import argparse
import requests
import colorama
from bs4 import BeautifulSoup

argparser = argparse.ArgumentParser()
argparser.add_argument("dir")
args = argparser.parse_args()


def display(url):
    dot_position = cmd.find('.')
    filename = url[:dot_position]
    filepath = os.path.join(args.dir, filename)

    if os.path.exists(filepath):
        with open(filepath) as f:
            page = f.read()
    else:
        if url[:8] != 'https://':
            url = 'https://' + url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        page = ""
        supported_tags = ['li', 'p'] + [f'h{i}' for i in range(1, 7)]
        for tag in supported_tags:
            instances = soup.find_all(tag)
            for instance in instances:
                i_text = [s.strip() for s in instance.strings if s.strip()]

                for link in instance.find_all('a'):
                    if link.text in i_text:
                        idx = i_text.index(link.text)
                        i_text[idx] = colorama.Fore.BLUE + link.text + colorama.Style.RESET_ALL

                if i_text:
                    page += ' '.join(i_text) + "\n"

        if not os.path.exists(args.dir):
            os.mkdir(args.dir)
        if not os.path.isdir(args.dir):
            print("Error: dir exists but is not a dir")
        with open(filepath, 'w', encoding='utf8') as f:
            f.write(page)

    print(page)


colorama.init()
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
        display(cmd)
        history.append(cmd)
    else:
        print('Error: no dot')
