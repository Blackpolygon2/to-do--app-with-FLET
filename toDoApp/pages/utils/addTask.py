import flet as ft
from flet import *
#from sqlalchemy import *

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

 

def taskAddPopupComponent():

    return Column(
        [
           Text("Task Title"), 
           TextField(),
           Text("Task Description (Optional)"),
           TextField(),
           Row(
               [
                   FilledTonalButton(text="pick Due Date",on_click=lambda _: date_picker.pick_date()),
                   FilledTonalButton(text="pick Due Time", on_click=lambda _: time_picker_for_due_time.pick_time()),
                   FilledTonalButton(text="pick Start time", on_click=lambda _: time_picker_for_start_time.pick_time())
               ]
           ),
           Text("Priority"),
           Row(
               [
                   FilledTonalButton("Low",on_click=choose_priority(1)),
                   FilledTonalButton("Medium",on_click=choose_priority(2)),
                   FilledTonalButton("High",on_click=choose_priority(3))
               ]
           ),
           
           
        ]
    )
    
def addTaskFunction():
    pass