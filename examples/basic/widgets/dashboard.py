import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
from widgets_1 import MainWindow_widgets_1
from widgets_2 import MainWindow_widgets_2
from widgets_3 import MainWindow_widgets_3
from widgets_4 import MainWindow_widgets_4
from widgets_5 import MainWindow_widgets_5
from widgets_6 import MainWindow_widgets_6
from widgets_7 import MainWindow_widgets_7
from widgets_8 import MainWindow_widgets_8
from widgets_9 import MainWindow_widgets_9


# Subclass QMainWindow to customize your application's main window
class MainWindowWidgetsDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        be1 = QPushButton("Basic example 1", self)
        be2 = QPushButton("Basic example 2", self)
        be3 = QPushButton("Basic example 3", self)
        be4 = QPushButton("Basic example 4", self)
        be5 = QPushButton("Basic example 5", self)
        be6 = QPushButton("Basic example 6", self)
        be7 = QPushButton("Basic example 7", self)
        be8 = QPushButton("Basic example 8", self)
        be9 = QPushButton("Basic example 9", self)

        be1.move(10, 0)
        be2.move(10, 40)
        be3.move(10, 80)
        be4.move(10, 120)
        be5.move(10, 160)
        be6.move(10, 200)
        be7.move(10, 240)
        be8.move(10, 280)
        be9.move(10, 320)

        be1.setFixedSize(150, 30)
        be2.setFixedSize(150, 30)
        be3.setFixedSize(150, 30)
        be4.setFixedSize(150, 30)
        be5.setFixedSize(150, 30)
        be6.setFixedSize(150, 30)
        be7.setFixedSize(150, 30)
        be8.setFixedSize(150, 30)
        be9.setFixedSize(150, 30)

        be1.clicked.connect(self.open_example_1)
        be2.clicked.connect(self.open_example_2)
        be3.clicked.connect(self.open_example_3)
        be4.clicked.connect(self.open_example_4)
        be5.clicked.connect(self.open_example_5)
        be6.clicked.connect(self.open_example_6)
        be7.clicked.connect(self.open_example_4)
        be8.clicked.connect(self.open_example_5)
        be9.clicked.connect(self.open_example_6)

        self.setFixedSize(QSize(170, 360))

    def open_example_1(self):
        self.window = MainWindow_widgets_1()
        self.window.show()

    def open_example_2(self):
        self.window = MainWindow_widgets_2()
        self.window.show()

    def open_example_3(self):
        self.window = MainWindow_widgets_3()
        self.window.show()

    def open_example_4(self):
        self.window = MainWindow_widgets_4()
        self.window.show()

    def open_example_5(self):
        self.window = MainWindow_widgets_5()
        self.window.show()

    def open_example_6(self):
        self.window = MainWindow_widgets_6()
        self.window.show()

    def open_example_7(self):
        self.window = MainWindow_widgets_7()
        self.window.show()

    def open_example_8(self):
        self.window = MainWindow_widgets_8()
        self.window.show()

    def open_example_9(self):
        self.window = MainWindow_widgets_9()
        self.window.show()


app = QApplication(sys.argv)
window = MainWindowWidgetsDashboard()
window.show()
app.exec_()
