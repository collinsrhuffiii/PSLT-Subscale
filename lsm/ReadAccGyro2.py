from datetime import datetime
import time
import csv
from altimu import AltIMU


imu = AltIMU()
imu.enable()
imu.calibrateGyroAngles()

start = datetime.now()
launched = False
launchTime = -1
motorState = 0
FREQ = 2

while True:
	dataFile = open("AccGyroData2.csv", "a")
	data = "\n"
	stop = datetime.now() - start
	start = datetime.now()
	deltaT = stop.microseconds/1000000.0
	
	accList = imu.getAccelerometerAngles()
	data += str(accList[0]) + "," + str(accList[1]) + "," + str(accList[2])
	gyroList = imu.trackGyroAngles(deltaT = deltaT)
	data += "," + str(gyroList[0]) + "," + str(gyroList[1]) + "," +str(gyroList[2])
	dataFile.write(data)
	dataFile.close()
	
	
	if((acc	List[1] / 8000.0) > 2 & launchTime == -1):
		launchTime = time.time()
		launched = True
	
	timeElapsed = time.time() - launchTime
	if(timeElapsed > 4 & motorState == 0 & launched):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup([21,23], GPIO.OUT)
		GPIO.output(21,1)
		p = GPIO.PWM(23, 5120)
		p.start(100)
		motorState = 1
	
	if(timeElapsed > 6 & motorState == 1):
		p.stop()
		GPIO.output(21,0)
		GPIO.cleanup()
		motorState = 2
		
	time.sleep(1.0 / FREQ)