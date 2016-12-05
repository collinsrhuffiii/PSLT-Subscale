import gps
import csv
import time

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
quit = False

while(not quit):
	try:
		report = session.next()
		dataFile = open("GPSData.csv", "a")
		data = "\n"
		if report["class"] == "TPV":
			if hasattr(report, "lat"):
				data += str(report.lat) + ","
			if hasattr(report, "lon"):
				data += str(report.lon) + ","
			if hasattr(report, "climb"):
				data += str(report.climb) + ","
			if hasattr(report, "altitude"):
				data += str(report.altitude) + ","
			if hasattr(report, "speed"):
				data += str(report.speed) + ","
			if hasattr(report, "time"):
				data += str(report.time)
			dataFile.write(data)

		time.sleep(1.0 / FREQ)
	except KeyboardInterrupt:
		quit = True
