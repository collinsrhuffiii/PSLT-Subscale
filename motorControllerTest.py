import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup([21,23], GPIO.OUT)
GPIO.output(21,1)
p = GPIO.PWM(23, 5120)
p.start(100)

time.sleep(5)

p.stop()

GPIO.output(21,0)

GPIO.cleanup()



