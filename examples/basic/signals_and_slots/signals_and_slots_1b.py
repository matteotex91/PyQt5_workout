import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow_signals_and_slots_1b(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_signals_and_slots_1b()
    window.show()
    app.exec_()
