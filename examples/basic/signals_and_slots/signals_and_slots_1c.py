import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow_signals_and_slots_1c(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        # Set the central widget of the Window.

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_signals_and_slots_1c()
    window.show()
    app.exec_()
