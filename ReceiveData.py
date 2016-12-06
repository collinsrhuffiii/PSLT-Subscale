import serial
import time

ser = serial.Serial("COM3", 9600)
quit = False

while(not quit):
	try:
		data = ser.readline()
		with open("exData.csv", 'a') as f:
			f.write(data)
	
		time.sleep(0.01)
		
	except KeyboardInterrupt:
		quit = True