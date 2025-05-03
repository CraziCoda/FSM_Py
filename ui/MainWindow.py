from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt
from ui.menu_bar.menu import Menu

class MainWindow(QMainWindow):
    main_layout: QVBoxLayout | None  = None

    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("FSM")
        self.setMinimumSize(QSize(800, 600))

        # menu bar
        Menu(self.menuBar(), self)

        # main layout
        widget = QWidget()
        self.main_layout = QVBoxLayout()
        
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
