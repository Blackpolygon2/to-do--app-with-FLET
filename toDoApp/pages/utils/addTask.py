import flet as ft
from flet import *
import sqlalchemy
from .database import Task, engine, session


def dismissed(e):
    pass


def time_changed(e):
    pass



def change_date(e):
    pass


def choose_priority(priority,):
    print(priority.control.selected)
    pass


time_picker = TimePicker(
    on_change=time_changed,
    on_dismiss=dismissed,
)

date_picker = DatePicker(
    on_change=change_date,
    on_dismiss=dismissed,
)
pichtimebutton = ButtonStyle(
    shape=RoundedRectangleBorder(radius=5),

)
prioritybuttonsstyle = ButtonStyle(
    shape=RoundedRectangleBorder(radius=5), 
)
bgcolorforfilledbuttons = "#6a7a67"
def appendpopups (page):
    page.overlay.append(date_picker)
    page.overlay.append(time_picker)
    
def taskAddPopupColumn(page):
    
    return Column(
        [
            TextField(label='Task Title', autofocus=True),
            TextField(label="Task Description (Optional)"),
            Row(
                [
                    OutlinedButton(text="pick Due Date", on_click=lambda _: date_picker.pick_date(
                    ), style=pichtimebutton),
                    OutlinedButton(text="pick Due Time", on_click=lambda _: time_picker.pick_time(
                    ), style=pichtimebutton),
                    OutlinedButton(text="pick Start time", on_click=lambda : print("hello"), style=pichtimebutton)
                ], alignment=MainAxisAlignment.CENTER, spacing=10
            ),
            Text("Priority"),
            SegmentedButton(
                selected={"1"},
                #style=prioritybuttonsstyle,
                on_change=lambda e: choose_priority(e),
                segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("Low"),
                ),
                ft.Segment(
                    value="2",
                    label=ft.Text("Medium"),
                ),
                ft.Segment(
                    value="3",
                    label=ft.Text("High"),
                    
                ),

            ],
            ),

            IconButton(icon=icons.CHECK, on_click=addTaskFunction),

        ], spacing=30, alignment=MainAxisAlignment.CENTER,horizontal_alignment=MainAxisAlignment.CENTER
    )


def bs_dismissed(e):
    pass


def PopupAddTaskBottomSheet(page):
    print("hello")
    return BottomSheet(
        ft.Container(
            content=taskAddPopupColumn(page),
            padding=15,
        ),
        open=True,
        on_dismiss=bs_dismissed,
    )


def addTaskFunction():
    new_object = Task(taskname="wash hands", taskdescription="wash your hands", tasktimestart="10:00",
                      tasktimeend="11:00", taskpriority=1, istaskcompleted=False, taskdaydue="2023-05-01", istaskreocuring=False)
    session.add(new_object)
    session.commit()

    # Example: Querying data from the database
    result = session.query(Task).filter_by(taskname='wash hands')
    print(result)


# Example: Inserting data into the database
