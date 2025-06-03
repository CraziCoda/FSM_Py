from PyQt5.QtWidgets import QGraphicsEllipseItem


class State:
    name = ""
    _type = "moore"
    initial = False
    location = [0, 0]
    _drawn_item: QGraphicsEllipseItem = None


    def __init__(self, name, type, location, initial=False):
        self.name = name
        self._type = type
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
    _type = ""
    states: list[State] = []
    transitions: list[Transition] = []
    def __init__(self):
        initial = State("q0", "moore", [0, 0], True)
        self.states.append(initial)

    def add_state(self, state):
        self.states.append(state)