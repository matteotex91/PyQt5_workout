import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow


class MainWindow_widgets_4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_widgets_4()
    window.show()
    app.exec_()
