from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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
        icons_frame_layout.setContentsMargins(0, 0, 0, 0)
        icons_frame.setLayout(icons_frame_layout)

        new_machine_button = QPushButton()
        new_machine_button.setIcon(QIcon("assets/icons/add.png"))

        delete_machine_button = QPushButton()
        delete_machine_button.setIcon(QIcon("assets/icons/delete.png"))

        open_world_button = QPushButton()
        open_world_button.setIcon(QIcon("assets/icons/open-folder.png"))

        clear_world_button = QPushButton()
        clear_world_button.setIcon(QIcon("assets/icons/broom.png"))

        icons_frame_layout.addWidget(new_machine_button)
        icons_frame_layout.addWidget(delete_machine_button)

        icons_frame_layout.addWidget(open_world_button)
        icons_frame_layout.addWidget(clear_world_button)

        world_name = QLabel("Just a world")
        world_name.setStyleSheet("font-weight: 500; font-family: 'Segoe UI'; font-size: 14px; border: 1px solid #aaaacc; border-bottom: 1px groove #dddddd; background-color: #ffffff; padding: 5px;")

        worlds_frame = QFrame()
        worlds_frame_layout = QVBoxLayout()
        worlds_frame_layout.setContentsMargins(0, 0, 0, 0)
        worlds_frame_layout.setSpacing(0)
        worlds_frame.setLayout(worlds_frame_layout)

        worlds_sample = ["Microwave", "Traffic Light", "Washing Machine", "Light Switch", "Door"]
        i = 0

        for world in worlds_sample:
            world_label = QLabel(world)
            style = "font-weight: 400; font-family: 'Segoe UI'; font-size: 14px; border: none; border-bottom: 1px groove #dddddd; padding: 5px 5px;"
            if i % 2 == 0:
                style += "background-color: #eeeeec;"
            else:
                style += "background-color: #ffffff;"
            
            world_label.setStyleSheet(style)

            world_label.setMaximumHeight(30)
            world_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            worlds_frame_layout.addWidget(world_label, 0)            
            i += 1

        worlds_frame.setStyleSheet("background-color: #ffffff; border: 1px solid #aaaacc; border-top: none;")
        worlds_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidget(worlds_frame)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: #ffffff;")


        self.layout().addWidget(icons_frame, 0)
        self.layout().addWidget(world_name, 0)
        self.layout().addWidget(scroll, 1)
        