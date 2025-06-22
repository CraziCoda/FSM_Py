from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QWidget,
                             QFrame, QLabel, QScrollArea, QToolButton, QGroupBox, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ui.styles.components import *


class SimulationWin(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(5, 5, 5, 5)
        vLayout.setSpacing(20)
        self.setLayout(vLayout)

        controls_group_box = QGroupBox("Controls")
        controls_group_box_layout = QHBoxLayout()
        controls_group_box_layout.setContentsMargins(0, 0, 0, 0)
        controls_group_box_layout.setSpacing(0)
        controls_group_box.setLayout(controls_group_box_layout)
        controls_group_box.setStyleSheet(controls_group_box_style)
        controls_group_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        play_button = QToolButton()
        play_button.setIcon(QIcon("assets/icons/play.png"))
        play_button.clicked.connect(lambda: print("play"))
        controls_group_box_layout.addWidget(play_button)
        controls_group_box.setStyleSheet(control_buttons_style)

        stop_button = QToolButton()
        stop_button.setIcon(QIcon("assets/icons/stop.png"))
        stop_button.clicked.connect(lambda: print("stop"))
        stop_button.setDisabled(True)
        controls_group_box_layout.addWidget(stop_button)
        controls_group_box.setStyleSheet(control_buttons_style)

        forward_button = QToolButton()
        forward_button.setIcon(QIcon("assets/icons/next.png"))
        forward_button.setDisabled(True)
        forward_button.clicked.connect(lambda: print("forward"))
        controls_group_box_layout.addWidget(forward_button)
        controls_group_box.setStyleSheet(control_buttons_style)

        start_button = QToolButton()
        start_button.setIcon(QIcon("assets/icons/play-button.png"))
        start_button.setText("Start Simulation")
        start_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        start_button.clicked.connect(lambda: print("start"))
        controls_group_box_layout.addWidget(start_button)

        restart_button = QToolButton()
        restart_button.setIcon(QIcon("assets/icons/play-button.png"))
        restart_button.setText("Restart")
        restart_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        controls_group_box.setStyleSheet(control_buttons_style)
        controls_group_box_layout.addWidget(restart_button)

        input_group_box = QGroupBox("Inputs")
        input_group_box_layout = QVBoxLayout()
        input_group_box_layout.setContentsMargins(0, 0, 0, 0)
        input_group_box_layout.setSpacing(5)
        input_group_box.setLayout(input_group_box_layout)
        input_group_box.setStyleSheet(controls_group_box_style)
        input_group_box_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        load_inputs_button = QToolButton()
        load_inputs_button.setText("Load Inputs")
        load_inputs_button.clicked.connect(lambda: print("Load Inputs"))
        input_group_box.setStyleSheet(control_buttons_style)
        input_group_box_layout.addWidget(load_inputs_button)

        direct_input_layout = QHBoxLayout()
        direct_input_layout.setContentsMargins(0, 0, 0, 0)
        direct_input_layout.setSpacing(0)
        input_group_box_layout.addLayout(direct_input_layout)

        direct_input_label = QLabel("Direct Input: ")
        direct_input_label.setStyleSheet(input_lable_style)
        direct_input_layout.addWidget(direct_input_label)

        direct_input_input = QLineEdit()
        direct_input_input.setPlaceholderText("Press enter to submit")
        direct_input_input.setClearButtonEnabled(True)
        direct_input_input.returnPressed.connect(lambda: direct_input_input.clear())
        direct_input_input.setStyleSheet(input_line_edit_style)
        direct_input_layout.addWidget(direct_input_input)

        added_inputs_layout = QVBoxLayout()
        added_inputs_layout.setContentsMargins(10, 0, 0, 0)
        added_inputs_layout.setSpacing(0)
        input_group_box_layout.addLayout(added_inputs_layout)

        added_inputs_label = QLabel("Added Inputs: ")
        added_inputs_layout.addWidget(added_inputs_label)

        added_inputs_scroll_area = QScrollArea()
        added_inputs_scroll_area.setWidgetResizable(True)
        added_inputs_scroll_area.setWidget(QFrame())
        added_inputs_scroll_area.setStyleSheet(input_scroll_area_style)
        added_inputs_layout.addWidget(added_inputs_scroll_area)


        inputs_buttons_layout = QHBoxLayout()
        inputs_buttons_layout.setContentsMargins(0, 0, 0, 0)
        inputs_buttons_layout.setSpacing(0)
        input_group_box_layout.addLayout(inputs_buttons_layout)

        add_input_button = QToolButton()
        add_input_button.setText("Save Input")
        add_input_button.clicked.connect(lambda: print("Save Input"))
        add_input_button.setStyleSheet(save_button_style)
        inputs_buttons_layout.addWidget(add_input_button)

        remove_input_button = QToolButton()
        remove_input_button.setText("Clear Input")
        remove_input_button.clicked.connect(lambda: print("Clear Input"))
        remove_input_button.setStyleSheet(clear_button_style)
        inputs_buttons_layout.addWidget(remove_input_button)

        self.layout().addWidget(controls_group_box, 0)
        self.layout().addWidget(input_group_box, 0)
        self.layout().setAlignment(Qt.AlignmentFlag.AlignTop)