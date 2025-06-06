from PyQt5.QtWidgets import QGraphicsItem, QMessageBox


class State:
    name = ""
    initial = False
    accepting = False
    location = [0, 0]
    _drawn_item: QGraphicsItem = None


    def __init__(self, name, location, initial=False, accepting=False):
        self.name = name
        self.initial = initial
        self.location = location
        self.accepting = accepting

    def set_drawn_item(self, item: QGraphicsItem):
        self._drawn_item = item

    def get_drawn_item(self):
        return self._drawn_item


class Transition:
    def __init__(self, source: State, target: State, name: str = ""):
        self.source: State = source
        self.target: State = target
        self.name = name



class Machine:

    def __init__(self, name, type, initial_state: State = None):
        self.name = name
        self._type = type
        self.states: list[State] = []
        self.transitions: list[Transition] = []

        if initial_state:
            self.states.append(initial_state)

    def add_state(self, state: State):
        for s in self.states:
            if s.name == state.name:
                return QMessageBox.critical(None, "Error", f"State with name {state.name} already exists")
        self.states.append(state)

    def add_transition(self, transition: Transition):
        self.transitions.append(transition)

    def get_state_by_name(self, name: str):
        for state in self.states:
            if state.name == name:
                return state

    def __str__(self):
        return f"Machine: {self.name} ({self._type}) with {len(self.states)} states"