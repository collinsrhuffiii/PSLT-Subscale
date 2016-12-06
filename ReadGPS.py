import gps
import csv
import time
from datetime import datetime

print "ReadGPS.py is starting"

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
quit = False

while(not quit):
	try:
		report = session.next()
		dataFile = open("/home/pi/Desktop/PSLT-Subscale/Data/GPSData.csv", "a")
		data = "\n"
		if report["class"] == "TPV":
			if hasattr(report, "lat"):
				data += str(report.lat) + ","
			if hasattr(report, "lon"):
				data += str(report.lon) + ","
			if hasattr(report, "climb"):
				data += str(report.climb) + ","
			if hasattr(report, "alt"):
				data += str(report.alt) + ","
			if hasattr(report, "speed"):
				data += str(report.speed) + ","
			data += str(datetime.now())
			dataFile.write(data)
			
		dataFile.close()
			
		time.sleep(1.0 / FREQ)
		
	except KeyboardInterrupt:
		quit = True
		
print "ReadGPS.py is ending"