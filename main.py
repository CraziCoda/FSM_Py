from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()