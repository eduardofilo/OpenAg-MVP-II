#!/usr/bin/python
import time
import picamera
import datetime as dt

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 1280)
    camera.framerate = 30
    # calentamiento/enfoque de la camara
    time.sleep(2)
    # fijamos valores para que salga mejor el timelapse
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = "/home/pi/MVP/pictures/" + time.strftime("%Y-%m-%d_%H%M.jpg")
    camera.capture(filename)
