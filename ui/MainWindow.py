from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSize, Qt
from ui.menu_bar.menu import Menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("FSM")
        self.setMinimumSize(QSize(800, 600))

        # menu bar
        Menu(self.menuBar(), self)
        




