from source.backend.database import Base
from sqlalchemy import Column, String, Integer

class TaskDB(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)


class Task:
    def __init__(self, task_id: int, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Task({self.task_id}, {self.title})"
    

class Node:
    def __init__(self, data: Task):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head : Node | None = None