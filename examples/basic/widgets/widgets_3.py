import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow_widgets_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QCheckBox("This is a checkbox")
        # widget.setCheckState(Qt.Checked)
        widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_widgets_3()
    window.show()
    app.exec_()
