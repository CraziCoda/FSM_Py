from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel

class WorldWin(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    
    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        icons_frame = QFrame()
        icons_frame_layout = QHBoxLayout()
        icons_frame_layout.setContentsMargins(5, 5, 5, 5)
        icons_frame.setLayout(icons_frame_layout)

        world_name = QLabel("Just a world")

        worlds_frame = QFrame()
        worlds_frame_layout = QVBoxLayout()
        worlds_frame.setLayout(worlds_frame_layout)

        worlds_frame.setStyleSheet("background-color: #ffffff; border: 1px solid #222222;")


        self.layout().addWidget(icons_frame, 0)
        self.layout().addWidget(world_name, 0)
        self.layout().addWidget(worlds_frame, 1)

        