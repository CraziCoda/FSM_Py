from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush, QColor, QPixmap
from PyQt5.QtCore import QRectF, Qt


class GraphicsInputStateItem(QGraphicsItem):
    def __init__(self, label: str = "", parent=None):
        super().__init__()
        self.height = 70
        self.width = 150
        self.label = label

        self.arrow = QPixmap("assets/pixmap/right-arrow.png")
        self.arrow = self.arrow.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio,
                          Qt.TransformationMode.SmoothTransformation)

        self.text = QGraphicsTextItem(self.label, self)
        self.text.setFont(QFont("Arial", 14))
        self.text.setPos(self.width / 2 - self.text.boundingRect().width() / 2,
                         self.height / 2 - self.text.boundingRect().height() / 2)
        self.text.setDefaultTextColor(QColor("#000000"))

    def boundingRect(self):
        return QRectF(-self.arrow.width(), 0, self.width + self.arrow.width(), self.height)

    def paint(self, painter, option, widget=...):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QPen(Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(QColor("#f0f0f0")))

        painter.drawRoundedRect(0, 0, self.width, self.height, 10, 10)

        painter.drawPixmap(-self.arrow.width(), int(self.arrow.height() / 2) + 3, self.arrow)


class GraphicsNormalStateItem(QGraphicsItem):
    def __init__(self, label: str = "", parent=None):
        super().__init__()
        self.height = 70
        self.width = 150
        self.label = label

        self.text = QGraphicsTextItem(self.label, self)
        self.text.setFont(QFont("Arial", 14))
        self.text.setPos(self.width / 2 - self.text.boundingRect().width() / 2,
                         self.height / 2 - self.text.boundingRect().height() / 2)
        self.text.setDefaultTextColor(QColor("#000000"))

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget=...):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(QPen(Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(QColor("#f0f0f0")))

        painter.drawRoundedRect(0, 0, self.width, self.height, 10, 10)


class GraphicsOutputStateItem(QGraphicsItem):
    def __init__(self, label: str = "", parent=None):
        super().__init__()
        self.height = 70
        self.width = 150
        self.label = label

        self.text = QGraphicsTextItem(self.label, self)
        self.text.setFont(QFont("Arial", 14))
        self.text.setPos(self.width / 2 - self.text.boundingRect().width() / 2,
                         self.height / 2 - self.text.boundingRect().height() / 2)
        self.text.setDefaultTextColor(QColor("#000000"))

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget=...):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # outer rect
        painter.setPen(QPen(Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(QColor("#f0f0f0")))

        painter.drawRoundedRect(0, 0, self.width, self.height, 10, 10)

        # inner rect
        painter.setPen(QPen(Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(QColor("#f0f0f0")))
        painter.drawRoundedRect(5, 5, self.width - 10, self.height - 10, 10, 10)