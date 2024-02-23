import flet as ft
from flet import *
import sqlalchemy
from .database import Task, engine, session
# set these to be text and asing a text to the button uintead of using the button built in text
new_object = Task
pickDueDate = Text("pick Due Date")
userPage = ft.Page
TextDueDate = Text("Due Date", visible=False)
reocouringtime = Text("reocuring time")
prioritybuttonsstyle = ButtonStyle(
    shape=RoundedRectangleBorder(radius=5),
)
bgcolorforfilledbuttons = "#6a7a67"

reocuringColumn = Column(
    [
        Text("days of the week to reapet"),
        Row(
            [
                SegmentedButton(

                    show_selected_icon=False,
                    # style=prioritybuttonsstyle,
                    on_change=lambda e: choose_day_of_week_reocuring(e),
                    allow_multiple_selection=True,
                    allow_empty_selection=True,
                    segments=[
                        ft.Segment(
                            value="1",
                            label=ft.Text("mon"),
                        ),
                        ft.Segment(
                            value="2",
                            label=ft.Text("tue"),
                        ),
                        ft.Segment(
                            value="3",
                            label=ft.Text("wed"),
                        ),
                        ft.Segment(
                            value="4",
                            label=ft.Text("thur"),
                        ),
                        ft.Segment(
                            value="5",
                            label=ft.Text("fri"),
                        ),
                        ft.Segment(
                            value="6",
                            label=ft.Text("sat"),
                        ),
                        ft.Segment(
                            value="7",
                            label=ft.Text("sun"),
                        ),


                    ],
                ),
            ], scroll=ScrollMode.AUTO
        ), Text("start time"),
        Row([
            OutlinedButton("pick start time", on_click=lambda _: Text(
                "pick start time")), reocouringtime
        ])
    ])


def change_date(e):
    new_object.taskdaydue = e.control.value
    global pickDueDate
    pickDueDate.value = str(e.control.value)
    pickDueDate.update()
    TextDueDate.visible = True
    TextDueDate.update()


def dismissed(e):
    global pickDueDate
    pickDueDate = Text("pick Due Date")


def choose_priority(priority,):
    print(priority.control.selected)
    new_object.taskpriority = str(priority.control.selected)


def appendpopups(page):
    page.overlay.append(date_picker)


def add_task_name(e):
    taskName = e.control.value
    new_object.taskname = taskName


def add_task_description(e):
    taskdescription = e.control.value
    new_object.taskdescription = taskdescription


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
            Text("Time Managment (Optional)"),
            Row(
                [
                    Column(
                        [
                            TextDueDate,
                            OutlinedButton(content=pickDueDate, on_click=lambda _: date_picker.pick_date(
                            ),),
                        ]
                    ),
                ], alignment=MainAxisAlignment.CENTER, spacing=10, scroll=ScrollMode.AUTO
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

            Switch(label="Task Reocuring", value=False),
            ElevatedButton(icon=icons.CHECK,
                           on_click=addTaskFunction, text="Add Task",),
            reocuringColumn,



        ], spacing=30, alignment=MainAxisAlignment.CENTER, horizontal_alignment=MainAxisAlignment.CENTER, height=500, scroll=ScrollMode.AUTO
    )


def bs_dismissed(e):
    pass


def PopupAddTaskBottomSheet(page):
    print("hello")
    return BottomSheet(
        ft.Container(
            content=taskAddPopupColumn(page),
            padding=15,
            height=500,
        ),
        open=True,
        on_dismiss=bs_dismissed,
        enable_drag=True,
        show_drag_handle=True,
    )


def addTaskFunction():
    new_object = Task(taskname="wash hands", taskdescription="wash your hands", tasktimestart="10:00",
                      tasktimeend="11:00", taskpriority=1, istaskcompleted=False, taskdaydue="2023-05-01", istaskreocuring=False)
    session.add(new_object)
    session.commit()

    # Example: Querying data from the database
    result = session.query(Task).filter_by(taskname='wash hands')
    print(result)


def addTaskFunction():
    new_object = Task(taskname="wash hands", taskdescription="wash your hands", tasktimestart="10:00",
                      tasktimeend="11:00", taskpriority=1, istaskcompleted=False, taskdaydue="2023-05-01", istaskreocuring=False)
    session.add(new_object)
    session.commit()

    # Example: Querying data from the database
    result = session.query(Task).filter_by(taskname='wash hands')
    print(result)
