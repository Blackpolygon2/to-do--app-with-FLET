import flet as ft
from flet import *
import sqlalchemy
from .database import Task, engine, session
# set these to be text and asing a text to the button uintead of using the button built in text
new_object = Task
pickDueDate = Text("pick Due Date")
pickDueTime = Text("pick Due Time")
pickStarttime = Text("pick Due Time")
userPage = ft.Page
TextDueDate = Text("Due Date", visible=False)
TextStarttime = Text("Start Time", visible=False)
TextDueTime = Text("Due Time", visible=False)
pichtimebutton = ButtonStyle(
    shape=RoundedRectangleBorder(radius=5),
)
prioritybuttonsstyle = ButtonStyle(
    shape=RoundedRectangleBorder(radius=5),
)
bgcolorforfilledbuttons = "#6a7a67"


def change_date(e):
    new_object.taskdaydue = e.control.value
    global pickDueDate
    pickDueDate.value = str(e.control.value)
    pickDueDate.update()
    TextDueDate.visible = True
    TextDueDate.update()


def time_changed_due(e):
    new_object.tasktimeend = e.control.value
    global pickDueTime
    pickDueTime.value = str(e.control.value)
    pickDueTime.update()
    TextDueTime.visible = True
    TextDueTime.update()


def time_changed_start(e):
    new_object.tasktimestart = e.control.value
    global pickStarttime
    pickStarttime.value = str(e.control.value)
    pickStarttime.update()
    TextStarttime.visible = True
    TextStarttime.update()


def dismissed(e):
    pass


def time_changed(timePicker, e):
    pass


def choose_priority(priority,):
    print(priority.control.selected)
    new_object.taskpriority = str(priority.control.selected)


def appendpopups(page):
    page.overlay.append(date_picker)
    page.overlay.append(time_picker_start)
    page.overlay.append(time_picker_due)


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


time_picker_start = TimePicker(
    on_change=time_changed_start,
    on_dismiss=dismissed,
)
time_picker_due = TimePicker(
    on_change=time_changed_due,
    on_dismiss=dismissed,
)

date_picker = DatePicker(
    on_change=change_date,
    on_dismiss=dismissed,
)


def taskAddPopupColumn(page):

    return Column(
        [
            TextField(label='Task Title', autofocus=True,
                      on_change=lambda _: add_task_name,),
            TextField(label="Task Description (Optional)", multiline=True,
                      on_change=lambda _: add_task_description,),
            Row(
                [
                    Column(
                        [
                            TextDueDate,
                            OutlinedButton(content=pickDueDate, on_click=lambda _: date_picker.pick_date(
                            ), style=pichtimebutton),
                        ]
                    ),
                    Column(
                        [
                            TextStarttime,
                            OutlinedButton(content=pickStarttime, on_click=lambda _: time_picker_start.pick_time(
                            ), style=pichtimebutton)
                        ]
                    ),
                    Column(
                        [
                            TextDueTime,
                            OutlinedButton(content=pickDueTime, on_click=lambda _: time_picker_due.pick_time(
                            ), style=pichtimebutton),
                        ]
                    ),


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


            ElevatedButton(icon=icons.CHECK,
                           on_click=addTaskFunction, text="Add Task",),

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
