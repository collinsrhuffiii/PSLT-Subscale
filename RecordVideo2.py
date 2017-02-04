from picamera import PiCamera
import time
import os

print "RecordVideo2.py is starting"

quit = False

with PiCamera() as camera:
	#camera.start_preview()
	videoFile = open("/media/pi/Samsung USB/video2.h264", "wb")
	camera.start_recording(videoFile)

	while(not quit):
		try:
			videoFile.flush()
			os.fsync(videoFile.fileno())
			
			time.sleep(0.01)

		except KeyboardInterrupt:
			quit = True

	camera.stop_recording()
	#camera.stop_preview()

print "RecordVideo2.py is ending"