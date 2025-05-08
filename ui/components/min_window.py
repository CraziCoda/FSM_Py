from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFrame, QLabel, QSizePolicy
from PyQt5.QtCore import Qt

class MinWindow(QWidget):
    def __init__(self, name: str = ""):
        super().__init__()

        self.name = name

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        self.label = QLabel(self.name)
        self.label.setSizePolicy(QLabel().sizePolicy())

        self.main = QFrame()
        self.main.setFrameShape(QFrame.StyledPanel)

        self.layout().addWidget(self.label, 0)
        self.layout().addWidget(self.main, 1)