from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

if __name__ == '__main__':
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base = declarative_base()


    class Record(Base):
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String, default='default_value')
        deadline = Column(Date, default=datetime.today())

        def __repr__(self):
            return self.task


    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()

    def print_rows(rows, emptymessage, dates=False):
        for i, r in enumerate(rows, 1):
            s = f"{i}. {r.task}"
            if dates:
                month = datetime.strftime(r.deadline, "%b")
                s += f". {r.deadline.day} {month}"
            print(s)
        if not rows:
            print(emptymessage)
        print('')

    def get_tasks(day, today=False):

        if today:
            day_mon = datetime.strftime(day, "%d %b")
            print(f"Today {day_mon}:")
        else:
            print(datetime.strftime(day, "%A %d %b:"))

        rows = sess.query(Record).filter(Record.deadline == day.date()).all()
        print_rows(rows, "Nothing to do!")


    while True:
        print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
        cmd = int(input())
        if not cmd:
            break

        if cmd == 1:
            today = datetime.today()
            get_tasks(today, True)

        if cmd == 2:
            today = datetime.today()
            for i in range(7):
                day = today + timedelta(days=i)
                get_tasks(day)

        if cmd == 3:
            print("All tasks:")
            rows = sess.query(Record).order_by(Record.deadline).all()
            print_rows(rows, "Nothing to do!", True)

        if cmd == 4:
            print("Missed tasks:")
            today = datetime.today().date()
            rows = sess.query(Record).filter(Record.deadline < today).order_by(Record.deadline).all()
            print_rows(rows, "Nothing is missed!")

        if cmd == 5:
            print("Enter task")
            text = input()
            print("Enter deadline")
            date_string = input()
            dt = datetime.strptime(date_string, '%Y-%m-%d')
            new_row = Record(task=text, deadline=dt)
            sess.add(new_row)
            sess.commit()

        if cmd == 6:
            print("Choose the number of the task you want to delete:")
            rows = sess.query(Record).order_by(Record.deadline).all()
            print_rows(rows, "Nothing to delete", True)

            n = int(input())
            target_row = rows[n-1]
            sess.delete(target_row)
            sess.commit()
            print("The task has been deleted!\n")
