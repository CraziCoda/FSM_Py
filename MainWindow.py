from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FSM")
        self.setMinimumSize(QSize(800, 600))


