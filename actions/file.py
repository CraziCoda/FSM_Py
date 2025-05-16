from PyQt5.QtWidgets import QFileDialog, QWidget
from context.context import AppContext

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

def get_machines_in_world():
    pass