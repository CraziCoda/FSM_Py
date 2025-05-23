from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QToolButton
from PyQt5.QtGui import QIcon

class LabelIcon(QWidget):
    def __init__(self, icon: QIcon, text: str, parent=None):
        super().__init__(parent)
        self.icon = icon
        self.text = text
        self.init_ui()

    def init_ui(self):
        hLayout = QHBoxLayout()
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)
        self.setLayout(hLayout)

        self.icon_label = QLabel(self.text)
        self.tool_button = QToolButton()
        self.tool_button.setIcon(self.icon)

        hLayout.addWidget(self.icon_label)
        hLayout.addWidget(self.tool_button)
