from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QScrollArea, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SimulationWin(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(5, 5, 5, 5)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        # Header
        header_frame = QFrame()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)
        header_frame.setLayout(header_layout)

        label_style = "margin: 5px 0; color: #888888; font-family: 'Segoe UI'; font-size: 14px; font-weight: 500;"

        input_name = QLabel("Input")
        input_name.setStyleSheet(label_style)

        steps_label = QLabel("Step: 2 / 10")
        steps_label.setStyleSheet(label_style)
        steps_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        header_layout.addWidget(input_name)
        header_layout.addWidget(steps_label)

        # Main
        main_frame = QFrame()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_frame.setLayout(main_layout)


        # output 
        output_frame = QFrame()
        output_layout = QHBoxLayout()
        output_layout.setContentsMargins(0, 0, 0, 0)
        output_layout.setSpacing(0)
        output_frame.setLayout(output_layout)

        output_label = QLabel("Output: ")
        output_value = QLabel("Accepted")

        output_label.setStyleSheet(label_style)
        output_value.setStyleSheet(label_style + " color: #000000;")

        output_frame.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)

        output_layout.addWidget(output_label, 0)
        output_layout.addWidget(output_value, 0)


        # controls
        controls_frame = QFrame()
        controls_layout = QHBoxLayout()
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(0)
        controls_frame.setLayout(controls_layout)

        stop_button = QPushButton()
        stop_button.setIcon(QIcon("assets/icons/stop.png"))

        play_button = QPushButton()
        play_button.setIcon(QIcon("assets/icons/play.png"))

        next_button = QPushButton()
        next_button.setIcon(QIcon("assets/icons/next.png"))

        controls_layout.addWidget(stop_button)
        controls_layout.addWidget(play_button)
        controls_layout.addWidget(next_button)



        main_frame.setStyleSheet("background-color: #ffffff;")
        self.layout().addWidget(header_frame, 0)
        self.layout().addWidget(main_frame, 1)
        self.layout().addWidget(output_frame, 0)
        self.layout().addWidget(controls_frame, 0)




        