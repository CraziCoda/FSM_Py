from PyQt5.QtWidgets import QGraphicsEllipseItem


class State:
    name = ""
    initial = False
    location = [0, 0]
    _drawn_item: QGraphicsEllipseItem = None


    def __init__(self, name, location, initial=False):
        self.name = name
        self.initial = initial
        self.location = location

    def set_drawn_item(self, item: QGraphicsEllipseItem):
        self._drawn_item = item

    def get_drawn_item(self):
        return self._drawn_item


class Transition:
    source = ""
    target = ""
    symbol = ""

    def __init__(self, source, target, symbol):
        self.source = source
        self.target = target
        self.symbol = symbol


class Machine:

    def __init__(self, name, type, initial_state: State = None):
        self.name = name
        self._type = type
        self.states: list[State] = []
        self.transitions: list[Transition] = []

        if initial_state:
            self.states.append(initial_state)

    def add_state(self, state: State):
        self.states.append(state)

    def __str__(self):
        return f"Machine: {self.name} ({self._type}) with {len(self.states)} states"