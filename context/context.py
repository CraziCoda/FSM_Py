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
    _machines_update_handler: Callable[[], None] = None


    def set_machines(self, machines: list[str]):
        self.machines = machines
        if self._machines_update_handler:
            self._machines_update_handler()


    def set_handler(self, variable: str, handler: Callable[[], None]):
        if variable == "machines":
            self._machines_update_handler = handler
