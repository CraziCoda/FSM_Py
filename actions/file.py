from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import QSettings

def open_folder(parent: QWidget, settings: QSettings):
    folder = QFileDialog.getExistingDirectory(parent, "Select World Folder")
    if (folder == ""):
        return
    settings.setValue("world_folder", folder)