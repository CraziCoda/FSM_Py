from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    

class AppContext(metaclass=SingletonMeta):
    settings: QSettings = None
    main_window: QMainWindow = None