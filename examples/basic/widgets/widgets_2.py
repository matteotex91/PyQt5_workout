import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow_widgets_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("examples/basic/widgets/picture.jpg"))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_widgets_2()
    window.show()
    app.exec_()
