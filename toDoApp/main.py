import flet as ft
from flet import *
from pages import homePage, TodayPage
from pages.utils import navbar, addTask, database
import threading


def main(page: ft.Page):
    page.update()
    page.title = "To Do App"

    #this fuction depends on the changpage function in the nav bar component from utils 
    def go_to(page_index):
        while len(page.controls) > 1:
            page.remove_at(1)
        
        if page_index == 0:
            print("home")
            page.add(
                        AppBar(title=Text("Home")),
                        homePage.home(),
                        #navbar.navbar(page,go_to()),  
            )
        if page_index == 1:
            print("today")
            page.add(
                        AppBar(title=Text("Today")),
                        TodayPage.today(),
                        #navbar.navbar(page,go_to()),  
            )
        if page_index == 2:
            print("task")
            taskAddPopUp= addTask.PopupAddTaskBottomSheet(page)
            page.overlay.append(taskAddPopUp)
            addTask.appendpopups(page)
            page.update()
            taskAddPopUp.open = True
            
            page.update()
        if page_index == 3:
            print("clander")
            page.add(
                        AppBar(title=Text("calender")),
                        TodayPage.today(),
                        #navbar.navbar(page,go_to()),
                        
            )
    page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route) 
    
    page.add(navbar.navbar(go_to))
    
    go_to(0)
    print(page.controls)
    page.update()
    

ft.app(target=main)


