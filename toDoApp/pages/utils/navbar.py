import flet as ft
from flet import *
from .addTask import addTaskFunction



def changePage(indexcontrol,navigation):
        
        my_index = indexcontrol.control.selected_index
        print(my_index)
        navigation( my_index)
 
        
def navbar(navigation):
    return ft.NavigationBar(
        label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        selected_index=0,
        on_change=lambda e: changePage(e,navigation),
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_ROUNDED, label="Home", ),
            ft.NavigationDestination(
                icon=ft.icons.FORMAT_LIST_BULLETED_ROUNDED, selected_icon=ft.icons.CHECKLIST_RTL_ROUNDED, label="Today", ),
            ft.NavigationDestination(icon=ft.icons.ADD,
                                     selected_icon=ft.icons.ADD_ROUNDED, ),
            ft.NavigationDestination(icon=ft.icons.DATE_RANGE_OUTLINED,
                                     selected_icon=ft.icons.DATE_RANGE_ROUNDED, label="Calendar", ),
            ft.NavigationDestination(icon=ft.icons.SETTINGS_OUTLINED,
                                     selected_icon=ft.icons.SETTINGS_ROUNDED, label="Settings", ),
        ]
    )
