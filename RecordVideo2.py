from picamera import PiCamera
import time

print "RecordVideo2.py is starting"

quit = False

with PiCamera() as camera:
	#camera.start_preview()
	camera.start_recording("/media/pi/Samsung USB/video2.h264")

	while(not quit):
		try:
			time.sleep(0.01)

		except KeyboardInterrupt:
			quit = True

	camera.stop_recording()
	#camera.stop_preview()

print "RecordVideo2.py is ending"