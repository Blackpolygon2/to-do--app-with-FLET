import flet as ft
from flet import *
import sqlalchemy
from .database import Task, engine, session
# set these to be text and asing a text to the button uintead of using the button built in text 
new_object = Task
pickDueDate = "pick Due Date"
pickDueTime = "pick Due Time"
pickStarttime = "pick Due Time"
userPage= ft.Page

def get_page(pagevar):
    global userPage
    userPage= pagevar
    print(id(userPage))
    print(id(pagevar))
def dismissed(e):
    pass


def time_changed(timePicker, e):
    pass


def change_date(e):
    new_object.taskdaydue = e.control.value
    print(str(e.control.value))
    global pickDueDate
    pickDueDate=str(e.control.value)
    
    print(id(userPage))
    userPage.update()


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


def appendpopups(page):
    page.overlay.append(date_picker)
    page.overlay.append(time_picker)


def add_task_name(e):
    taskName = e.control.value
    new_object.taskname = taskName


def add_task_description(e):
    taskdescription = e.control.value
    new_object.taskdescription = taskdescription

def addTaskFunction():
    new_object = Task(taskname="wash hands", taskdescription="wash your hands", tasktimestart="10:00",
                      tasktimeend="11:00", taskpriority=1, istaskcompleted=False, taskdaydue="2023-05-01", istaskreocuring=False)
    session.add(new_object)
    session.commit()

    # Example: Querying data from the database
    result = session.query(Task).filter_by(taskname='wash hands')
    print(result)




def taskAddPopupColumn(page):

    return Column(
        [
            TextField(label='Task Title', autofocus=True,
                      on_change=lambda _: add_task_name,),
            TextField(label="Task Description (Optional)", multiline=True,
                      on_change=lambda _: add_task_description,),
            Row(
                [
                    OutlinedButton(text=pickDueDate, on_click=lambda _: date_picker.pick_date(
                    ), style=pichtimebutton),
                    OutlinedButton(text=pickDueTime, on_click=lambda _: date_picker.pick_date(
                    ), style=pichtimebutton),
                    OutlinedButton(text=pickStarttime, on_click=lambda _: date_picker.pick_date(
                    ), style=pichtimebutton)
                ], alignment=MainAxisAlignment.CENTER, spacing=10
            ),
            Column(
                [
                    Text("Priority"),
                    SegmentedButton(
                        selected={"1"},
                        show_selected_icon=False,
                        # style=prioritybuttonsstyle,
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
                ]
            ),


            ElevatedButton(icon=icons.CHECK, on_click=addTaskFunction, text="Add Task",),

        ], spacing=30, alignment=MainAxisAlignment.CENTER, horizontal_alignment=MainAxisAlignment.CENTER
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
