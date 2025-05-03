from PyQt6.QtWidgets import QHBoxLayout, QPushButton
class BottomLayout:
    bottom_layout: QHBoxLayout | None = None
    def __init__(self):
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)

        self.bottom_layout.addWidget(QPushButton("Run 2"))

    
    def get_layout(self) -> QHBoxLayout:
        return self.bottom_layout
