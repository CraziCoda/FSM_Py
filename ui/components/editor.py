from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget,
                             QVBoxLayout, QGraphicsEllipseItem, QListWidget, QListWidgetItem, QGraphicsItem,
                             QLineEdit)
from PyQt5.QtGui import QPainter, QPen, QIcon, QBrush, QColor, QCursor, QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize, QPoint, QLineF, QPointF
from ui.styles.components import tools_list_style
from context.context import AppContext
from context.machine import *
from ui.components.custom.graphics import *
from ui.components.properties_win import PropertiesWin
from ui.components.popups.obj_props import *

class Editor(QGraphicsView):
    current_machine: Machine = None
    dragged_item: QGraphicsItem = None
    last_pos_dragged_item: QPoint = None
    drag_offset: QPoint = None
    adding_transition_line: QGraphicsLineItem = None
    starting_state_transition: State = None

    zoom_factor = 1
    zoom_step = 0.01

    def __init__(self):
        super().__init__()

        self.scene: QGraphicsScene = QGraphicsScene()
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

        if self.current_machine.add_state(state):
            item = GraphicsNormalStateItem(state.name, self)
            item.setPos(x - item.width / 2, y - item.height / 2)
            self.scene.addItem(item)
            state.set_drawn_item(item)

        AppContext().save_machine()

    def change_cursor(self):
        selected_tool = AppContext().selected_tool

        if self.adding_transition_line and selected_tool != "add_transition":
            self.scene.removeItem(self.adding_transition_line)
            self.adding_transition_line = None

        if selected_tool == "move":
            self.setCursor(Qt.CursorShape.OpenHandCursor)

        if selected_tool == "add_state":
            self.setCursor(Qt.CursorShape.CrossCursor)

        if selected_tool == "add_transition":
            self.setCursor(Qt.CursorShape.PointingHandCursor)

        if selected_tool == "accept_state":
            self.setCursor(Qt.CursorShape.CrossCursor)

        if selected_tool == "remove_transition":
            transform = QTransform().rotate(-45)
            pixmap = QPixmap("assets/tools/scissors.png")\
                .scaled(20, 20).transformed(transform, mode=Qt.TransformationMode.SmoothTransformation)
            cursor = QCursor(pixmap, 10, 10)
            self.setCursor(cursor)

        if selected_tool == "remove_state":
            pixmap = QPixmap("assets/tools/bin-close.png")\
                .scaled(20, 20)
            cursor = QCursor(pixmap, 10, 10)
            self.setCursor(cursor)

        if selected_tool == "zoom":
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)

    def load_machine(self):
        self.current_machine = AppContext().selected_machine

        self.scene.clear()
        self.add_dot_grid()

        for state in self.current_machine.states:
            if state.initial and not state.accepting:
                item = GraphicsInputStateItem(state.name, self)
                item.setPos(state.location[0], state.location[1])
                state.set_drawn_item(item)
                self.scene.addItem(item)

            elif state.accepting and state.initial:
                item = GraphicsAcceptedInputStateItem(state.name, self)
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

        paired_states: list = []
        for i, state in enumerate(self.current_machine.states):
            for j in range(i + 1, len(self.current_machine.states)):
                other_state = self.current_machine.states[j]
                paired_states.append((state, other_state))

        parallel_transitions: list[list[Transition]] = []
        for i in range(len(paired_states)):
            parallel_transitions.append([])

        for transition in self.current_machine.transitions:
            for i, paired_state in enumerate(paired_states):
                if (transition.source == paired_state[0] or transition.target == paired_state[0]) and (transition.source == paired_state[1] or transition.target == paired_state[1]):
                    parallel_transitions[i].append(transition)

        for parallel_transition_group in parallel_transitions:
            num_parallel_transitions = len(parallel_transition_group)
            start_index = 0
            if num_parallel_transitions > 1:
                start_index = -(num_parallel_transitions // 2)

            for transition in parallel_transition_group:
                line = GraphicsTransitionItem(
                    transition, control_value=start_index, parent=self.scene)
                self.scene.addItem(line)

                transition.set_drawn_item(line)

                start_index += 1
                if num_parallel_transitions % 2 == 0 and start_index == 0:
                    start_index += 1
        self.scene.update()
        self.load_props_to_window()

    def get_state_from_item(self, item: QGraphicsItem) -> State | None:
        for state in self.current_machine.states:
            if state.get_drawn_item() == item:
                return state
        return None

    def get_transition_from_item(self, item: QGraphicsItem) -> Transition | None:
        for transition in self.current_machine.transitions:
            if transition.get_drawn_item() == item:
                return transition
        return None

    def remove_state(self, state: State):
        transitions = self.current_machine.transitions.copy()

        for transtion in transitions:
            if state in [transtion.source, transtion.target]:
                self.current_machine.transitions.pop(
                    self.current_machine.transitions.index(transtion))

        try:
            self.current_machine.states.pop(
                self.current_machine.states.index(state))
        except:
            pass

        AppContext().save_machine()

    def load_props_to_window(self):
        if self.current_machine.selected_item:
            props_win: PropertiesWin = AppContext().props_window

            props = []

            if self.current_machine.selected_item.__class__.__name__ == "State":
                props.append({
                    "name": "Name",
                    "value": self.current_machine.selected_item.name,
                    "type": "str"
                })
                props.append({
                    "name": "Is initial",
                    "value": str(self.current_machine.selected_item.initial),
                    "type": "switch"
                })
                props.append({
                    "name": "Is accepting",
                    "value": str(self.current_machine.selected_item.accepting),
                    "type": "switch"
                })
                props.append({
                    "name": "Output",
                    "value": self.current_machine.selected_item.output,
                    "type": "str"
                })
            elif self.current_machine.selected_item.__class__.__name__ == "Transition":
                props.append({
                    "name": "Name",
                    "value": self.current_machine.selected_item.name,
                    "type": "str"
                })
                props.append({
                    "name": "Source",
                    "value": self.current_machine.selected_item.source.name,
                    "type": "str"
                })
                props.append({
                    "name": "Target",
                    "value": self.current_machine.selected_item.target.name,
                    "type": "str"
                })
                props.append({
                    "name": "Output",
                    "value": self.current_machine.selected_item.output,
                    "type": "str"
                })
            props_win.load_props(props)

    def select_item(self, item: GraphicsInputStateItem | GraphicsAcceptedInputStateItem | GraphicsNormalStateItem | GraphicsOutputStateItem | GraphicsTransitionItem):
        if not self.current_machine:
            return
        previous_item = self.current_machine.selected_item

        for state in self.current_machine.states:
            if state.get_drawn_item() == item:
                self.current_machine.selected_item = state
                break

        for transition in self.current_machine.transitions:
            if transition.get_drawn_item() == item:
                self.current_machine.selected_item = transition
                break

        # print(previous_item, self.current_machine.selected_item)
        if previous_item and previous_item.get_drawn_item():
            previous_item.get_drawn_item().unmarkAsSelected()

        if item:
            item.markAsSelected()

        self.load_props_to_window()

    def mousePressEvent(self, event):
        pos = self.mapToScene(event.pos())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "add_state":
            self.add_state(pos.x(), pos.y())

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "move":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())

            if not item or "Transition" in item.__class__.__name__:
                self.dragged_item = None
                self.select_item(item)
            elif item.__class__.__name__ == "QGraphicsTextItem":
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.dragged_item = item.parentItem()
                self.drag_offset = event.screenPos() - item.parentItem().pos()
                self.select_item(item.parentItem())
            elif item:
                self.setCursor(Qt.CursorShape.ClosedHandCursor)
                self.dragged_item = item
                self.drag_offset = event.screenPos() - item.pos()
                self.select_item(item)
            else:
                self.dragged_item = None

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "add_transition":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())
            screen_pos = self.mapToScene(event.pos())

            if self.adding_transition_line:
                if item.__class__.__name__.startswith("Graphics") and self.starting_state_transition:
                    target_state = self.get_state_from_item(item)

                    if target_state:
                        transition_name = f"t{len(self.current_machine.transitions)}"
                        transition = Transition(
                            self.starting_state_transition, target_state, transition_name)
                        self.current_machine.add_transition(transition)

                        line = GraphicsTransitionItem(
                            transition, parent=self.scene)
                        self.scene.addItem(line)

                        AppContext().save_machine()

                elif item.__class__.__name__ == "QGraphicsTextItem" and self.starting_state_transition:
                    target_state = self.get_state_from_item(item.parentItem())

                    if target_state:
                        transition_name = f"t{len(self.current_machine.transitions)}"
                        transition = Transition(
                            self.starting_state_transition, target_state, transition_name)
                        self.current_machine.add_transition(transition)

                        line = GraphicsTransitionItem(
                            transition, parent=self.scene)
                        self.scene.addItem(line)

                        AppContext().save_machine()

                self.scene.removeItem(self.adding_transition_line)
                self.adding_transition_line = None
                self.scene.update()

                self.load_machine()
                return

            if not item:
                pass
            elif item.__class__.__name__ == "QGraphicsTextItem":
                pos = item.parentItem().pos() + QPointF(item.parentItem().width / 2,
                                                        item.parentItem().height / 2)

                self.adding_transition_line = self.scene\
                    .addLine(QLineF(pos, screen_pos))

                self.starting_state_transition = self\
                    .get_state_from_item(item.parentItem())

            elif item.__class__.__name__.startswith("Graphics"):
                pos = item.pos() + QPointF(item.width / 2,
                                           item.height / 2)

                self.adding_transition_line = self.scene\
                    .addLine(QLineF(pos, screen_pos))

                self.starting_state_transition = self\
                    .get_state_from_item(item)
            else:
                pass

            self.scene.update()

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "accept_state":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())
            screen_pos = self.mapToScene(event.pos())

            if item.__class__.__name__.startswith("Graphics"):
                state = self.get_state_from_item(item)

                if state:
                    state.accepting = not state.accepting

            elif item.__class__.__name__ == "QGraphicsTextItem":
                state = self.get_state_from_item(item.parentItem())

                if state:
                    state.accepting = not state.accepting

            AppContext().save_machine()
            self.load_machine()

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "remove_transition":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())

            if item.__class__.__name__ == "GraphicsTransitionItem":
                transition = self.get_transition_from_item(item)

                if transition:
                    transform = QTransform().rotate(-45)
                    pixmap = QPixmap("assets/tools/scissors-close.png")\
                        .scaled(20, 20).transformed(transform, mode=Qt.TransformationMode.SmoothTransformation)
                    cursor = QCursor(pixmap, 10, 10)
                    self.setCursor(cursor)

                    self.current_machine.transitions.pop(
                        self.current_machine.transitions.index(transition))
                    self.scene.removeItem(item)
                    AppContext().save_machine()
                    self.load_machine()

        if event.button() == Qt.MouseButton.LeftButton and AppContext().selected_tool == "remove_state":
            item = self.scene.itemAt(pos, self.scene.views()[0].transform())

            if item.__class__.__name__.startswith("Graphics"):
                state = self.get_state_from_item(item)

                if state and state.initial == False:
                    pixmap = QPixmap("assets/tools/bin-open.png")\
                        .scaled(20, 20)
                    cursor = QCursor(pixmap, 10, 10)
                    self.setCursor(cursor)

                    self.remove_state(state)
                    self.load_machine()

    def mouseMoveEvent(self, event):
        if self.dragged_item and self.current_machine:
            pos = event.screenPos() - self.drag_offset
            self.dragged_item.setPos(pos)

            dragged_state = self.get_state_from_item(self.dragged_item)
            if dragged_state:
                dragged_state.set_location([pos.x(), pos.y()])

            AppContext().save_machine()

        if self.adding_transition_line:
            pos = self.mapToScene(event.pos()) - QPointF(3, 3)
            self.adding_transition_line.setLine(
                QLineF(self.adding_transition_line.line().p1(), pos))

        self.scene.update()

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
    

    def mouseDoubleClickEvent(self, event):
        pos = self.mapToScene(event.pos())
        item = self.scene.itemAt(pos, self.scene.views()[0].transform())
        main_window = AppContext().main_window

        if item.__class__.__name__.startswith("Graphics"):
            state = self.get_state_from_item(item)
            if state:
                popup = StatePropertiesPopup(main_window)
                popup.exec()

        elif item.__class__.__name__ == "QGraphicsTextItem":
            state = self.get_state_from_item(item.parentItem())

            if state:
                pass


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
