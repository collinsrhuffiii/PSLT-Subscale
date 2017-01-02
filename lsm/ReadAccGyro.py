from datetime import datetime
import time
import csv
from altimu import AltIMU

print "ReadAccGyro.py is starting"

imu = AltIMU()
imu.enable(True, False, True, False, False)

start = time.time()
quit = False
FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
#lastTime = time.time()
start = time.time()
lastAccList = [0.0, 0.0, 0.0]
lastGyroList = [0.0, 0.0, 0.0]

while(not quit):
	try:
		dataFile = open("/home/pi/Desktop/PSLT-Subscale/Data/AccGyroData.csv", "a")
		data = "\n"

		accList = imu.getAccelerometerRaw()
		
		if(not (accList[0] == None)):
			data += str(accList[0] / 8000.0) + ","
			lastAccList[0] = accList[0]
		else:
			data += str(lastAccList[0] / 8000.0) + ","
			
		if(not (accList[1] == None)):
			data += str(accList[1] / 8000.0) + ","
			lastAccList[1] = accList[1]
		else:
			data += str(lastAccList[1] / 8000.0) + ","
			
		if(not (accList[2] == None)):
			data += str(accList[2] / 8000.0) + ","
			lastAccList[2] = accList[2]
		else:
			data += str(lastAccList[2] / 8000.0) + ","
		
		stop = time.time() - start
		start = time.time()
		deltaT = stop
		#while(time.time() - (1.0 / FREQ) < lastTime):
		#	pass
		gyroList = imu.getComplementaryAngles(deltaT=deltaT)
		lastTime = time.time()
		#print gyroList
		
		if(not (gyroList[0] == None)):
			data += str(gyroList[0]) + ","
			lastGyroList[0] = gyroList[0]
		else:
			data += str(lastGyroList[0]) + ","

		if(not (gyroList[1] == None)):
			data += str(gyroList[1]) + ","
			lastGyroList[1] = gyroList[1]
		else:
			data += str(lastGyroList[1]) + ","

		if(not (gyroList[2] == None)):
			data += str(gyroList[2]) + ","
			lastGyroList[2] = gyroList[2]
		else:
			data += str(lastGyroList[2]) + ","
		
		data += "0"
		
		data += "," + str(datetime.now())
		
		dataFile.write(data)
		dataFile.close()
		
		time.sleep(1.0 / FREQ)
	
	except KeyboardInterrupt:
		quit = True

print "ReadAccGyro.py is ending"
