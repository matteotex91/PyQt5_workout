import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)
from signals_and_slots_1a import MainWindow_signals_and_slots_1a
from signals_and_slots_1b import MainWindow_signals_and_slots_1b
from signals_and_slots_1c import MainWindow_signals_and_slots_1c
from signals_and_slots_1d import MainWindow_signals_and_slots_1d
from signals_and_slots_2 import MainWindow_signals_and_slots_2
from signals_and_slots_3 import MainWindow_signals_and_slots_3


# Subclass QMainWindow to customize your application's main window
class MainWindowSignalsSlotsDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        be1 = QPushButton("Basic example 1a", self)
        be2 = QPushButton("Basic example 1b", self)
        be3 = QPushButton("Basic example 1c", self)
        be4 = QPushButton("Basic example 1d", self)
        be5 = QPushButton("Basic example 2", self)
        be6 = QPushButton("Basic example 3", self)

        be1.move(10, 0)
        be2.move(10, 40)
        be3.move(10, 80)
        be4.move(10, 120)
        be5.move(10, 160)
        be6.move(10, 200)

        be1.setFixedSize(150, 30)
        be2.setFixedSize(150, 30)
        be3.setFixedSize(150, 30)
        be4.setFixedSize(150, 30)
        be5.setFixedSize(150, 30)
        be6.setFixedSize(150, 30)

        be1.clicked.connect(self.open_example_1)
        be2.clicked.connect(self.open_example_2)
        be3.clicked.connect(self.open_example_3)
        be4.clicked.connect(self.open_example_4)
        be5.clicked.connect(self.open_example_5)
        be6.clicked.connect(self.open_example_6)

        self.setFixedSize(QSize(170, 240))

    def open_example_1(self):
        self.window = MainWindow_signals_and_slots_1a()
        self.window.show()

    def open_example_2(self):
        self.window = MainWindow_signals_and_slots_1b()
        self.window.show()

    def open_example_3(self):
        self.window = MainWindow_signals_and_slots_1c()
        self.window.show()

    def open_example_4(self):
        self.window = MainWindow_signals_and_slots_1d()
        self.window.show()

    def open_example_5(self):
        self.window = MainWindow_signals_and_slots_2()
        self.window.show()

    def open_example_6(self):
        self.window = MainWindow_signals_and_slots_3()
        self.window.show()


app = QApplication(sys.argv)
window = MainWindowSignalsSlotsDashboard()
window.show()
app.exec_()
