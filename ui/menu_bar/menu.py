from PyQt5.QtWidgets import QMenuBar

class Menu:
    
    def __init__(self, menu_bar: QMenuBar):
        self.menu_bar = menu_bar

        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("New Machine")
        file_menu.addAction("Open World")
        file_menu.addAction("Exit")

