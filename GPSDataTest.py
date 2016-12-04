import gps
import time
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
while True:
	report = session.next()
	if report["class"] == "TPV":
		if hasattr(report, "lat"):
			print report.lat
		if hasattr(report, "lon"):
			print report.lon
	time.sleep(1)


