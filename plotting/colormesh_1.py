import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, QEvent, QThread, QObject, QMutex
from PyQt5.QtGui import QMouseEvent
import sys
import numpy as np
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        x = np.linspace(-2, 2, 200)
        gaussian = np.exp(-np.power(x, 2))
        gaussian2d = np.tensordot(gaussian, gaussian, axes=0)
        xv, yv = np.meshgrid(x, x)
        self.plot_widget = pg.PlotWidget()
        self.plot_graph = pg.PColorMeshItem(xv, yv, gaussian2d[1:, 1:])
        self.plot_widget.addItem(self.plot_graph)
        self.setCentralWidget(self.plot_widget)
        # self.plot_graph.plot(x, x, gaussian2d)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

print("stop here")
