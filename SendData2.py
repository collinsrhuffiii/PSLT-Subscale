import time
import serial
import csv
from collections import deque

def get_last_row(csv_filename):
	with open(csv_filename, 'rb') as f:
		try:
			lastrow = deque(csv.reader(f), 1)[0]
		except IndexError:  # empty file
			lastrow = None
	return lastrow


ser = serial.Serial("/dev/ttyUSB0", 9600)
quit = False;
index = 0
FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())

while(not quit):
	try:
		gpsData = get_last_row("/home/pi/Desktop/PSLT-Subscale/GPSData2.csv")
		agData = get_last_row("/home/pi/Desktop/PSLT-Subscale/lsm/AccGyroData2.csv")

		dataList = [index] + gpsData + agData

		data = ""
		for d in dataList:
			data += str(d) + ','
		data = data[:-1]
		data += '\n'

		print data
		ser.write(data)

		index += 1
		
		time.sleep(1.0 / FREQ)
	except KeyboardInterrupt:
		quit = True

print "Sent " + str(index) + " packets"