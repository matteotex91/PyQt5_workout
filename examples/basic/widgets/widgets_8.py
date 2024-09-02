import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow_widgets_8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QSlider()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow_widgets_8()
    window.show()
    app.exec_()
