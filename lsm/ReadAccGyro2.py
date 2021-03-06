from datetime import datetime
import time
import csv
from altimu import AltIMU
import RPi.GPIO as GPIO
import os
import math

print "ReadAccGyro2.py is starting"

imu = AltIMU()
imu.enable(True, True, True, True, True)

FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
GPIO.setmode(GPIO.BOARD)
GPIO.setup([21,23], GPIO.OUT)
p = GPIO.PWM(23, 5120)
start = time.time()
launched = False
launchTime = -1
motorState = 0
quit = False
lastAccList = [0.0, 0.0, 0.0]
lastGyroList = [0.0, 0.0, 0.0]
lastMagList = [0.0, 0.0, 0.0]
lastRot = 0.0
errs = 0

while(not quit):
	try:
		errs = 0
		with open("/home/pi/Desktop/PSLT-Subscale/Data/AccGyroData2.csv", "ab") as dataFile:	
			data = "\n"

			accList = imu.getAccelerometerRaw()

			if(not (accList[0] == None)):
				data += str(accList[0] / 4098.0) + ","
				lastAccList[0] = accList[0]
			else:
				data += str(lastAccList[0] / 4098.0) + ","
				errs += 1

			if(not (accList[1] == None)):
				data += str(accList[1] / 4098.0) + ","
				lastAccList[1] = accList[1]
			else:
				data += str(lastAccList[1] / 4098.0) + ","
				errs += 1

			if(not (accList[2] == None)):
				data += str(accList[2] / 4098.0) + ","
				lastAccList[2] = accList[2]
			else:
				data += str(lastAccList[2] / 4098.0) + ","
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

			rot = math.degrees(math.atan2(lastMagList[1], lastMagList[2]) + math.pi) + 180.0
			data += str(rot) + ","
			
			bar = imu.getAltitude()
			data += str(bar) + ","

			data += "1," if (motorState == 1) else "0,"
			data += str(errs) + ","
			data += str(datetime.now())

			dataFile.write(data)

			dataFile.flush()
			os.fsync(dataFile.fileno())

		if((math.fabs(lastAccList[0] / 4098.0) > 2) & (launchTime == -1)):
			launchTime = time.time()
			launched = True
			print "Launched!"

		timeElapsed = time.time() - launchTime
		if((timeElapsed > 4) & (motorState == 0) & launched):
			GPIO.output(21,1)
			p.start(100)
			motorState = 1
			print "Starting motor"

		if((timeElapsed > 6) & (motorState == 1)):
			p.stop()
			GPIO.output(21,0)
			motorState = 2
			print "Stopping motor"

		time.sleep(1.0 / FREQ)
		
	except KeyboardInterrupt:
		quit = True

GPIO.cleanup()		
print "ReadAccGyro2.py is ending"
