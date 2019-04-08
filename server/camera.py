#!/usr/bin/python
import picamera
import time

def takePhoto():
    camera = picamera.PiCamera()
    camera.capture('cameraTest.jpg')
    camera.close()

#camera.start_recording('videoTest.h264')
#time.sleep(5)
#camera.stop_recording()

