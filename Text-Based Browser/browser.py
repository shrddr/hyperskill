import os.path
import argparse

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

argparser = argparse.ArgumentParser()
argparser.add_argument("dir")
args = argparser.parse_args()

content = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}


def display(url):
    if url in content:
        filename = url[:dot_position]
        filepath = os.path.join(args.dir, filename)

        if os.path.exists(filepath):
            with open(filepath) as f:
                page = f.read()
        else:
            page = content[url]
            if not os.path.exists(args.dir):
                os.mkdir(args.dir)
            if not os.path.isdir(args.dir):
                print("Error: dir exists but is not a dir")
            with open(filepath, 'w') as f:
                f.write(page)

        print(page)
    else:
        print("Error: unknown url")


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
