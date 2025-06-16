from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush, QColor, QPixmap, QPainterPath, QPainterPathStroker
from PyQt5.QtCore import QRectF, Qt, QPointF
from context.machine import State, Transition
import math


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

        painter.drawPixmap(-self.arrow.width(),
                           int(self.arrow.height() / 2) + 3, self.arrow)


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

class GraphicsAcceptedInputStateItem(QGraphicsItem):
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

        painter.drawPixmap(-self.arrow.width(),
                           int(self.arrow.height() / 2) + 3, self.arrow)
        
        # inner rect
        painter.setPen(QPen(Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(QColor("#f0f0f0")))
        painter.drawRoundedRect(5, 5, self.width - 10,
                                self.height - 10, 10, 10)

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
        painter.drawRoundedRect(5, 5, self.width - 10,
                                self.height - 10, 10, 10)


class GraphicsTransitionItem(QGraphicsItem):
    def __init__(self, transition: Transition, control_value: int = 0, parent: QGraphicsScene = None):
        super().__init__()
        self.transition = transition

        self.start_state = transition.source
        self.end_state = transition.target

        self.pen = QPen(Qt.GlobalColor.blue, 2)

        self.source_item = transition.source.get_drawn_item()
        self.target_item = transition.target.get_drawn_item()

        self.source = self.source_item.scenePos() + QPointF(self.source_item.width / 2,
                                                            self.source_item.height / 2)

        self.target = self.target_item.scenePos() + QPointF(self.target_item.width / 2,
                                                            self.target_item.height / 2)

        self.setZValue(-1)
        self.start_state.add_handle(self.update_pos)
        self.end_state.add_handle(self.update_pos)

        self.control_value = control_value

    def boundingRect(self):
        path = QPainterPath(self.source)
        control_point = self.find_control_point()

        path.quadTo(control_point, self.target)

        return path.boundingRect().adjusted(-5, -5, 5, 5)
        

    def paint(self, painter, option, widget=...):
        path = QPainterPath(self.source)
        control_point = self.find_control_point()

        path.quadTo(control_point, self.target)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setPen(self.pen)
        
        painter.drawPath(path)

    def shape(self):
        stroker = QPainterPathStroker()
        stroker.setWidth(self.pen.widthF() + 10)  # +2 to allow a bit of room for clicking
        return stroker.createStroke(self._make_path())
    
    def _make_path(self):
        path = QPainterPath(self.source)
        control_point = self.find_control_point()

        path.quadTo(control_point, self.target)
        return path

    def find_control_point(self):
        control = 100 * self.control_value

        mid_x = (self.source.x() + self.target.x()) / 2
        mid_y = (self.source.y() + self.target.y()) / 2

        mid_point = QPointF(mid_x, mid_y)

        dx = abs(self.target.x() - self.source.x())
        dy = abs(self.target.y() - self.source.y())

        length = math.hypot(dx, dy)

        if length == 0:
            mid_point

        perp_dx = -dy / length
        perp_dy = dx / length

        return QPointF(mid_point.x() + (perp_dx * control), mid_point.y() + (perp_dy * control))

    def update_pos(self):
        source_item = self.transition.source.get_drawn_item()
        target_item = self.transition.target.get_drawn_item()

        try: 
            self.source = source_item.scenePos() + QPointF(target_item.width / 2,
                                                        target_item.height / 2)

            self.target = target_item.scenePos() + QPointF(target_item.width / 2,
                                                        target_item.height / 2)
        except RuntimeError:
            pass