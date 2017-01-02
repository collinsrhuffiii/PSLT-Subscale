from datetime import datetime
import time
import csv
from altimu import AltIMU
import RPi.GPIO as GPIO

print "ReadAccGyro2.py is starting"

imu = AltIMU()
imu.enable(True, False, True, False, False)

start = datetime.now()
launched = False
launchTime = -1
motorState = 0
quit = False
FREQ = float(open("/home/pi/Desktop/PSLT-Subscale/FREQ.txt", 'r').read())
GPIO.setmode(GPIO.BOARD)
GPIO.setup([21,23], GPIO.OUT)
p = GPIO.PWM(23, 5120)

while(not quit):
	try:
		dataFile = open("/home/pi/Desktop/PSLT-Subscale/Data/AccGyroData2.csv", "a")
		data = "\n"
		stop = datetime.now() - start
		start = datetime.now()
		deltaT = stop.microseconds/1000000.0

		accList = imu.getAccelerometerRaw()
		data += str(accList[0] / 8000.0) + "," + str(accList[1] / 8000.0) + "," + str(accList[2] / 8000.0)

		gyroList = imu.trackGyroAngles(deltaT = deltaT)
		data += "," + str(gyroList[0]) + "," + str(gyroList[1]) + "," +str(gyroList[2])
		
		data += ","
		data += "1" if (motorState == 1) else "0"

		data += "," + str(datetime.now())

		dataFile.write(data)
		dataFile.close()


		if((abs(accList[0] / 8000.0) > 2) & (launchTime == -1)):
			launchTime = time.time()
			launched = True
			print "Launched!"

		timeElapsed = time.time() - launchTime
		#print "Time elapsed: " + str(timeElapsed)
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
