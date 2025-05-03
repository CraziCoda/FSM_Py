from PyQt6.QtWidgets import QHBoxLayout, QPushButton
class TopLayout:
    top_layout: QHBoxLayout | None = None
    def __init__(self):
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        self.top_layout.addWidget(QPushButton("Run 1"))

    
    def get_layout(self) -> QHBoxLayout:
        return self.top_layout
