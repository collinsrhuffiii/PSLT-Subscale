from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
camera.start_recording("/media/pi/Samsung USB/video2.h264")
time.sleep(30)
camera.stop_recording()
camera.stop_preview()
