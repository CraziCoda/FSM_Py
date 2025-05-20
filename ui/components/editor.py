from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QVBoxLayout, QListWidget, QListWidgetItem
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
        
        icons = ["assets/tools/plus.png", "assets/tools/nodes.png", "assets/tools/tick-mark.png"]


        self.setLayout(vLayout)