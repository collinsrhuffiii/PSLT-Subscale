from datetime import datetime
from time import sleep
import csv
from altimu import AltIMU

print "ReadAccGyro.py is starting"

imu = AltIMU()
imu.enable(True, False, True, False, False)

start = datetime.now()
quit = False
FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())

while(not quit):
	try:
		dataFile = open("/home/pi/Desktop/PSLT-Subscale/Data/AccGyroData.csv", "a")
		data = "\n"
		stop = datetime.now() - start
		start = datetime.now()
		deltaT = stop.microseconds/1000000.0

		accList = imu.getAccelerometerRaw()
		data += str(accList[0] / 8000.0) + "," + str(accList[1] / 8000.0) + "," + str(accList[2] / 8000.0)
		
		gyroList = imu.trackGyroAngles(deltaT = deltaT)
		data += "," + str(gyroList[0]) + "," + str(gyroList[1]) + "," +str(gyroList[2])
		
		data += ",0"
		
		data += "," + str(datetime.now())
		
		dataFile.write(data)
		dataFile.close()
		
		sleep(1.0 / FREQ)
	
	except KeyboardInterrupt:
		quit = True

print "ReadAccGyro.py is ending"
