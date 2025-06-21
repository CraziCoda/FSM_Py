from PyQt5.QtWidgets import QGraphicsItem, QMessageBox
from typing import Callable


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
        self._handles: list[Callable[[], None]] = []

        self.output: str | None = None

    def set_drawn_item(self, item: QGraphicsItem):
        self._drawn_item = item

    def get_drawn_item(self):
        return self._drawn_item

    def set_location(self, location):
        self.location = location

        for handle in self._handles:
            handle()

    def add_handle(self, handle: Callable[[], None]):
        self._handles.append(handle)

    def __str__(self):
        return f"State: {self.name}"


class Transition:
    _drawn_item: QGraphicsItem = None
    def __init__(self, source: State, target: State, name: str = ""):
        self.source: State = source
        self.target: State = target
        self.name = name
        self.output: str | None = None

    def set_drawn_item(self, item: QGraphicsItem):
        self._drawn_item = item
    
    def get_drawn_item(self):
        return self._drawn_item
    
    def __str__(self):
        return f"Transition: {self.name}"

class Machine:
    def __init__(self, name, type, initial_state: State = None):
        self.name = name
        self._type = type
        self.states: list[State] = []
        self.transitions: list[Transition] = []
        self.selected_item: State | Transition | None = None

        if initial_state:
            self.states.append(initial_state)

    def add_state(self, state: State):
        for s in self.states:
            if s.name == state.name:
                QMessageBox.critical(None, "Error", 
                                     f"State with name {state.name} already exists")
                return None
        self.states.append(state)
        return State

    def add_transition(self, transition: Transition):
        self.transitions.append(transition)

    def get_state_by_name(self, name: str):
        for state in self.states:
            if state.name == name:
                return state

    def __str__(self):
        return f"Machine: {self.name} ({self._type}) with {len(self.states)} states"
