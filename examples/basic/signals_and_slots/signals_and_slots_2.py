from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow_signals_and_slots_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        # Also change the window title.
        self.setWindowTitle("My Oneshot App")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_signals_and_slots_2()
    window.show()
    app.exec_()
