from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey, Boolean, JSON, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from datetime import datetime

Base = declarative_base()

# Provide the path to the existing database file
existing_database_path = 'taskDatabase.db'
engine = create_engine(f'sqlite:///{existing_database_path}', echo=True)



class Task(Base):
    __tablename__ = 'Task'
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    taskname = Column(String(50) , nullable=False)
    taskdescription = Column(String(400))
    taskdaystart = Column(String(50), nullable=True)
    taskpriority = Column(String(50), nullable=False)
    istaskcompleted = Column(Boolean, nullable=False)
    taskdaydue = Column(String(50), nullable=True)
    istaskreocuring = Column(Boolean, nullable=False)
    isreocuringmonday = Column(Boolean)
    isreocuringtuesday = Column(Boolean)
    isreocuringwednesday = Column(Boolean)
    isreocuringthursday = Column(Boolean)
    isreocuringfriday = Column(Boolean)
    isreocuringsaturday = Column(Boolean)
    isreocuringsunday = Column(Boolean)
    taskdatemade = Column(DateTime, default=datetime.utcnow)
    
        
        # Add other columns as needed

    # Define the User class
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    setting = Column(JSON)
    taskdatemade = Column(DateTime, default=datetime.utcnow) 
        # Add other columns as needed
if not os.path.exists(existing_database_path):
    print(f"Error: The database file '{existing_database_path}' does not exist.")
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

    