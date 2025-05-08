from PyQt5.QtWidgets import QHBoxLayout, QWidget, QFrame, QSplitter, QVBoxLayout
from PyQt5.QtCore import Qt
from ui.components.min_window import MinWindow


class TopFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        
    
    def init_ui(self):
        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)
        self.setLayout(hLayout)

        self.left = QFrame()
        self.main = QFrame()
        self.right = QFrame()

        self.left.setMinimumWidth(int(self.width() * 0.25))
        self.main.setMinimumWidth(int(self.width() * 0.5))
        self.right.setMinimumWidth(int(self.width() * 0.25))


        left_frame_layout = QVBoxLayout()
        left_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left.setLayout(left_frame_layout)

        left_frame_splitter = QSplitter(Qt.Vertical)
        left_frame_splitter.addWidget(MinWindow("World Manager"))
        left_frame_splitter.addWidget(MinWindow("States"))
        left_frame_layout.addWidget(left_frame_splitter)

        right_frame_layout = QVBoxLayout()
        right_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.right.setLayout(right_frame_layout)

        right_frame_splitter = QSplitter(Qt.Vertical)
        right_frame_splitter.addWidget(MinWindow("Simulation"))
        right_frame_splitter.addWidget(MinWindow(""))
        right_frame_layout.addWidget(right_frame_splitter)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left)
        splitter.addWidget(self.main)
        splitter.addWidget(self.right)

        splitter.setSizes([25, 50, 25])

        self.layout().addWidget(splitter)


class BottomFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)
        self.setLayout(hLayout)

        self.left = QFrame()
        self.right = QFrame()

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        self.left.setLayout(left_layout)

        left_layout.addWidget(MinWindow("Log"))

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        self.right.setLayout(right_layout)

        right_layout.addWidget(MinWindow("Transitions Table"))

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left)
        splitter.addWidget(self.right)

        splitter.setSizes([50, 50])

        self.layout().addWidget(splitter)
