from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton, QListWidget, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt, QSettings
from ui.styles.components import world_list_style
from context.context import AppContext
from ui.dialogs.new_machine import NewMachineDialog
from actions.file import open_folder
import os

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
        delete_machine_button.clicked.connect(lambda: self.delete_machine())

        open_world_button = QPushButton()
        open_world_button.setIcon(QIcon("assets/icons/open-folder.png"))
        open_world_button.clicked.connect(lambda: open_folder(self))

        clear_world_button = QPushButton()
        clear_world_button.setIcon(QIcon("assets/icons/broom.png"))
        clear_world_button.clicked.connect(lambda: self.clear_world())

        icons_frame_layout.addWidget(new_machine_button)
        icons_frame_layout.addWidget(delete_machine_button)

        icons_frame_layout.addWidget(open_world_button)
        icons_frame_layout.addWidget(clear_world_button)

        world_name: str | None = AppContext().settings.value("world_folder")

        if world_name == None:
            world_name = "Open a world"
        else:
            world_name = os.path.basename(world_name)

        world_name = QLabel(world_name)
        world_name.setStyleSheet("font-weight: 500; font-family: 'Segoe UI'; font-size: 14px; border: 1px solid #aaaacc; border-bottom: 1px groove #dddddd; background-color: #ffffff; padding: 5px;")

        self.world_list = QListWidget()
        self.world_list_layout = QVBoxLayout()
        self.world_list_layout.setContentsMargins(0, 0, 0, 0)
        self.world_list_layout.setSpacing(0)
        self.world_list.setLayout(self.world_list_layout)

        AppContext().set_handler("machines", self.update_world_list)
        AppContext().set_handler("world_name", lambda: world_name.setText(AppContext().world_name))

        worlds_sample = AppContext().machines
        self.world_list.addItems(worlds_sample)

        self.world_list.setStyleSheet(world_list_style)

        self.world_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidget(self.world_list)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: #ffffff;")


        self.layout().addWidget(icons_frame, 0)
        self.layout().addWidget(world_name, 0)
        self.layout().addWidget(scroll, 1)

    def create_new_machine(self):
        main_window = AppContext().main_window

        dialog = NewMachineDialog(main_window)
        dialog.exec()

    def update_world_list(self):
        self.world_list.clear()
        self.world_list.addItems(AppContext().machines)

    
    def delete_machine(self):
        _machine = self.world_list.currentItem().text()
        path = os.path.join(AppContext().settings.value("world_folder"), _machine)
        os.remove(path)

    def clear_world(self):
        reply = QMessageBox.question(AppContext().main_window, "Clear World", "Are you sure you want to clear the world?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        
        folder = AppContext().settings.value("world_folder")
        for file in os.listdir(folder):
            if file.endswith(".fsm"):
                path = os.path.join(folder, file)
                os.remove(path)
        
                