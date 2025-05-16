from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFrame, QSplitter, QHBoxLayout
from PyQt5.QtCore import QSize, Qt, QSettings
from ui.menu_bar.menu import Menu
from ui.components.frames import TopFrame, BottomFrame
from context.context import AppContext

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.start_ui()

    def start_ui(self):
        context = AppContext()
        context.settings = QSettings("FSM", "FSM")

        # set window properties
        self.setWindowTitle("FSM")
        self.setMinimumSize(QSize(1200, 800))

        # menu bar
        Menu(self)

        # layout setup
        central_widget = QWidget()
        vlayout = QVBoxLayout()
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(12)
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("background-color: #ced1dc;")

        # add frames and splitter
        top_frame = QFrame()
        bottom_frame = QFrame()

        top_frame_layout = QHBoxLayout()
        top_frame_layout.setContentsMargins(0, 0, 0, 0)
        top_frame_layout.setSpacing(0)
        top_frame.setLayout(top_frame_layout)

        bottom_frame_layout = QHBoxLayout()
        bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        bottom_frame_layout.setSpacing(0)
        bottom_frame.setLayout(bottom_frame_layout)

        top_frame_layout.addWidget(TopFrame())
        bottom_frame_layout.addWidget(BottomFrame())

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(top_frame)
        splitter.addWidget(bottom_frame)
        
        splitter.setSizes([70, 30])

        central_widget.layout().addWidget(splitter)

        self.show()