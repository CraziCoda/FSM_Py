from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFrame, QLabel, QSizePolicy
from PyQt5.QtCore import Qt

class MinWindow(QWidget):
    def __init__(self, name: str = "",content: QWidget = None,  bg_color: str = "#eeeeec"):
        super().__init__()

        self.name = name
        self.bg_color = bg_color
        if content is None:
            self.main = QFrame()
        else:
            self.main = content

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        self.label = QLabel(self.name)
        self.label.setSizePolicy(QLabel().sizePolicy())

        self.layout().addWidget(self.label, 0)
        self.layout().addWidget(self.main, 1)

        self.setStyleSheet(f"background-color: {self.bg_color}; padding: 5px;")