from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QDialog
from PyQt5.QtCore import Qt


class StatePropertiesPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        self.main_frame = QFrame()
        self.main_frame_layout = QVBoxLayout()
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(0)
        self.main_frame.setLayout(self.main_frame_layout)

        self.main_frame_layout.addWidget(QLabel("State Properties"))

        self.setLayout(self.main_frame_layout)
        self.setStyleSheet("background-color: #eeeeec;")


class TransitionPropertiesPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        self.main_frame = QFrame()
        self.main_frame_layout = QVBoxLayout()
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(0)
        self.main_frame.setLayout(self.main_frame_layout)

        self.main_frame_layout.addWidget(QLabel("Transition Properties"))

        self.setLayout(self.main_frame_layout)
        self.setStyleSheet("background-color: #eeeeec;")