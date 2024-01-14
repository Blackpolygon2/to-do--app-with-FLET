import flet as ft
from flet import *
from pages import homePage, TodayPage
from pages.utils import navbar, addTask
import threading

def main(page: ft.Page):
    page.update()
    page.title = "To Do App"
    
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
            addTask.addTaskFunction()
            
            page.update()
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

