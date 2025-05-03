from PyQt6.QtWidgets import QMenuBar, QMainWindow
from PyQt6.QtGui import QAction
class Menu:
    menu_bar: QMenuBar

    def __init__(self, menu_bar: QMenuBar, parent: QMainWindow | None = None) -> None:
        self.menu_bar = menu_bar

        self.menu_bar.addMenu("File")
        self.menu_bar.addMenu("Run")
        self.menu_bar.addMenu("FSM")
        self.menu_bar.addMenu("Help")
