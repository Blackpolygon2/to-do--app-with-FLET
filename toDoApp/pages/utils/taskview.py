import flet as ft
from flet import *

# i want the task be have 
def taskcontrol(task):
    task =  Column(
        [
            Row(
                [
                    Checkbox(),Text(task)
                ]
            ),
            Row(
                [
                    
                ]
            )
        ]
    ) 
    return