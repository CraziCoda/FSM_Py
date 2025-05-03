from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt
from ui.menu_bar.menu import Menu
from ui.top.top_layout import TopLayout
from ui.bottom.bottom_layout import BottomLayout

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
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # top and bottom layout
        top_layout = TopLayout().get_layout()
        bottom_layout = BottomLayout().get_layout()
        self.main_layout.addLayout(top_layout)
        self.main_layout.addLayout(bottom_layout)

        # set central widget
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
