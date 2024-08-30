import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
)


class MainWindowExample4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        # Set the central widget of the Window.

        self.setCentralWidget(button)


class MainWindowExample5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


# Subclass QMainWindow to customize your application's main window
class MainWindowBasicDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        be1 = QPushButton("Basic example 1", self)
        be2 = QPushButton("Basic example 2", self)
        be3 = QPushButton("Basic example 3", self)
        be4 = QPushButton("Basic example 4", self)
        be5 = QPushButton("Basic example 5", self)

        be1.move(10, 0)
        be2.move(10, 40)
        be3.move(10, 80)
        be4.move(10, 120)
        be5.move(10, 160)

        be1.setFixedSize(150, 30)
        be2.setFixedSize(150, 30)
        be3.setFixedSize(150, 30)
        be4.setFixedSize(150, 30)
        be5.setFixedSize(150, 30)

        be1.clicked.connect(self.open_example_1)
        be2.clicked.connect(self.open_example_2)
        be3.clicked.connect(self.open_example_3)
        be4.clicked.connect(self.open_example_4)
        be5.clicked.connect(self.open_example_5)

        self.setFixedSize(QSize(170, 200))

    def open_example_1(self):
        self.window = QWidget()
        self.window.show()

    def open_example_2(self):
        self.window = QPushButton("Push Me")
        self.window.show()

    def open_example_3(self):
        self.window = QMainWindow()
        self.window.show()

    def open_example_4(self):

        self.window = MainWindowExample4()
        self.window.show()

    def open_example_5(self):
        self.window = MainWindowExample5()
        self.window.show()


app = QApplication(sys.argv)
window = MainWindowBasicDashboard()
window.show()
app.exec_()
