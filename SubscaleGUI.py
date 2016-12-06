# -*- coding: utf-8 -*-
"""
Display data from xbee
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pandas as pd
import csv
import serial
import time
import os


df = pd.read_csv("exData.csv")

app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="PSLT Subscale")
win.resize(1000,600)
win.setWindowTitle('PSLT Subscale')


pg.setConfigOptions(antialias=True)

alt = np.array(df[df.columns[3]].values)
p1 = win.addPlot(title="Altitude", y = alt)
curve1 = p1.plot(pen='y')



vel = np.array(df[df.columns[2]].values)
p2 = win.addPlot(title="Velocity", y = vel)
curve2 = p2.plot(pen='c')



win.nextRow()

acc = np.array(df[df.columns[1]].values)
p3 = win.addPlot(title="Acceleration")
curve3 = p3.plot(pen='m', y = acc)




p4 = win.addPlot(title="Lat, lon")
curve4 = p4.plot(pen='y')

def update():
	global curve, curve2, data, ptr, p1, p2
	df = pd.read_csv("exData.csv")
	alt = np.array(df[df.columns[3]].values)
	vel = np.array(df[df.columns[2]].values)
	acc = np.array(df[df.columns[1]].values)
	curve1.setData(alt)
	curve2.setData(vel)
	curve3.setData(acc)
     #curve4.setData(alt[ptr])
	
     
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)




## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
