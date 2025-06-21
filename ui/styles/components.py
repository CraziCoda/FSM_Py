world_list_style = """
QListWidget {
    font-family: 'Segoe UI';
    color: red;
    background-color: #ffffff;
}

QListWidget::item {
    border-bottom: 1px solid #eeeeee;
    color: #000000;
    font-family: 'Segoe UI';
    font-size: 1px;
    font-weight: 400;
    padding: 5px 0;
    height: 20px;
    margin: 0;
}

QListWidget::item:selected {
    margin: 0;
    padding: 0;
    background-color: #4cadfc;
}
"""

world_list_scroll_style = """
QScrollArea {
    border: 1px solid #aaaacc;
    border-top: none;
    background-color: #ffffff;
}
"""

tools_list_style = """
QListWidget {
    padding: 0;
    margin: 0;
}
QListWidget::item {
    margin: 0;
    padding: 0;
    border-bottom: 1px solid #cccccc;
    margin-bottom: 10px;
}
QListWidget::item:selected {
    background-color: #aaaaaf;
    border-radius: 4px;       
    padding: 2px 0;
    width: 100%;
}
"""

world_name_style = """
QLabel {
   font-weight: 500; 
   font-family: 'Segoe UI'; 
   font-size: 16px; 
   border: 1px solid #aaaacc; 
   border-bottom: none;
   border-right: none;
   background-color: #ffffff; 
   padding: 2px;
}
"""

new_machine_button_style = """
QToolButton {
    background-color: #ffffff;
    border: 1px solid #aaaacc;
    border-bottom: none;
    border-left: none;
    padding: 2px;
    padding-right: 5px;
}
"""

world_menu_button_style = """
QToolButton {
    background-color: #ffffff;
    border: 1px solid #aaaacc;
    border-bottom: none;
    border-left: none;
    padding: 2px;
}

QToolButton::menu-indicator { image: none; }
"""

controls_group_box_style = """
QGroupBox {
    padding-left: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
}
"""

control_buttons_style = """
QToolButton {
    background-color: transparent;
    border: 1px solid #aaaacc;
    padding: 2px;
    margin-left: 5px;
}
"""

props_window_style = """
QWidget {
    background-color: #f8f9fa;
    font-family: Segoe UI, sans-serif;
    font-size: 14px;
}
QHeaderView::section {
    background-color: #343a40;
    color: white;
    padding: 8px;
    border: none;
    border-right: 1px solid #ced4da;
}
QTableWidget {
    border: 1px solid #ced4da;
    gridline-color: #dee2e6;
    selection-background-color: #e9ecef;
    alternate-background-color: #f1f3f5;
}
QTableWidget::item {
    padding: 6px;
}
QLineEdit, QComboBox {
    border: 1px solid #ced4da;
    border-radius: 4px;
    padding: 4px 6px;
    background: white;
}
QCheckBox {
    margin-left: 6px;
} 
"""
