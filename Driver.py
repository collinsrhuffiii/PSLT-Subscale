import time
import subprocess
	
print "Starting GPS Daemon"

subprocess.call(["sudo", "killall", "gpsd"])
subprocess.call(["sudo", "gpsd", "/dev/ttyS0", "-F", "/var/run/gpsd.sock"])

print "Waiting 5 seconds"

time.sleep(5)

print "Starting data collection\n"

p1 = subprocess.Popen("python RecordVideo.py", shell=True)
p2 = subprocess.Popen("python ReadGPS.py", shell=True)
p3 = subprocess.Popen("python ./lsm/ReadAccGyro.py", shell=True)

time.sleep(1)

print "\nWaiting 5 seconds"

time.sleep(5)

print "Beginning transmission\n"

p4 = subprocess.Popen("python SendData.py", shell=True)

quit = False

while(not quit):
	try:
		time.sleep(0.01)
	
	except KeyboardInterrupt:
		p1.terminate()
		p2.terminate()
		p3.terminate()
		p4.terminate()
		
		quit = True
			
print "Driver.py is ending"