import numpy as np
import random
import pandas as pd
import time
import serial
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
from socket import *

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

style.use('dark_background')

# data = "38.831435,-77.805762"
bottomLeft = [38.819280, -77.830782]
topRight = [38.843879, -77.780234]


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.axis([bottomLeft[0], topRight[0], bottomLeft[1], topRight[1]])
ax1.set_xlabel("Longitude")
ax1.set_ylabel("Latitude")
ax1.set_title("Position")

ax1.scatter([bottomLeft[0], topRight[0], 38.831435], [bottomLeft[1],topRight[1], -77.805762] )


def animate(i):
	(data, addr) = UDPSock.recvfrom(buf)
	data = data.decode('utf-8')
	ys, xs = data.split(',', 2)
# 	xs = random.uniform(38.819280, 38.843879)
# 	ys = random.uniform(-77.830782, -77.780234)
# 	ax1.clear()
# 	ax1.axis([bottomLeft[0], topRight[0], bottomLeft[1], topRight[1]])
# 	ax1.set_xlabel("Longitude")
# 	ax1.set_ylabel("Latitude")
# 	ax1.set_title("Position")
# 	x0,x1 = ax1.get_xlim()
# 	y0,y1 = ax1.get_ylim()
# 	ax1.imshow(im, extent=[x0, x1, y0, y1], aspect='auto')
# 	print(xs)
# 	print(ys)
	ax1.scatter(xs, ys)
	
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
im = plt.imread("LaunchSiteMap.jpg")
x0,x1 = ax1.get_xlim()
y0,y1 = ax1.get_ylim()
ax1.imshow(im, extent=[x0, x1, y0, y1], aspect='auto')
plt.show()
UDPSock.close()



