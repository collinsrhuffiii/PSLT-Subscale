import serial

ser = serial.Serial("/dev/ttyUSB0" , 9600)
for x in range(26):
	ser.write(unichr(x+65))


