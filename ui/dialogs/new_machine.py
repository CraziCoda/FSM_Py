from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class NewMachineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(5, 5, 5, 5)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        self.label = QLabel("New Machine")
        self.label.setStyleSheet("margin: 5px 0; color: #888888; font-family: 'Segoe UI';")

        self.layout().addWidget(self.label, 0)

        self.setStyleSheet("background-color: #eeeeec;")