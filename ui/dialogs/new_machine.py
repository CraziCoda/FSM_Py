from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox
import json
from context.context import AppContext
import os
from context.defaults import DEFAULT_MACHINE


class NewMachineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(5, 5, 5, 5)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        self.setWindowTitle("New Machine")

        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(0)

        gridLayout.addWidget(QLabel("Name:"), 0, 0)
        gridLayout.addWidget(QLabel("Type:"), 1, 0)

        self.name_input = QLineEdit()
        self.type_input = QComboBox()

        self.type_input.addItems(["Moore", "Mealy"])


        gridLayout.addWidget(self.name_input, 0, 1)
        gridLayout.addWidget(self.type_input, 1, 1)

        self.layout().addLayout(gridLayout, 1)
        

        self.create_button = QPushButton("Create")
        self.create_button.setStyleSheet("margin: 5px 0; color: #888888; font-family: 'Segoe UI';")

        self.create_button.clicked.connect(lambda: self.create_new_machine())

        self.layout().addWidget(self.create_button, 2)

        self.setStyleSheet("background-color: #eeeeec;")

    def create_new_machine(self):
        name = self.name_input.text() + ".fsm"
        type = self.type_input.currentText()

        if name == "":
            QMessageBox.critical(self, "Error", "Please enter a name")
            return
        
        default = DEFAULT_MACHINE.copy()
        default["name"] = name
        default["type"] = type

        
        world = AppContext().settings.value("world_folder")
        
        try:
            path = os.path.join(world, name)
            if os.path.exists(path):
                QMessageBox.critical(self, "Error", "Machine already exists")
                return
            with open(path, "w") as f:
                f.write(json.dumps(default))
        except:
            QMessageBox.critical(self, "Error", "Error creating machine")
            return

        self.accept()