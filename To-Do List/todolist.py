from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

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

    while True:
        print("1) Today's tasks\n2) Add task\n0) Exit")
        cmd = int(input())
        if not cmd:
            break

        if cmd == 1:
            print("Today:")
            rows = sess.query(Record).all()
            for r in rows:
                print(r)
            if not rows:
                print("Nothing to do!")

        if cmd == 2:
            print("Enter task")
            text = input()
            new_row = Record(task=text, deadline=datetime.today())
            sess.add(new_row)
            sess.commit()

