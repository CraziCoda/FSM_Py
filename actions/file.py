from PyQt5.QtWidgets import QFileDialog, QWidget
from context.context import AppContext
import os

def open_folder(parent: QWidget):
    settings = AppContext().settings
    world_watcher = AppContext().world_watcher

    folder = QFileDialog.getExistingDirectory(parent, "Select World Folder")
    if (folder == ""):
        return
    settings.setValue("world_folder", folder)

    for path in world_watcher.directories():
        world_watcher.removePath(path)
    world_watcher.addPath(folder)

    get_machines_in_world()

def get_machines_in_world():
    folder = AppContext().settings.value("world_folder")
    _machines = []
    for file in os.listdir(folder):
        if file.endswith(".fsm"):
            _machines.append(file)
    AppContext().set_machines(_machines)
