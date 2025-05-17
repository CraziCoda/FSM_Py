from PyQt5.QtWidgets import QFileDialog, QAction, QMainWindow
from ui.styles.menu import menu_bar_style
from actions.file import open_folder

class Menu:
    def __init__(self, parent: QMainWindow):
        self.menu_bar = parent.menuBar()
        self.parent = parent

        # style menu bar
        self.menu_bar.setStyleSheet(menu_bar_style)
        self.menu_bar.setFixedHeight(30)

        file_menu = self.menu_bar.addMenu("File")
        
        open_world_action = QAction("Open World", parent)
        open_world_action.triggered.connect(lambda: open_folder(self.parent))
        file_menu.addAction(open_world_action)

        exit_action = QAction("Exit", parent)
        exit_action.triggered.connect(parent.close)
        file_menu.addAction(exit_action)


    def open_world(self):
        QFileDialog.getExistingDirectory(self.parent, "Select World Folder")

