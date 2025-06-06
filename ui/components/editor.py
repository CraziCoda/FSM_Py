from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QVBoxLayout, QGraphicsEllipseItem, QListWidget, QListWidgetItem, QGraphicsItem
from PyQt5.QtGui import QPainter, QPen, QIcon, QBrush, QColor, QTransform
from PyQt5.QtCore import Qt, QSize, QPoint
from ui.styles.components import tools_list_style
from context.context import AppContext
from context.machine import *
from ui.components.custom.graphics import *


class Editor(QGraphicsView):
    current_machine: Machine = None
    dragged_item: QGraphicsItem = None
    last_pos_dragged_item: QPoint = None
    drag_offset: QPoint = None

    max_zoom = 1
    min_zoom = 0.5
    zoom_factor = 1
    zoom_step = 0.01

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setSceneRect(-1000, -1000, 2000, 2000)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setStyleSheet("background-color: #dddddd;")

        self.add_dot_grid()

        AppContext().set_handler("selected_tool", lambda: self.change_cursor())
        AppContext().set_handler("selected_machine", lambda: self.load_machine())

        self.scale(self.zoom_factor, self.zoom_factor)

    def add_dot(self, x, y, radius=2, color="#000000"):
        dot = QGraphicsEllipseItem(
            x - radius, y - radius, radius * 2, radius * 2)
        dot.setBrush(QBrush(QColor(color)))
        dot.setPen(QPen(Qt.PenStyle.NoPen))
        self.scene.addItem(dot)

    def add_dot_grid(self, radius=2):
        for x in range(-1000, 1000, 50):
            for y in range(-1000, 1000, 50):
                self.add_dot(x, y, radius, "#aaaaaa")

    def add_state(self, x, y):
        if not self.current_machine:
            return

        state = State(f"q{len(self.current_machine.states)}", [x, y])

        item = GraphicsNormalStateItem(state.name, self)
        item.setPos(x - item.width / 2, y - item.height / 2)
        self.scene.addItem(item)
        state.set_drawn_item(item)
        self.current_machine.add_state(state)

        AppContext().save_machine()

    def change_cursor(self):
        selected_tool = AppContext().selected_tool

        if selected_tool == "move":
            self.setCursor(Qt.CursorShape.OpenHandCursor)

        if selected_tool == "add_state":
            self.setCursor(Qt.CursorShape.CrossCursor)

        if selected_tool == "zoom":
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)

    def load_machine(self):
        self.current_machine = AppContext().selected_machine

        self.scene.clear()
        self.add_dot_grid()

        for state in self.current_machine.states:
            if state.initial:
                item = GraphicsInputStateItem(state.name, self)
                item.setPos(state.location[0], state.location[1])
                state.set_drawn_item(item)
                self.scene.addItem(item)
            elif state.accepting:
                item = GraphicsOutputStateItem(state.name, self)
                item.setPos(state.location[0], state.location[1])
                state.set_drawn_item(item)
                self.scene.addItem(item)
            else:
                item = GraphicsNormalStateItem(state.name, self)
                item.setPos(state.location[0], state.location[1])
                state.set_drawn_item(item)
                self.scene.addItem(item)

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "add_state":
            self.add_state(pos.x(), pos.y())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "move":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())

            if not item:
                pass
            elif item.__class__.__name__ == "QGraphicsTextItem":
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.dragged_item = item.parentItem()
                self.drag_offset = event.screenPos() - item.parentItem().pos()
            elif item:
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.dragged_item = item
                self.drag_offset = event.screenPos() - item.pos()
            else:
                self.dragged_item = None

    def mouseMoveEvent(self, event):
        if self.dragged_item:
            pos = event.screenPos() - self.drag_offset
            self.dragged_item.setPos(pos)

            for state in self.current_machine.states:
                if state.get_drawn_item() == self.dragged_item:
                    state.location = [pos.x(), pos.y()]

            AppContext().save_machine()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.change_cursor()
            self.dragged_item = None

    def wheelEvent(self, event):
        if AppContext().selected_tool == "zoom":
            if event.angleDelta().y() > 0:
                self.scale(1.05, 1.05)
            else:
                self.scale(0.95, 0.95)

            return

        return super().wheelEvent(event)


class ToolBar(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)

        icons = [
            "assets/tools/cursor.png",
            "assets/tools/plus.png",
            "assets/tools/nodes.png",
            "assets/tools/check-mark.png",
            "assets/tools/scissors.png",
            "assets/tools/recycle-bin.png",
            "assets/tools/loupe.png",
        ]
        tooltips = [
            "Move",
            "Add State",
            "Add Transition",
            "Accept State",
            "Remove Transition",
            "Remove State",
            "Zoom"
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
            item.setToolTip(tooltips[i])
            self.tools_list.addItem(item)
            if i == 0:
                self.tools_list.setCurrentItem(item)

        vLayout.addWidget(self.tools_list, 0)

        self.tools_list.setStyleSheet(tools_list_style)

        self.setStyleSheet("background-color: #ffffff; padding: 5px 0;")
        vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(vLayout)

        def handle_item_click(item: QListWidgetItem):
            tool_selected = item.toolTip()

            if tool_selected == "Move":
                AppContext().set_selected_tool("move")
            elif tool_selected == "Add State":
                AppContext().set_selected_tool("add_state")
            elif tool_selected == "Add Transition":
                AppContext().set_selected_tool("add_transition")
            elif tool_selected == "Accept State":
                AppContext().set_selected_tool("accept_state")
            elif tool_selected == "Remove Transition":
                AppContext().set_selected_tool("remove_transition")
            elif tool_selected == "Remove State":
                AppContext().set_selected_tool("remove_state")
            elif tool_selected == "Zoom":
                AppContext().set_selected_tool("zoom")
            else:
                AppContext().set_selected_tool("move")

        self.tools_list.itemClicked.connect(handle_item_click)
