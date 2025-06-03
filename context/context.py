from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QFileSystemWatcher
from typing import Callable


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
    _machines_update_handler: Callable[[], None] = None
    _world_name_update_handler: Callable[[], None] = None
    machine_details = {
        "states": [],
        "transitions": [],
    }
    editor = {
        "selected_machine": None,
        "selected_tool": "move"
    }

    def set_machines(self, machines: list[str]):
        self.machines = machines
        if self._machines_update_handler:
            self._machines_update_handler()

    def set_handler(self, variable: str, handler: Callable[[], None]):
        if variable == "machines":
            self._machines_update_handler = handler
        if variable == "world_name":
            self._world_name_update_handler = handler

    def set_world_name(self, name: str):
        self.world_name = name
        self.settings.setValue("world_name", name)

        if self._world_name_update_handler:
            self._world_name_update_handler()
