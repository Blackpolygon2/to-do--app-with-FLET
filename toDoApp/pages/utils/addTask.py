import flet as ft
from flet import *
import sqlalchemy
from .database import Task, engine, session

def dismissed(e):
    pass
def change_time_due(e):
    pass
def change_time_start(e):
    pass
def change_date(e):
    pass
def choose_priority(priority):
    pass
time_picker_for_due_time= TimePicker(
                            confirm_text="Confirm",
                            error_invalid_text="Time out of range",
                            help_text="Pick your time slot",
                            on_change=change_time_due,
                            on_dismiss=dismissed,
    ),
time_picker_for_start_time= TimePicker(
                            confirm_text="Confirm",
                            error_invalid_text="Time out of range",
                            help_text="Pick your time slot",
                            on_change=change_time_start,
                            on_dismiss=dismissed,
    ),
date_picker = DatePicker(
        on_change=change_date,
        on_dismiss=dismissed,
    )
pichtimebutton = ButtonStyle(
    color={
        
    },
    shape=RoundedRectangleBorder(radius=5),
    
)
 

def taskAddPopupColumn():

    return Column(
        [ 
           TextField(label='Task Title', autofocus=True),
           TextField(label="Task Description (Optional)"),
           Row(
               [
                   OutlinedButton(text="pick Due Date",on_click=lambda _: date_picker.pick_date(), style=pichtimebutton),
                   OutlinedButton(text="pick Due Time", on_click=lambda _: time_picker_for_due_time.pick_time(), style=pichtimebutton),
                   OutlinedButton(text="pick Start time", on_click=lambda _: time_picker_for_start_time.pick_time(), style=pichtimebutton)
               ], alignment=MainAxisAlignment.CENTER,spacing=10
           ),
           Text("Priority"),
           Row(
               [
                   FilledTonalButton("Low",on_click=choose_priority(1)),
                   FilledTonalButton("Medium",on_click=choose_priority(2)),
                   FilledTonalButton("High",on_click=choose_priority(3))
               ],alignment=MainAxisAlignment.CENTER,spacing=10
           ),
           
           
        ],spacing=30
    )
def bs_dismissed(e):
    pass    
def PopupAddTaskBottomSheet():
    print("hello")
    return BottomSheet(
        ft.Container(
            content=taskAddPopupColumn(),
            padding=15,
        ),
        open=True,
        on_dismiss=bs_dismissed,
    )
    
def addTaskFunction():
    new_object = Task(taskname = "wash hands", taskdescription = "wash your hands", tasktimestart = "10:00", tasktimeend = "11:00", taskpriority = 1, istaskcompleted = False, taskdaydue = "2023-05-01", istaskreocuring = False)
    session.add(new_object)
    session.commit()

    # Example: Querying data from the database
    result = session.query(Task).filter_by(taskname='wash hands')
    print(result)
   


# Example: Inserting data into the database

