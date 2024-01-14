import flet as ft
from flet import *
from pages.utils.addTask import taskAddPopupComponent
def home():
    return Container(
        content=Column(
            [
                Column(
                    [
                        
                       
                        taskAddPopupComponent()
                        ]) 
            ]
        )
    )
    