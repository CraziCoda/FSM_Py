from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class LogsWin(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(5, 5, 5, 5)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        logs_frame = QFrame()
        logs_frame_layout = QVBoxLayout()
        logs_frame_layout.setContentsMargins(0, 0, 0, 0)
        logs_frame_layout.setSpacing(0)
        logs_frame.setLayout(logs_frame_layout)

        logs = ["Log 1", "Log 2", "Log 3", "Log 4", "Log 5", "Log 6", "Log 7", "Log 8", "Log 9", "Log 10", "Log 11", "Log 12", "Log 13", "Log 14", "Log 15", "Log 16", "Log 17", "Log 18", "Log 19", "Log 20"]

        for log in logs:
            label = QLabel(log)
            label.setStyleSheet("margin: 5px 0; color: #000000; font-family: Consolas;")
            logs_frame_layout.addWidget(label, 0)

        
        scroll = QScrollArea()
        scroll.setWidget(logs_frame)
        scroll.setWidgetResizable(True)

        self.setStyleSheet(f"background-color: #eeeeec;")

        self.layout().addWidget(scroll, 1)