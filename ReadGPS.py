import gps
import csv
import time
from datetime import datetime

print "ReadGPS.py is starting"

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
quit = False
lastLat = 0.0
lastLon = 0.0
lastClimb = 0.0
lastAlt = 0.0
lastSpeed = 0.0
lastTrack = 0.0

while(not quit):
	try:
		report = session.next()
		dataFile = open("/home/pi/Desktop/PSLT-Subscale/Data/GPSData.csv", "a")
		data = "\n"
		if report["class"] == "TPV":
			if hasattr(report, "lat"):
				data += str(report.lat) + ","
				lastLat = report.lat
			else:
				data += str(lastLat) + ","
				
			if hasattr(report, "lon"):
				data += str(report.lon) + ","
				lastLon = report.lon
			else:
				data += str(lastLon) + ","
				
			if hasattr(report, "climb"):
				data += str(report.climb) + ","
				lastClimb = report.climb
			else:
				data += str(lastClimb) + ","
				
			if hasattr(report, "alt"):
				data += str(report.alt) + ","
				lastAlt = report.alt
			else:
				data += str(lastAlt) + ","
				
			if hasattr(report, "speed"):
				data += str(report.speed) + ","
				lastSpeed = report.speed
			else:
				data += str(lastSpeed) + ","
				
			if hasattr(report, "track"):
				data += str(report.track) + ","
				lastTrack = report.track
			else:
				data += str(lastTrack) + ","

			data += str(datetime.now())
			dataFile.write(data)
						
		dataFile.close()
			
		time.sleep(1.0 / FREQ)
		
	except KeyboardInterrupt:
		quit = True
		
print "ReadGPS.py is ending"