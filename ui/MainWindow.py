from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFrame, QSplitter, QHBoxLayout
from PyQt5.QtCore import QSize, Qt
from ui.menu_bar.menu import Menu
from ui.components.frames import TopFrame, BottomFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.start_ui()

    def start_ui(self):
        # set window properties
        self.setWindowTitle("FSM")
        self.setMinimumSize(QSize(1200, 800))

        # menu bar
        Menu(self.menuBar(), self)

        # layout setup
        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        self.setCentralWidget(central_widget)

        # add frames and splitter
        top_frame = QFrame()
        bottom_frame = QFrame()

        top_frame.setFrameShape(QFrame.StyledPanel)
        bottom_frame.setFrameShape(QFrame.StyledPanel)

        top_frame.setGeometry(0, 0, self.width(), int(self.height() * 0.7))
        bottom_frame.setGeometry(0, int(self.height() * 0.7), self.width(), int(self.height() * 0.3))

        top_frame.setMinimumHeight(int(self.height() * 0.4))
        top_frame.setMaximumHeight(int(self.height() * 0.8))
    
        top_frame_layout = QHBoxLayout()
        top_frame.setLayout(top_frame_layout)

        bottom_frame_layout = QHBoxLayout()
        bottom_frame.setLayout(bottom_frame_layout)

        top_frame_layout.addWidget(TopFrame())
        bottom_frame_layout.addWidget(BottomFrame())

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(top_frame)
        splitter.addWidget(bottom_frame)

        central_widget.layout().addWidget(splitter)

        self.show()