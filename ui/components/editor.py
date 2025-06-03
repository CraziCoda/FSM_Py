from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QVBoxLayout, QGraphicsEllipseItem, QListWidget, QListWidgetItem, QGraphicsItem
from PyQt5.QtGui import QPainter, QPen, QIcon, QBrush, QColor, QTransform
from PyQt5.QtCore import Qt, QSize, QPoint
from ui.styles.components import tools_list_style
from context.context import AppContext
from context.machine import *


class Editor(QGraphicsView):
    current_machine: Machine = Machine()
    dragged_item: QGraphicsItem = None
    last_pos_dragged_item: QPoint = None
    drag_offset: QPoint = None

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setSceneRect(-1000, -1000, 2000, 2000)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setStyleSheet("background-color: #dddddd;")

        self.add_dot_grid()

        AppContext().set_handler("selected_tool", lambda: self.change_cursor())

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
        radius = 50
        item = QGraphicsEllipseItem(
            x - radius, y - radius, radius * 2, radius * 2)
        item.setBrush(QBrush(QColor("#4cadfc")))
        self.scene.addItem(item)

        state = State(f"q{len(self.current_machine.states)}", "moore", [x, y], True)
        state.set_drawn_item(item)
        self.current_machine.add_state(state)

    def change_cursor(self):
        selected_tool = AppContext().selected_tool

        if selected_tool == "move":
            self.setCursor(Qt.CursorShape.OpenHandCursor)
        
        if selected_tool == "add_state":
            self.setCursor(Qt.CursorShape.CrossCursor)

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "add_state":
            self.add_state(pos.x(), pos.y())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "move":
            item  = self.scene.itemAt(pos, self.scene.views()[0].transform())

            if item:
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.dragged_item = item
                self.drag_offset = event.screenPos() - item.pos()
            else:
                self.dragged_item = None

    def mouseMoveEvent(self, event):
        if self.dragged_item:
            pos = event.screenPos() - self.drag_offset
            self.dragged_item.setPos(pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.change_cursor()
            self.dragged_item = None


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
