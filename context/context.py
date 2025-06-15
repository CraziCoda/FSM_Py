from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QFileSystemWatcher
from typing import Callable
from context.machine import Machine, State, Transition
import json


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppContext(metaclass=SingletonMeta):
    settings: QSettings = None
    main_window: QMainWindow = None
    world_watcher: QFileSystemWatcher = None
    machines: list[str] = []
    world_name: str = ""
    selected_tool = "move"
    selected_machine: Machine = None

    _machines_update_handler: Callable[[], None] = None
    _world_name_update_handler: Callable[[], None] = None
    _tool_change_handler: Callable[[], None] = None
    _selected_machine_change_handler: Callable[[], None] = None

    def set_machines(self, machines: list[str]):
        self.machines = machines
        if self._machines_update_handler:
            self._machines_update_handler()

    def set_handler(self, variable: str, handler: Callable[[], None]):
        if variable == "machines":
            self._machines_update_handler = handler
        if variable == "world_name":
            self._world_name_update_handler = handler
        if variable == "selected_tool":
            self._tool_change_handler = handler
        if variable == "selected_machine":
            self._selected_machine_change_handler = handler

    def set_world_name(self, name: str):
        self.world_name = name
        self.settings.setValue("world_name", name)

        if self._world_name_update_handler:
            self._world_name_update_handler()

    def set_selected_tool(self, tool: str):
        self.selected_tool = tool

        if self._tool_change_handler:
            self._tool_change_handler()

    def set_selected_machine(self, machine: Machine):
        self.selected_machine = machine

        if self._selected_machine_change_handler:
            self._selected_machine_change_handler()

    def load_machine(self, machine_name: str):
        with open(f"{self.settings.value('world_folder')}/{machine_name}", "r") as f:
            data = json.loads(f.read())

            machine = Machine(data["name"], data["type"])

            for state in data["states"]:
                machine_state = State(state["name"], state["location"], state["initial"], state["accepting"])
                machine.add_state(machine_state)

            for transition in data["transitions"]:
                machine.add_transition(Transition(
                    machine.get_state_by_name(transition["source"]),
                    machine.get_state_by_name(transition["target"]),
                    transition["name"]
                ))

            self.set_selected_machine(machine)

    
    def save_machine(self):
        data = {
            "name": self.selected_machine.name,
            "type": self.selected_machine._type,
            "states": [],
            "transitions": []
        }

        for state in self.selected_machine.states:
            data["states"].append({
                "name": state.name,
                "location": state.location,
                "initial": state.initial,
                "accepting": state.accepting
            })

        for transition in self.selected_machine.transitions:
            data["transitions"].append({
                "source": transition.source.name,
                "target": transition.target.name,
                "name": transition.name
            })

        with open(f"{self.settings.value('world_folder')}/{self.selected_machine.name}", "w") as f:
            f.write(json.dumps(data))
