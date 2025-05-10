from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem

class PropertiesWin(QWidget):
    def __init__(self, props: list[dict] = []):
        super().__init__()

        self.props = props

        self.init_ui()
    
    def init_ui(self):
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.setSpacing(0)
        self.setLayout(vLayout)

        table = QTableWidget(len(self.props), 2)
        table.setHorizontalHeaderLabels(["Name", "Value"])

        for i, prop in enumerate(self.props):
            table.setItem(i, 0, QTableWidgetItem(prop["name"]))
            table.setItem(i, 1, QTableWidgetItem(prop["value"]))

        self.layout().addWidget(table)
