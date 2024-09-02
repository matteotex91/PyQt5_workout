import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow


class MainWindow_widgets_5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        # In QListWidget there are two separate signals for the item, and the str
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):  # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s):  # s is a str
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_widgets_5()
    window.show()
    app.exec_()
