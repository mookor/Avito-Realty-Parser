from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    url = Column(String(500))

    user = relationship("User", back_populates="tasks")
    contents = relationship("Content", back_populates="task")
    
class Content(Base):
    __tablename__ = "content"

    content_id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.task_id"))
    task = relationship("Task", back_populates="contents")

    
engine = create_engine('sqlite:///ARP.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_user(user: User):
    session.add(user)
    session.commit()

def create_task(task: Task):
    session.add(task)
    session.commit()

def create_content(content: Content):
    session.add(content)
    session.commit()

if __name__ == "__main__":
    user_1 = User(user_id=1)
    user_2 = User(user_id=2)

    task_1 = Task(user_id=1, url="https://example.com")
    task_2 = Task(user_id=2, url="https://example1.com")
    task_3 = Task(user_id=2, url="https://example2.com")

    create_user(user_1)
    create_user(user_2)

    create_task(task_1)
    create_task(task_2)
    create_task(task_3)

    content_1 = Content(content_id = 123, task_id=task_1.task_id)
    content_2 = Content(content_id = 124, task_id=task_1.task_id)

    content_3 = Content(content_id = 125, task_id=task_2.task_id)
    content_4 = Content(content_id = 126, task_id=task_2.task_id)
    content_5 = Content(content_id = 127, task_id=task_2.task_id)

    create_content(content_1)
    create_content(content_2)
    create_content(content_3)
    create_content(content_4)
    create_content(content_5)
    x = 1