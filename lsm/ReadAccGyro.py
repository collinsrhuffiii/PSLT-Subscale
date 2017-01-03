from datetime import datetime
import time
import csv
from altimu import AltIMU
import os
import math

print "ReadAccGyro.py is starting"

imu = AltIMU()
imu.enable(True, True, True, True, True)

quit = False
FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
start = time.time()
lastAccList = [0.0, 0.0, 0.0]
lastGyroList = [0.0, 0.0, 0.0]
lastMagList = [0.0, 0.0, 0.0]
lastRot = 0.0
errs = 0

while(not quit):
	try:
		errs = 0
		with open("/home/pi/Desktop/PSLT-Subscale/Data/AccGyroData.csv", "ab") as dataFile:	
			data = "\n"

			accList = imu.getAccelerometerRaw()

			if(not (accList[0] == None)):
				data += str(accList[0] / 8000.0) + ","
				lastAccList[0] = accList[0]
			else:
				data += str(lastAccList[0] / 8000.0) + ","
				errs += 1

			if(not (accList[1] == None)):
				data += str(accList[1] / 8000.0) + ","
				lastAccList[1] = accList[1]
			else:
				data += str(lastAccList[1] / 8000.0) + ","
				errs += 1

			if(not (accList[2] == None)):
				data += str(accList[2] / 8000.0) + ","
				lastAccList[2] = accList[2]
			else:
				data += str(lastAccList[2] / 8000.0) + ","
				errs += 1

			stop = time.time() - start
			start = time.time()
			deltaT = stop
			gyroList = imu.getComplementaryAngles(deltaT=deltaT)

			if(not (gyroList[0] == None)):
				data += str(gyroList[0]) + ","
				lastGyroList[0] = gyroList[0]
			else:
				data += str(lastGyroList[0]) + ","
				errs += 1

			if(not (gyroList[1] == None)):
				data += str(gyroList[1]) + ","
				lastGyroList[1] = gyroList[1]
			else:
				data += str(lastGyroList[1]) + ","
				errs += 1

			if(not (gyroList[2] == None)):
				data += str(gyroList[2]) + ","
				lastGyroList[2] = gyroList[2]
			else:
				data += str(lastGyroList[2]) + ","
				errs += 1
			
			magList = imu.getMagnetometerRaw()
			
			if(not (magList[0] == None)):
				data += str(magList[0]) + ","
				lastMagList[0] = magList[0]
			else:
				data += str(lastMagList[0]) + ","
				errs += 1

			if(not (magList[1] == None)):
				data += str(magList[1]) + ","
				lastMagList[1] = magList[1]
			else:
				data += str(lastMagList[1]) + ","
				errs += 1

			if(not (magList[2] == None)):
				data += str(magList[2]) + ","
				lastMagList[2] = magList[2]
			else:
				data += str(lastMagList[2]) + ","
				errs += 1
			
			rot = math.degrees(math.atan2(lastMagList[1], lastMagList[2]))
			data += str(rot) + ","

			data += "0,"
			data += str(errs) + ","
			data += str(datetime.now())

			dataFile.write(data)
			
			dataFile.flush()
			os.fsync(dataFile.fileno())
		
		time.sleep(1.0 / FREQ)
	
	except KeyboardInterrupt:
		quit = True

print "ReadAccGyro.py is ending"
