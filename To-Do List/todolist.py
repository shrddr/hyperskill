class Task():
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class TaskList():
    def __init__(self):
        self.tasks = []

    def add(self, t):
        self.tasks.append(t)

    def __str__(self):
        lines = [f'{i+1}) {t}' for i, t in enumerate(self.tasks)]
        s = 'Today:\n' + '\n'.join(lines)
        return s


if __name__ == '__main__':
    tasks = TaskList()
    tasks.add(Task('Do yoga'))
    tasks.add(Task('Make breakfast'))
    tasks.add(Task('Learn basics of SQL'))
    tasks.add(Task('Learn what is ORM'))
    print(tasks)