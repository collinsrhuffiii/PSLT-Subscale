from picamera import PiCamera
import time

print "RecordVideo.py is starting"

quit = False

with PiCamera() as camera:
	#camera.start_preview()
	camera.start_recording("/media/pi/Samsung USB/video.h264")

	while(not quit):
		try:
			time.sleep(0.01)

		except KeyboardInterrupt:
			quit = True

	camera.stop_recording()
	#camera.stop_preview()

print "RecordVideo.py is ending"