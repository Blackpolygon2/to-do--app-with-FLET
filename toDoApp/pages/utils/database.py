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
    tasktimestart = Column(String(50), nullable=True)
    tasktimeend = Column(String(50), nullable=True)
    taskpriority = Column(String(50), nullable=False)
    istaskcompleted = Column(Boolean, nullable=False)
    taskdaydue = Column(String(50), nullable=True)
    istaskreocuring = Column(Boolean, nullable=False)
    taskreocuring = relationship('ReocuringTask', back_populates='task', uselist=False)
    taskdatemade = Column(DateTime, default=datetime.utcnow) 
        
        # Add other columns as needed
class ReocuringTask(Base):
    __tablename__ = 'ReocuringTask'
    id = Column(Integer, Sequence('task_details_id_seq'), primary_key=True)
    task_id = Column(Integer, ForeignKey('Task.id'), unique=True)
    task = relationship('Task', back_populates='taskreocuring', uselist=False) 
    isreocuringmonday = Column(Boolean)
    isreocuringtuesday = Column(Boolean)
    isreocuringwednesday = Column(Boolean)
    isreocuringthursday = Column(Boolean)
    isreocuringfriday = Column(Boolean)
    isreocuringsaturday = Column(Boolean)
    isreocuringsunday = Column(Boolean)
    isreocuringmonthly = Column(Boolean)
    dayofmonthreocuring = Column(String(50))
    isreocuringyearly = Column(Boolean)
    dayofyearreocuring = Column(String(50))
        
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

    