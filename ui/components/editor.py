from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem
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
            "assets/tools/check-mark.png",
            "assets/tools/recycle-bin.png",
            "assets/tools/loupe.png",
        ]

        self.tools_list = QListWidget()
        self.tools_list_layout = QVBoxLayout()
        self.tools_list_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_list.setSpacing(5)
        self.tools_list.setFixedWidth(40)
        self.tools_list.setLayout(self.tools_list_layout)
        self.tools_list.setFlow(QListWidget.Flow.TopToBottom)
        self.tools_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.tools_list.setIconSize(QSize(20, 20))
        self.tools_list.setMovement(QListWidget.Movement.Static)

        # self.tools_list.addItems(icons)
        for i, icon in enumerate(icons):
            item = QListWidgetItem()
            item.setIcon(QIcon(icon))
            self.tools_list.addItem(item)
            if i == 0:
                self.tools_list.setCurrentItem(item)

        vLayout.addWidget(self.tools_list, 0)

        self.setStyleSheet("background-color: #ffffff; padding: 5px 0;")
        vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(vLayout)
