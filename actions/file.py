from PyQt5.QtWidgets import QFileDialog, QWidget
from context.context import AppContext

def open_folder(parent: QWidget):
    settings = AppContext().settings

    folder = QFileDialog.getExistingDirectory(parent, "Select World Folder")
    if (folder == ""):
        return
    settings.setValue("world_folder", folder)