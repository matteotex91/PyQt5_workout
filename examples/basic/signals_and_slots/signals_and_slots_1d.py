import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow_signals_and_slots_1d(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_signals_and_slots_1d()
    window.show()
    app.exec_()
