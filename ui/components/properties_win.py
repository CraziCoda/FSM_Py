from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem
from ui.styles.components import *

class PropertiesWin(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        self.table = QTableWidget(1, 2)
        self.table.setAlternatingRowColors(True)
        self.table.setHorizontalHeaderLabels(["Name", "Value"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(True)
        self.table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        self.layout().addWidget(self.table, 1)
        self.setStyleSheet(props_window_style)

    def load_props(self, props: list[dict]):
        self.table.setRowCount(0)
        for prop in props:
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(prop["name"]))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(prop["value"], ))
