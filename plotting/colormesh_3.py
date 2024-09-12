"""NOT WORKING"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

app = pg.mkQApp("Data Slicing Example")

## Create window with two ImageView widgets
win = QtWidgets.QMainWindow()
win.resize(800, 800)
win.setWindowTitle("pyqtgraph example: DataSlicing")
cw = QtWidgets.QWidget()
win.setCentralWidget(cw)
l = QtWidgets.QGridLayout()
cw.setLayout(l)
imv1 = pg.PlotWidget()
imv2 = pg.PlotWidget()
l.addWidget(imv1, 0, 0)
l.addWidget(imv2, 1, 0)
win.show()


x = np.linspace(-2, 2, 200)
gaussian = np.exp(-np.power(0.5 * (x[:-1] + x[1:]), 2))
gaussian2d = np.tensordot(gaussian, gaussian, axes=0)
xv, yv = np.meshgrid(x, x)
plot_curve = pg.PlotCurveItem()
imv2.addItem(plot_curve)
pcolormesh_item = pg.PColorMeshItem(xv, yv, gaussian2d)
imv1.addItem(pcolormesh_item)
roi = pg.LineSegmentROI([[-2, -2], [2, 2]], pen="r", parent=pcolormesh_item)
imv1.addItem(roi)


def update():
    global roi, gaussian2d, xv, yv, plot_curve
    print("stop here")
    # d2 = roi.getArrayRegion(gaussian2d, imv1.currentItem)
    d2 = roi.getArraySlice(gaussian2d, imv1.currentItem)
    plot_curve.setData(d2)
    # imv2.addItem(pg.PlotCurveItem(d2))


roi.sigRegionChanged.connect(update)


## Display the data


update()

if __name__ == "__main__":
    pg.exec()
