world_list_style = """
QListWidget {
    font-family: 'Segoe UI';
    color: #000000;
}

QListWidget::item {
    border-bottom: 1px solid #eeeeee;
    color: #000000;
    font-family: 'Segoe UI';
    font-size: 14px;
    padding: 5px 0;
    height: 20px;
    margin: 0;c
}

QListWidget::item:selected {
    margin: 0;
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