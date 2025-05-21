from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QVBoxLayout, QPushButton, QListWidget
from PyQt5.QtGui import QPainter, QPen, QIcon
from PyQt5.QtCore import Qt, QSize


class Editor(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setStyleSheet("background-color: white;")

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        print(pos)


class ToolBar(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)

        icons = [
                    "assets/tools/plus.png",
                    "assets/tools/nodes.png",
                    "assets/tools/scissors.png",
                    "assets/tools/tick-mark.png",
                    "assets/tools/delete.png",
                    "assets/tools/loupe.png",
                ]
        # self.add_state_button = QPushButton()
        # self.add_state_button.setIcon(QIcon("assets/tools/plus.png"))

        # self.add_event_button = QPushButton()
        # self.add_event_button.setIcon(QIcon("assets/tools/nodes.png"))

        # vLayout.addWidget(self.add_state_button)
        # vLayout.addWidget(self.add_event_button)

        self.tools_list = QListWidget()
        self.tools_list_layout = QVBoxLayout()
        self.tools_list_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_list_layout.setSpacing(0)
        self.tools_list.setLayout(self.tools_list_layout)

        self.tools_list.addItems(icons)

        vLayout.addWidget(self.tools_list, 0)

        self.setStyleSheet("background-color: #ffffff; margin: 0;")
        vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(vLayout)
