from PyQt5.QtWidgets import QHBoxLayout, QWidget, QFrame, QSplitter
from PyQt5.QtCore import Qt


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

        self.left.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShape(QFrame.StyledPanel)

        self.left.setMinimumWidth(int(self.width() * 0.25))
        self.main.setMinimumWidth(int(self.width() * 0.5))
        self.right.setMinimumWidth(int(self.width() * 0.25))

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

        self.left.setFrameShape(QFrame.StyledPanel)
        self.right.setFrameShape(QFrame.StyledPanel)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left)
        splitter.addWidget(self.right)

        self.layout().addWidget(splitter)
