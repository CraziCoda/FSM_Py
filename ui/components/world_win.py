from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton, QListWidget
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt, QSettings
from ui.styles.components import world_list_style
from context.context import AppContext
from ui.dialogs.new_machine import NewMachineDialog

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
        new_machine_button.clicked.connect(lambda: self.create_new_machine())

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

        world_list = QListWidget()
        world_list_layout = QVBoxLayout()
        world_list_layout.setContentsMargins(0, 0, 0, 0)
        world_list_layout.setSpacing(0)
        world_list.setLayout(world_list_layout)

        worlds_sample = ["Microwave", "Traffic Light", "Washing Machine", "Light Switch", "Door"]
        world_list.addItems(worlds_sample)

        world_list.setStyleSheet(world_list_style)

        world_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidget(world_list)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: #ffffff;")


        self.layout().addWidget(icons_frame, 0)
        self.layout().addWidget(world_name, 0)
        self.layout().addWidget(scroll, 1)

    def create_new_machine(self):
        main_window = AppContext().main_window

        dialog = NewMachineDialog(main_window)
        dialog.exec()
                