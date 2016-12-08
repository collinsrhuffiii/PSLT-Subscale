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
import math


df = pd.read_csv("exData.csv")

app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)

win = pg.GraphicsWindow(title="PSLT Subscale")
win.resize(1000,600)
win.setWindowTitle('PSLT Subscale')

pg.setConfigOptions(antialias=True)

alt = np.array(df[df.columns[3]].values) * 3.2808
p1 = win.addPlot(title="Altitude")
curve1 = p1.plot(pen='y')

vel = np.array(df[df.columns[2]].values) * 3.2808
p2 = win.addPlot(title="Velocity")
curve2 = p2.plot(pen='c')

win.nextRow()

acc = np.array(df[df.columns[1]].values)
p3 = win.addPlot(title="Acceleration")
curve3 = p3.plot(pen='m')

p4 = win.addPlot(title = "Rotation")
p4.setAspectLocked()
p4.addLine(x=0, pen=0.2)
p4.addLine(y=0, pen=0.2)
for r in range(2, 20, 2):
    circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r*2, r*2)
    circle.setPen(pg.mkPen(0.2))
    p4.addItem(circle)
   
angle = math.radians(df.iloc[0][9])
theta = np.linspace(angle, angle, 100)
radius = np.linspace(0, 18, 100)

x1 = radius * np.cos(theta)
y1 = radius * np.sin(theta)
curve4 = p4.plot(pen='r')
curve4.setData(y1,x1)


# p5 = win.addPlot(title="Lat, lon")
# lat = np.array(df[df.columns[1]].values)
# lon = np.array(df[df.columns[2]].values)
# curve5 = p4.plot(pen='r', x = lon, y = lat)

def update():
 	global curve1, curve2, curve3, curve4, data, ptr, p1, p2, p3, p4, p5, x1, y1
	df = pd.read_csv("exData.csv")
 	time = np.array(df[df.columns[13]].values)
	alt = np.array(df[df.columns[4]].values) * 3.2808
	vel = np.array(df[df.columns[3]].values) * 3.2808
	acc = np.array(df[df.columns[8]].values)
	lat = np.array(df[df.columns[1]].values)
	lon = np.array(df[df.columns[2]].values)
	angle = math.radians(df.iloc[-1][9])
	
	curve1.setData(alt)
	curve2.setData(vel)
	curve3.setData(acc)
	
	theta = np.linspace(angle, angle, 100)
	radius = np.linspace(0, 18, 100)
	x1 = radius * np.cos(theta)
	y1 = radius * np.sin(theta)
	if(df.iloc[-1][13] == 1):
		curve4.setData(y1,x1, pen='g')
	else:
		curve4.setData(y1,x1, pen='r')
# 	curve5.setData(lon, lat)
	
     
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
