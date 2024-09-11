import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x = np.linspace(-2, 2, 200)
        gaussian = np.exp(-np.power(0.5 * (x), 2))
        self.plot_widget = pg.PlotWidget()
        self.plot_graph = pg.PlotCurveItem(gaussian)
        self.plot_widget.addItem(self.plot_graph)
        self.setCentralWidget(self.plot_widget)
        # self.plot_graph.plot(x, x, gaussian2d)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

print("stop here")
