import flet as ft
from flet import *
from pages.utils.addTask import taskAddPopupComponent
def today():
    return Container(
        content=Column(
            [
                
                Column(
                    [
                        Text("No tasks found")
                        
                        ]) 
            ]
        )
    )
    