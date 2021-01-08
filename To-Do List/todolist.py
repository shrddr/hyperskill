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


    def get_tasks(day, today=False):

        if today:
            day_mon = datetime.strftime(day, "%d %b")
            print(f"Today {day_mon}:")
        else:
            print(datetime.strftime(day, "%A %d %b:"))

        rows = sess.query(Record).filter(Record.deadline == day.date()).all()

        for i, r in enumerate(rows, 1):
            print(f"{i}. {r.task}")
        if not rows:
            print("Nothing to do!")
        print('')


    while True:
        print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit")
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

            for i, r in enumerate(rows, 1):
                month = datetime.strftime(r.deadline, "%b")
                print(f"{i}. {r.task}. {r.deadline.day} {month}")

            if not rows:
                print("Nothing to do!")

        if cmd == 4:
            print("Enter task")
            text = input()
            print("Enter deadline")
            date_string = input()
            dt = datetime.strptime(date_string, '%Y-%m-%d')
            new_row = Record(task=text, deadline=dt)
            sess.add(new_row)
            sess.commit()

