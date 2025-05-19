from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Editor(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setStyleSheet("background-color: white;")

        axis_pen = QPen(Qt.GlobalColor.black, 1)

        self.setSceneRect(-self.width() // 2, -self.height() // 2, self.width(), self.height())

        y_axis = QGraphicsLineItem(0, -self.height() // 2, 0, self.height() // 2)
        y_axis.setPen(axis_pen)

        x_axis = QGraphicsLineItem(-self.width() // 2, 0, self.width() // 2, 0)
        x_axis.setPen(axis_pen)

        self.scene.addItem(y_axis)
        self.scene.addItem(x_axis)


    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        print(pos)
